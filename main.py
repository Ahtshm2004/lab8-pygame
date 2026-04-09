import sys
import random
import math
import pygame


WIDTH, HEIGHT = 1000, 900
NUM_SQUARES = 20
FPS = 60
MIN_SIZE = 30
MAX_SIZE = 80
K = 150
SPEED = 100

# Fleeing & Wander behavior constants
FLEE_RADIUS_MULTIPLIER = 3.5  # Threat detected at 3.5x the larger square's size
FLEE_FORCE_WEIGHT = 0.2  # 20% flee force, 80% current velocity
WANDER_CHANCE = 0.1  # 10% chance per frame to apply jitter
WANDER_ANGLE_RANGE = 10  # ±10 degrees for jitter


class Square:
	def __init__(self, size=30):
		self.size = size
		self.x = random.randint(0, WIDTH - size)
		self.y = random.randint(0, HEIGHT - size)
		# velocity scaled by size (smaller = faster) and SPEED constant
		self.vx = random.choice([-1, 1]) * (K / self.size) * (SPEED / 100.0)
		self.vy = random.choice([-1, 1]) * (K / self.size) * (SPEED / 100.0)
		self.color = (
			random.randint(50, 255),
			random.randint(50, 255),
			random.randint(50, 255),
		)

	def rect(self):
		return pygame.Rect(int(self.x), int(self.y), self.size, self.size)

	def get_center(self):
		"""Return the center position of the square"""
		return (self.x + self.size / 2, self.y + self.size / 2)

	def apply_wander(self):
		"""Apply random jitter to velocity (±5° to ±10° rotation)"""
		if random.random() < WANDER_CHANCE:
			# Convert velocity to angle
			angle = math.atan2(self.vy, self.vx)
			# Add random jitter
			jitter = math.radians(random.uniform(-WANDER_ANGLE_RANGE, WANDER_ANGLE_RANGE))
			angle += jitter
			# Preserve speed magnitude
			speed = math.sqrt(self.vx**2 + self.vy**2)
			self.vx = speed * math.cos(angle)
			self.vy = speed * math.sin(angle)

	def calculate_flee_force(self, larger_squares):
		"""Calculate flee force from nearby larger squares"""
		flee_vx = 0
		flee_vy = 0
		
		for other in larger_squares:
			if other is self:
				continue
			
			# Calculate distance squared to avoid expensive sqrt
			dx = other.x + other.size / 2 - (self.x + self.size / 2)
			dy = other.y + other.size / 2 - (self.y + self.size / 2)
			dist_squared = dx**2 + dy**2
			
			# Check if threat is within awareness radius
			threat_radius = FLEE_RADIUS_MULTIPLIER * other.size
			if dist_squared < threat_radius**2:
				# Calculate flee direction (away from threat)
				if dist_squared > 0:  # Avoid division by zero
					dist = math.sqrt(dist_squared)
					flee_vx -= (dx / dist)  # Normalize and negate (away from threat)
					flee_vy -= (dy / dist)
		
		# Normalize flee force if it exists
		flee_magnitude = math.sqrt(flee_vx**2 + flee_vy**2)
		if flee_magnitude > 0:
			flee_vx = (flee_vx / flee_magnitude) * 2  # Scale for effect
			flee_vy = (flee_vy / flee_magnitude) * 2
		
		return flee_vx, flee_vy

	def update(self, dt, all_squares=None):
		"""Update square position with fleeing and wander behavior"""
		# Apply wander (random jitter)
		self.apply_wander()
		
		# Apply fleeing if this square is small and other squares exist
		if all_squares:
			larger_squares = [s for s in all_squares if s.size > self.size]
			if larger_squares:
				flee_vx, flee_vy = self.calculate_flee_force(larger_squares)
				# Blend: 80% current velocity + 20% flee force
				self.vx = 0.8 * self.vx + FLEE_FORCE_WEIGHT * flee_vx
				self.vy = 0.8 * self.vy + FLEE_FORCE_WEIGHT * flee_vy
		
		# Update position based on velocity
		self.x += self.vx * dt * 60
		self.y += self.vy * dt * 60

		# bounce off walls
		if self.x < 0:
			self.x = 0
			self.vx *= -1
		elif self.x + self.size > WIDTH:
			self.x = WIDTH - self.size
			self.vx *= -1

		if self.y < 0:
			self.y = 0
			self.vy *= -1
		elif self.y + self.size > HEIGHT:
			self.y = HEIGHT - self.size
			self.vy *= -1


def main():
	pygame.init()
	screen = pygame.display.set_mode((WIDTH, HEIGHT))
	pygame.display.set_caption("Animated Squares with Inertia-Based Fleeing")
	clock = pygame.time.Clock()

	squares = [Square(size=random.randint(MIN_SIZE, MAX_SIZE)) for _ in range(NUM_SQUARES)]

	running = True
	while running:
		dt = clock.tick(FPS) / 1000.0

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					running = False

		for s in squares:
			s.update(dt, squares)

		screen.fill((15, 15, 20))

		for s in squares:
			pygame.draw.rect(screen, s.color, s.rect())

		# optional overlay text
		font = pygame.font.SysFont(None, 20)
		info = font.render("Press ESC or close window to quit", True, (200, 200, 200))
		screen.blit(info, (10, HEIGHT - 24))

		pygame.display.flip()

	pygame.quit()
	sys.exit(0)


if __name__ == "__main__":
	main()

