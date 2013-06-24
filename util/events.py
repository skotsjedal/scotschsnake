import pygame, sys
from pygame.locals import *
from util.enum import *

def input(events):
	game = pygame.game
	for event in events:
		if event.type == QUIT:
			sys.exit(0)
		if event.type == KEYDOWN:
			if event.key == K_ESCAPE:
				sys.exit(0)
			game.pressed(event.key)
		if event.type == USEREVENT:
			if event.code == OUTOFAREA or event.code == TAILCOLLIDE:
				game.active = False
				print "YOU ARE DEAD GG"
		else:
			None
			#print event