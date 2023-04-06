import pygame
from pygame.locals import *
import globals as g

class platform(pygame.sprite.Sprite):
    def __init__(self):#, x, y, width, height, color):
        super().__init__()
        self.image = pygame.Surface((g.WIDTH, 150))
        self.image.fill((255,0,0))
        self.rect = self.image.get_rect(center = (g.WIDTH/2, g.HEIGHT - 10))
        rotation = pygame.transform.rotate(self.image, 45)
        self.image = rotation
        #self.surf = pygame.Surface((width, height))
        #self.surf.fill(color)
        #self.rect = self.surf.get_rect(center = (x, y))
        #rotation = pygame.transform.rotate(self.surf, 45)
        #self.surf = rotation
