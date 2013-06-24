import pygame
from util.enum import *
from util.pixel import *

screen = pygame.display.get_surface()

def pixel(col, pos):
    screen = pygame.display.get_surface()
    screen.fill(col, (pos, (1,1)))

def sphere(col, pos, rad):
    x, y = pos
    rect = pygame.Rect(x-rad, y-rad, rad*2, rad*2)
    for i in range(-rad, rad):
        for j in range(-rad, rad):
            if i*i + j*j < rad*rad:
                pixel(col, (x+i, y+j))
    pygame.dirty_rects.append(rect)
    return rect

def ptail(pos1, pos2=None):
    screen = pygame.display.get_surface()
    rect = pygame.draw.line(screen, TAIL, pos1, pos2)
    """
    x = min(pos1[0], pos2[0]) - 1
    y = min(pos1[1], pos2[1]) - 1
    xd = max(3, abs(pos1[0] - pos2[0]))
    yd = max(3, abs(pos1[1] - pos2[1]))
    rect = pygame.Rect(x, y, xd, yd)
    for i in range(x, x+xd):
        for j in range(y, y+yd):
            pixel(TAIL, (i,j))
    """
    pygame.dirty_rects.append(rect)
    return rect

def phead(pos):
    rect = sphere(RED, pos, HEAD_RADIUS)
    sphere(ORANGE, pos, 2*HEAD_RADIUS/3)
    sphere(YELLOW, pos, HEAD_RADIUS/3)
    return rect

def psnack(pos):
    rect = sphere(SNACK, pos, SNACK_RADIUS)
    sphere(WHITE, pos, SNACK_RADIUS/2)
    return rect

def clear(rect):
    screen = pygame.display.get_surface()
    screen.fill(BACKGROUND, rect)
    pygame.dirty_rects.append(rect)

def square(rect, col=WHITE, thickness=1):
    for i in range(rect.width):
        for k in range(thickness):
            pixel(col, (rect.left + i, rect.top+k))
            pixel(col, (rect.left + i, rect.bottom-1-k))

    for i in range(rect.height):
        for k in range(thickness):
            pixel(col, (rect.left+k, rect.top + i))
            pixel(col, (rect.right-1-k, rect.top + i))
    pygame.dirty_rects.append(rect)

def num(n, size, pos):
    x, y = pos
    pixelart = getpixels(n)
    for i, row in enumerate(pixelart):
        for j, b in enumerate(row):
            if b:
                for k in range(size):
                    for k2 in range(size):
                        pixel(BLUE, (x+j*size+k, y+i*size+k2))

    rect = pygame.Rect(x, y, size*len(pixelart[0]), size*len(pixelart))
    pygame.dirty_rects.append(rect)
    return rect

def writen(ns, size, pos):
    x, y = pos
    ns = str(ns)
    for i, n in enumerate(ns):
        num(n, size, (x+i*(size*3*1.2), y))
    rect = pygame.Rect(x, y, len(ns)*3*size*1.2, 5*size)
    return rect