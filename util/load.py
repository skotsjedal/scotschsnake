import pygame, os

data_dir = "data"

def image(name):
	global data_dir
	img = pygame.image.load(os.path.join(data_dir,name))

	img = img.convert()
	return img, img.get_rect()