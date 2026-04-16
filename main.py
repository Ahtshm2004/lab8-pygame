import sys
import random
import math
import pygame
from typing import List, Tuple, Dict, Optional


WIDTH: int = 1000
HEIGHT: int = 900
NUM_SQUARES: int = 20
FPS: int = 60
MIN_SIZE: int = 30
MAX_SIZE: int = 80
K: int = 150
SPEED: int = 100

# Fleeing & Wander behavior constants
FLEE_RADIUS_MULTIPLIER: float = 3.5
FLEE_FORCE_WEIGHT: float = 0.2
WANDER_CHANCE: float = 0.1
WANDER_ANGLE_RANGE: int = 10

# Lifespan constants (in seconds)
MIN_LIFESPAN: float = 30.0
MAX_LIFESPAN: float = 60.0

# Fade duration at end of life (seconds)
FADE_DURATION: float = 2.0


class Square:
    def __init__(self, size: int = 30) -> None:
        self.size: int = size
        # Spawn fully within bounds
        self.x: float = float(random.randint(0, WIDTH - size))
        self.y: float = float(random.randint(0, HEIGHT - size))
        self.vx: float = random.choice([-1, 1]) * (K / self.size) * (SPEED / 100.0)
        self.vy: float = random.choice([-1, 1]) * (K / self.size) * (SPEED / 100.0)
        self.color: Tuple[int, int, int] = (
            random.randint(50, 255),
            random.randint(50, 255),
            random.randint(50, 255),
        )
        # Lifespan
        self.lifespan: float = random.uniform(MIN_LIFESPAN, MAX_LIFESPAN)
        self.age: float = 0.0
        self.alive: bool = True

    def rect(self) -> pygame.Rect:
        return pygame.Rect(int(self.x), int(self.y), self.size, self.size)

    def get_center(self) -> Tuple[float, float]:
        return (self.x + self.size / 2, self.y + self.size / 2)

    def get_alpha(self) -> int:
        """Return 0-255 alpha based on age. Fades in at birth, fades out before death."""
        # Fade in over first FADE_DURATION seconds
        if self.age < FADE_DURATION:
            return int(255 * (self.age / FADE_DURATION))
        # Fade out over last FADE_DURATION seconds
        time_left = self.lifespan - self.age
        if time_left < FADE_DURATION:
            return int(255 * max(0, time_left / FADE_DURATION))
        return 255

    def apply_wander(self) -> None:
        if random.random() < WANDER_CHANCE:
            angle = math.atan2(self.vy, self.vx)
            jitter = math.radians(random.uniform(-WANDER_ANGLE_RANGE, WANDER_ANGLE_RANGE))
            angle += jitter
            speed = math.sqrt(self.vx**2 + self.vy**2)
            self.vx = speed * math.cos(angle)
            self.vy = speed * math.sin(angle)

    def calculate_flee_force(self, larger_squares: List['Square']) -> Tuple[float, float]:
        flee_vx: float = 0.0
        flee_vy: float = 0.0
        for other in larger_squares:
            if other is self:
                continue
            dx = other.x + other.size / 2 - (self.x + self.size / 2)
            dy = other.y + other.size / 2 - (self.y + self.size / 2)
            dist_squared = dx**2 + dy**2
            threat_radius = FLEE_RADIUS_MULTIPLIER * other.size
            if dist_squared < threat_radius**2:
                if dist_squared > 0:
                    dist = math.sqrt(dist_squared)
                    flee_vx -= (dx / dist)
                    flee_vy -= (dy / dist)
        flee_magnitude = math.sqrt(flee_vx**2 + flee_vy**2)
        if flee_magnitude > 0:
            flee_vx = (flee_vx / flee_magnitude) * 2
            flee_vy = (flee_vy / flee_magnitude) * 2
        return flee_vx, flee_vy

    def update(self, dt: float, all_squares: Optional[List['Square']] = None) -> None:
        # Age the square
        self.age += dt
        if self.age >= self.lifespan:
            self.alive = False
            return

        self.apply_wander()

        if all_squares:
            larger_squares = [s for s in all_squares if s.size > self.size]
            if larger_squares:
                flee_vx, flee_vy = self.calculate_flee_force(larger_squares)
                self.vx = 0.8 * self.vx + FLEE_FORCE_WEIGHT * flee_vx
                self.vy = 0.8 * self.vy + FLEE_FORCE_WEIGHT * flee_vy

        self.x += self.vx * dt * 60
        self.y += self.vy * dt * 60

        # Left wall
        if self.x < 0:
            self.x = 0
            self.vx = abs(self.vx)
        # Right wall
        elif self.x + self.size > WIDTH:
            self.x = WIDTH - self.size
            self.vx = -abs(self.vx)

        # Top wall
        if self.y < 0:
            self.y = 0
            self.vy = abs(self.vy)
        # Bottom wall
        elif self.y + self.size > HEIGHT:
            self.y = HEIGHT - self.size
            self.vy = -abs(self.vy)


def draw_square_with_alpha(screen: pygame.Surface, square: Square, surface_cache: Dict[Tuple[int, Tuple[int, int, int]], pygame.Surface]) -> None:
    """Draw a square with its current alpha value using a cached surface."""
    alpha: int = square.get_alpha()
    key: Tuple[int, Tuple[int, int, int]] = (square.size, square.color)

    if key not in surface_cache:
        surf = pygame.Surface((square.size, square.size), pygame.SRCALPHA)
        surface_cache[key] = surf

    surf = surface_cache[key]
    r, g, b = square.color
    surf.fill((r, g, b, alpha))
    screen.blit(surf, (int(square.x), int(square.y)))


def main() -> None:
    pygame.init()
    screen: pygame.Surface = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Animated Squares — Lifespan & Rebirth")
    clock: pygame.time.Clock = pygame.time.Clock()
    font: pygame.font.Font = pygame.font.SysFont(None, 20)

    squares: List[Square] = [Square(size=random.randint(MIN_SIZE, MAX_SIZE)) for _ in range(NUM_SQUARES)]
    surface_cache: Dict[Tuple[int, Tuple[int, int, int]], pygame.Surface] = {}

    running: bool = True
    while running:
        dt: float = clock.tick(FPS) / 1000.0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

        # Update and cull dead squares, spawn replacements
        for s in squares:
            s.update(dt, squares)

        dead_count: int = sum(1 for s in squares if not s.alive)
        squares = [s for s in squares if s.alive]
        for _ in range(dead_count):
            squares.append(Square(size=random.randint(MIN_SIZE, MAX_SIZE)))

        # Draw
        screen.fill((15, 15, 20))

        for s in squares:
            draw_square_with_alpha(screen, s, surface_cache)

        # HUD
        info: pygame.Surface = font.render(
            f"Squares: {len(squares)}   |   Press ESC to quit",
            True, (200, 200, 200)
        )
        screen.blit(info, (10, HEIGHT - 24))

        pygame.display.flip()

    pygame.quit()
    sys.exit(0)


if __name__ == "__main__":
    main()