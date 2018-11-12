import pygame
import os
import sys
import datetime


class App():
    pygame.init()
    def RenderWindow(self, width, height):
        gameDisplay = pygame.display.set_mode((width, height))
    def run(self):
        pygame.display.update()
        pygame.quit()
        quit()
    def FPS(self, amount):
        clock = pygame.time.Clock()
        clock.tick(amount)
    def SetTitle(self, title):
        pygame.display.set_caption(title)
   
       
class Event():
    def type(self, myEvent):
        if myEvent == "QUIT":
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

     
class Sprite():
    def __init__(self, path, name):
        self.path = path
        self.name = name   

    def DrawRect(self):
        pass
    def DrawCircle(self):
        pass
    def DrawTriangle(self):
        pass
    def LoadTilemap(self):
        pass

     


    


