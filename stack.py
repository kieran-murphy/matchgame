import pygame, sys
from pygame.locals import *
import random
import time
w, h = 500, 600
size = (w, h)
GRAY = (150, 150, 150)
DISPLAY=pygame.display.set_mode(size,0,32)

doggochoices = [1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8]

def box(x, y):
    type = str(doggochoices.pop(random.randint(0,len(doggochoices) - 1)))
    randomimgurl = 'doggossquared/' + type + '.png'

    img = pygame.image.load(randomimgurl).convert()
    img = pygame.transform.scale(img, (80, 80))
    rect = img.get_rect()
    rect.center = x, y
    
    pygame.draw.rect(DISPLAY, GRAY, rect, 1)
    DISPLAY.blit(img, rect)


def main():
    pygame.init()

    
    WHITE=(255,255,255)
    BLUE=(0,0,255)

    DISPLAY.fill(WHITE)

    
    box_y = 100
    for i in range(4):
        box_x = 100
        for j in range(4):
            box(box_x, box_y)
            box_x += 100
        box_y += 100
    
    
    while True:
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()

main()