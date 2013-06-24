import pygame
from util import load
from pygame.locals import *
from util.enum import *

class Head(pygame.sprite.Sprite):

	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image, self.rect = load.image("head.jpg")
		self.rect.topleft = 100, 100
		self.area = pygame.display.get_surface().get_rect()

	def update(self):

		pygame.dirty_rects.append(self.rect)
		pygame.game.screen.fill(BACKGROUND, self.rect)

		direction = (pygame.game.x_v, pygame.game.y_v)

		if self.rect.left < self.area.left or \
			self.rect.right > self.area.right or \
			self.rect.top < self.area.top or \
			self.rect.bottom > self.area.bottom:
			print "u died"
			deadevent = pygame.event.Event(USEREVENT, code=OUTOFAREA)
			pygame.event.post(deadevent)

		newpos = self.rect.move(direction)
		self.rect = newpos

		pygame.dirty_rects.append(self.rect)

class Tail(pygame.sprite.Sprite):

	def __init__():
		None
