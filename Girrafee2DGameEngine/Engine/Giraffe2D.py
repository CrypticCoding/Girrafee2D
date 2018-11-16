import contextlib
import math
from test.test_turtle import Vec2D

with contextlib.redirect_stdout(None):
    import pygame
    import pygame.gfxdraw
    from pygame.locals import *
    
    

print("please Visit www.girrafee2d.com for more")


class App():
    def __init__(self):
        pygame.init()
    
    def RenderWindow(self, width, height):
        global gameDisplay
        gameDisplay = pygame.display.set_mode((width, height))
        icon = pygame.image.load('icon.png')
        pygame.display.set_icon(icon)

        
    def Update(self):
        pygame.display.update()

        
    def FPS(self, amount):
        clock = pygame.time.Clock()
        clock.tick(amount)

        
    def SetTitle(self, title):
        pygame.display.set_caption(title)

        
    def Fill(self, color):
        gameDisplay.fill(color)

        
    def get_display(self):
        return gameDisplay

    def SetIcon(self, path):
        myIcon = pygame.image.load(path)
        pygame.display.set_icon(myIcon)
    def quit(self):
        pygame.quit()
        quit()
        
class Event():
    def __init__(self):
        pygame.init()
        self.close = False
    
        for event in pygame.event.get():
            if event.type is pygame.QUIT:
                self.close = True
    
    
    
            
class Sprite(pygame.sprite.Sprite):
    def  __init__(self):
        pygame.init()
        pygame.sprite.Sprite().__init__(self)
    
    def DrawRect(self, color, sizeX, sizeY, posX, posY):
        self.color = color
        self.sizeX = sizeX
        self.sizeY = sizeY
        self.posX = posX
        self.posY = posY
        pygame.draw.rect(App.get_display(self), self.color, [self.posX, self.posY, self.sizeX, self.sizeY])
    def getPosX(self):
        return self.posX
    def LookAtMouse(self, spriteToRotate):
        x,y = pygame.mouse.get_pos()
        rel_x = x - self.posX
        rel_y = y - self.posY
        angle = (180 / math.pi) * math.atan2(rel_y, rel_x)
        spriteToRotate = pygame.transform.rotate(App.get_display(self), angle)
    def LoadImage(self, path):
        self.image = pygame.image.load(path).convert_alpha()
        self.rect = image.get_rect()
    def PlaceImage(self, x, y):
        self.x = x
        self.y = y
        self.image.blit(App.get_display(self),self.x,self.y)
        
    
        

class Keyboard():
    
    def __init__(self):
        self.moveRight = False
        self.moveLeft = False
        self.moveUp = False
        self.moveDown = False
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.moveLeft = True
        if keys[pygame.K_RIGHT]:
            self.moveRight = True
        if keys[pygame.K_UP]:
            self.moveUp = True
        if keys[pygame.K_DOWN]:
            self.moveDown = True
    def CheckKey(self, key):
        pass
            
            
                    
    
             


     


    


