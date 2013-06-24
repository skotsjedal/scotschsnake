import pygame, random, math
from util import load, utils
from core import sprites, gfx
from util.enum import *
from pygame.locals import *

speed = 3

class scsn():
    x = 100
    y = 100

    x_v = speed
    y_v = 0
    active = False
    tlen = 1

    width = 640
    height = 480

    head = None
    screen = None

    snacks = []
    
    def __init__(self):
        None

    def start(self):
        #self.head = sprites.Head()
        self.screen = pygame.display.get_surface()
        self.active = True
        self.currect = pygame.Rect(0,0,0,0)
        self.dispfpsr = pygame.Rect(0,0,0,0)

        self.disptail = (0,0,0,0)
        self.lastprint = 0
        
        self.tail = [pygame.Rect(self.x, self.y, 0, 0)]
        self.tailx = self.tail[-1].x
        self.taily = self.tail[-1].y

        self.area = pygame.display.get_surface().get_rect()

        statussize = 32
        self.area.inflate_ip(0, -statussize)
        self.area.move_ip(0, -statussize/2)
        self.status_area = Rect(self.area.left, self.area.bottom, self.area.width, statussize)
        gfx.square(self.status_area, col=BLUE)

        gfx.square(self.area, col=ORANGE, thickness=HEAD_RADIUS/2)

    def disptaillen(self):
        if len(self.tail) > self.lastprint:
            self.lastprint = len(self.tail)
            gfx.clear(self.disptail)
            self.disptail = gfx.writen(len(self.tail)/TAIL_PIECE_PER_SNACK, FONTSIZE, (self.status_area.x+5, self.status_area.y+4))

    def dispfps(self):
        gfx.clear(self.dispfpsr)
        self.dispfpsr = gfx.writen(int(self.clock.get_fps()), FONTSIZE, (self.status_area.right-5-FONTSIZE*3*3*1.2, self.status_area.y+4))

    def pressed(self, key):
        # Change Dir
        movement = [ord(c) for c in ['a', 's', 'd', 'w']] + [K_LEFT, K_RIGHT, K_DOWN, K_UP]
        if key in movement:
            self.x_v = self.y_v = 0
            
            if key == ord('a') or key == K_LEFT:
                self.x_v = -speed
            if key == ord('d') or key == K_RIGHT:
                self.x_v = speed
            if key == ord('s') or key == K_DOWN:
                self.y_v = speed
            if key == ord('w') or key == K_UP:
                self.y_v = -speed

        else:
            char = chr(key) if key >= ord('a') and key <= ord('z') else None
            print "Pressed", key, char

    def updatepos(self):
        self.x += self.x_v
        self.y += self.y_v
        if self.x + HEAD_RADIUS > self.area.right or \
            self.x - HEAD_RADIUS < self.area.left or \
            self.y + HEAD_RADIUS > self.area.bottom or \
            self.y - HEAD_RADIUS < self.area.top:
            deadevent = pygame.event.Event(USEREVENT, code=OUTOFAREA)
            pygame.event.post(deadevent)

    def move(self):
        #self.head.update()
        self.movephead()
        colid = self.currect.collidelist(self.snacks)
        if colid >= 0:
            snack = self.snacks[colid]
            self.snacks.remove(snack)
            gfx.clear(snack)
            self.tlen += 1
        tailcolid = self.currect.collidelist(self.tail)
        if tailcolid >= 0 and tailcolid < len(self.tail)-TAILCOLLERR:
            deadevent = pygame.event.Event(USEREVENT, code=TAILCOLLIDE)
            pygame.event.post(deadevent)
            #print "DEAD"
        self.updatetail()
        self.disptaillen()
        self.dispfps()

    def updatetail(self):
        x = self.x #- HEAD_RADIUS*self.x_v/speed
        y = self.y #- HEAD_RADIUS*self.y_v/speed
        ox = self.tailx
        oy = self.taily
        xd = abs(ox - x)
        yd = abs(oy - y)
        dist = math.sqrt(xd*xd+yd*yd)
        #print dist
        if dist > TAIL_PIECE_LEN:
            self.tailx = x
            self.taily = y
            newt = gfx.ptail((ox, oy), (x , y))
            self.tail.append(newt)
        if len(self.tail) > self.tlen * TAIL_PIECE_PER_SNACK:
            last = self.tail.pop(0)
            gfx.clear(last)

    def movephead(self):
        if self.currect:
            gfx.clear(self.currect)

        self.updatepos()
        self.currect = gfx.phead((self.x, self.y))
    
    def spawnsnack(self):
        x = HEAD_RADIUS/2 + SNACK_RADIUS/2 + random.random()*(self.area.width-HEAD_RADIUS-SNACK_RADIUS)
        y = HEAD_RADIUS/2 + SNACK_RADIUS/2 + random.random()*(self.area.height-HEAD_RADIUS-SNACK_RADIUS)
        srect = gfx.psnack((x, y))
        self.snacks.append(srect)
        #print "creating snack at", srect

    def tick(self):
        if len(self.snacks) < MAX_SNACKS:
            self.spawnsnack()
