#!/usr/bin/python
import pygame, sys, os
from util import load, events, utils
from core import scsn
from pygame.locals import *
if not pygame.font: print 'Warning, fonts disabled'
else:
	pygame.font.init()
if not pygame.mixer: print 'Warning, sound disabled'

ss_name = "Scotsch Snake"
ss_version = 0.1

pygame.dirty_rects = []
pygame.init()

game = scsn.scsn()
pygame.game = game

pygame.display.set_mode((game.width, game.height))
pygame.display.set_caption(ss_name+" "+str(ss_version))
screen = pygame.display.get_surface()

game.start()

game.clock = pygame.time.Clock()
#sprite_h = pygame.sprite.RenderPlain(game.head)

while True:
	events.input(pygame.event.get())
	game.clock.tick(60)
	if game.active:
		game.tick()
		game.move()
	#utils.cprint(game.clock.get_fps())
	
	#sprite_h.draw(screen)
	#utils.draw_text()
	pygame.display.update(pygame.dirty_rects)
	pygame.dirty_rects = []
