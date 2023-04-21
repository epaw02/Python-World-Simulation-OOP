import pygame
from pygame.locals import *

class Buttons():
	def __init__(self, x, y, text, scr, clicked):
		self.x = x
		self.y = y
		self.text = text
		self.screen=scr
		self.white=(255,255,255)
		self.black=(0,0,0)
		self.button_color = (240,248,255)
		self.hover_color = (50, 225, 255)
		self.click_color = (50, 150, 255)
		self.text_color = (0,0,0)
		self.width = 200
		self.height = 50
		self.clicked=clicked

	def draw_button(self):
		action = False
		pos = pygame.mouse.get_pos() #getting mouse position
		font = pygame.font.SysFont(None, 30)
		button_rect = Rect(self.x, self.y, self.width, self.height) #create pygame Rect object for the button
		if button_rect.collidepoint(pos):
			if pygame.mouse.get_pressed()[0] == 1:
				self.clicked = True
				pygame.draw.rect(self.screen, self.click_color, button_rect)
			elif pygame.mouse.get_pressed()[0] == 0 and self.clicked == True:
				self.clicked = False
				action = True
			else:
				pygame.draw.rect(self.screen, self.hover_color, button_rect)
		else:
			pygame.draw.rect(self.screen, self.button_color, button_rect)
		
		text_img = font.render(self.text, True, self.text_color) #adding text to button
		text_len = text_img.get_width()
		self.screen.blit(text_img, (self.x + int(self.width / 2) - int(text_len / 2), self.y + 25))
		return action
