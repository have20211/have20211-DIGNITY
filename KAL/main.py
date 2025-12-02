import pygame, sys
from settings import *
from level import Level


class Calculator:
	def __init__(self):

		pygame.init()
		self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
		pygame.display.set_caption("Калькулятор")
		self.clock = pygame.time.Clock()
		self.level = Level()

	def run(self):
		while True:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()

				self.screen.fill("#222222")
				self.level.update()
				pygame.display.update()
				self.clock.tick(FPS)


if __name__ == "__main__":
	calculator = Calculator()
	calculator.run()