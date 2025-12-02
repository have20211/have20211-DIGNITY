import pygame 
from button import Button
from settings import *
pygame.init()







class Level:
	def __init__(self):
		self.screen = pygame.display.get_surface()

		self.main_text = '1234'
		self.history = []




		self.last_key = {}
		self.symbols = {pygame.K_1:1,pygame.K_2:2,pygame.K_3:3,pygame.K_4:4,pygame.K_5:5,pygame.K_6:6,pygame.K_7:7,pygame.K_8:8,pygame.K_9:9,pygame.K_0:0, pygame.K_SLASH:'/', pygame.K_MINUS:'-', pygame.K_EQUALS:'='}
		self.symbols_shift = {pygame.K_EQUALS:'+', pygame.K_8:'*'} #сука пидорасы кто это придумал

	def draw_text(self, txt):
		font_main = pygame.font.Font(None, 58)
		text_main = font_main.render(txt, True, COLOR_NUM_MAIN)
		rect_main = text_main.get_rect(topright=(345,70))
		font_history = pygame.font.Font(None, 24)
		text_history = font_history.render(' '.join(map(str, self.history)), True, COLOR_NUM_HISTORY)
		rect_history = text_history.get_rect(topright=(345,27))
		self.screen.blit(text_main, (rect_main))
		self.screen.blit(text_history, (rect_history))

	def get_keyboard(self):
		key = pygame.key.get_pressed()
		for i in self.symbols:
			if key[i]:
				if not self.last_key.get(i, False):
					return self.symbols[i]
			self.last_key[i] = key[i]

		for i in self.symbols_shift:
			if key[i]:
				if not self.last_key.get(i, False):
					mods = pygame.key.get_mods()
					if mods & pygame.KMOD_SHIFT:
						return self.symbols_shift[i]
			self.last_key[i] = key[i]
		





	def get_functions(self):
		key = pygame.key.get_pressed()

		if key[pygame.K_SLASH]:
			if not self.last_key.get(pygame.K_SLASH, False):
					self.history.append(self.main_text)
					self.history.append('/')
					self.main_text = ''
		self.last_key[pygame.K_SLASH] = key[pygame.K_SLASH]


	def main(self):
		print(self.get_keyboard())



	def update(self):
		print(self.get_keyboard())
		self.main()
		self.draw_text(self.main_text)
