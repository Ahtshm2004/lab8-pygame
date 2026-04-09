import sys
import random
import pygame


WIDTH, HEIGHT = 1000, 900
NUM_SQUARES = 20
FPS = 60
MIN_SIZE = 30
MAX_SIZE = 80
K = 150
SPEED = 100


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

	def update(self, dt):
		# dt: seconds elapsed since last frame
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
			s.update(dt)

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

