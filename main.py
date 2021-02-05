import pygame
from pygame.locals import *
import random

doggochoices = [1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8]

class Box:
    def __init__(self, box_x, box_y, id):
        self.box_x = box_x
        self.box_y = box_y
        self.id = id
        self.type = str(doggochoices.pop(random.randint(0,len(doggochoices) - 1)))
        self.randomimgurl = 'doggossquared/' + self.type + '.png'
        self.img = pygame.image.load(self.randomimgurl).convert()
        self.img = pygame.transform.scale(self.img, (80, 80))
        self.rect = self.img.get_rect()
        self.draw()
        self.render()
    
    def render(self):
        self.rect.center = self.box_x, self.box_y
        
        #pygame.draw.rect(DISPLAY, GRAY, rect, 1)
        
    def draw(self):
        App.screen.blit(self.img, self.rect)

    def hide(self):
        self.img = pygame.image.load(doggossquared/question.png).convert()
        self.img = pygame.transform.scale(self.img, (80, 80))
        self.rect = self.img.get_rect()

    


class App:
    """Create a single-window app with multiple scenes."""
    def __init__(self):
        """Initialize pygame and the application."""
        pygame.init()
        #flags = RESIZABLE
        App.screen = pygame.display.set_mode((500, 600))
        App.b1 = Box(100,100,1)
        App.b2 = Box(200,100,2)
        App.b3 = Box(300,100,3)
        App.b4 = Box(400,100,4)
        App.b5 = Box(100,200,5)
        App.b6 = Box(200,200,6)
        App.b7 = Box(300,200,7)
        App.b8 = Box(400,200,8)
        App.b9 = Box(100,300,9)
        App.b10 = Box(200,300,10)
        App.b11 = Box(300,300,11)
        App.b12 = Box(400,300,12)
        App.b13 = Box(100,400,13)
        App.b14 = Box(200,400,14)
        App.b15 = Box(300,400,15)
        App.b16 = Box(400,400,16)
        
        App.running = True
        
    def run(self):
        """Run the main event loop."""
        while App.running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    App.running = False
                elif event.type == MOUSEBUTTONDOWN:
                    if App.b1.collidepoint(event.pos):
                        moving = True


                        
            WHITE=(255,255,255)
            App.screen.fill(WHITE)
            
            App.b1.draw()
            App.b2.draw()
            App.b3.draw()
            App.b4.draw()
            App.b5.draw()
            App.b6.draw()
            App.b7.draw()
            App.b8.draw()
            App.b9.draw()
            App.b10.draw()
            App.b11.draw()
            App.b12.draw()
            App.b13.draw()
            App.b14.draw()
            App.b15.draw()
            App.b16.draw()
            pygame.display.update()
        pygame.quit()




if __name__ == '__main__':
    App().run()