import pygame

lastprint = 0

def cprint(text):
	global lastprint
	if pygame.time.get_ticks() - lastprint > 1500:
		lastprint = pygame.time.get_ticks()
		print text

def draw_text():
	fonto = pygame.font.Font(None, 26)
	textt = fonto.render("Status", 1, (200, 200, 200))
	pygame.dirty_rects.append(textt.get_rect())
	screen.blit(textt, (100,20))