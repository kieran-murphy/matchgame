import pygame
from pygame.locals import *
import random
import time

doggochoices = [1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8]
choice = ['1']

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
        
        self.hide()
        self.render()
    
    def render(self):
        self.rect.center = self.box_x, self.box_y
        
        
    def draw(self):
        App.screen.blit(self.img, self.rect)
        

    def hide(self):
        self.img = pygame.image.load('doggossquared/question.png').convert()
        self.img = pygame.transform.scale(self.img, (80, 80))
        self.rect = self.img.get_rect()
        self.render()
    
    def reveal(self):
        global choice
        if self.type == choice[0]:
            print('match!')
            self.img = pygame.image.load(self.randomimgurl).convert()
            self.img = pygame.transform.scale(self.img, (80, 80))
            self.rect = self.img.get_rect()
            self.render()
        else:
            pass
                
        
        
    


class App:
    """Create a single-window app with multiple scenes."""
    def __init__(self):
        """Initialize pygame and the application."""
        pygame.init()
        #flags = RESIZABLE
        App.screen = pygame.display.set_mode((500, 600))
        App.boxes = pygame.sprite.Group()
        App.b1 = Box(100,100,1)
        App.boxes.add(App.b1)
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
        
        '''
        box_y = 100
        num = 1
        boxes = []
        for i in range(4):
            box_x = 100
            for j in range(4):
                box = (box_x, box_y, num)
                boxes.append(box)
                box_x += 100
                num += 1
            box_y += 100
        
        for i in boxes:
            Box(i)
        '''
        
        App.running = True

      
    def run(self):
        """Run the main event loop."""
        while App.running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    App.running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # Set the x, y postions of the mouse click
                    x, y = event.pos
                    if App.b1.rect.collidepoint(x, y):
                        App.b1.reveal()
                    elif App.b2.rect.collidepoint(x, y):
                        App.b2.reveal()
                    elif App.b3.rect.collidepoint(x, y):
                        App.b3.reveal()
                    elif App.b4.rect.collidepoint(x, y):
                        App.b4.reveal()
                    elif App.b5.rect.collidepoint(x, y):
                        App.b5.reveal()
                    elif App.b6.rect.collidepoint(x, y):
                        App.b6.reveal()
                    elif App.b7.rect.collidepoint(x, y):
                        App.b7.reveal()
                    elif App.b8.rect.collidepoint(x, y):
                        App.b8.reveal()
                    elif App.b9.rect.collidepoint(x, y):
                        App.b9.reveal()
                    elif App.b10.rect.collidepoint(x, y):
                        App.b10.reveal()
                    elif App.b11.rect.collidepoint(x, y):
                        App.b11.reveal()
                    elif App.b12.rect.collidepoint(x, y):
                        App.b12.reveal()
                    elif App.b13.rect.collidepoint(x, y):
                        App.b13.reveal()
                    elif App.b14.rect.collidepoint(x, y):
                        App.b14.reveal()
                    elif App.b15.rect.collidepoint(x, y):
                        App.b15.reveal()
                    elif App.b16.rect.collidepoint(x, y):
                        App.b16.reveal()

                        
            WHITE=(255,255,255)
            App.screen.fill(WHITE)
            
            App.boxes.draw()
            pygame.display.update()
        pygame.quit()




if __name__ == '__main__':
    App().run()