import pygame
from pygame.locals import *
import globals as g

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((30, 30))
        self.image.fill((128, 255, 40))
        self.rect = self.image.get_rect(center = (10,420))

        self.pos = g.vect((10, 226))
        self.vel = g.vect(0, 0)
        self.acc = g.vect(0, 0)

        self.gravity = 1

    def move(self):
        self.acc = g.vect(0, self.gravity * 0.5)

        pressed_keys = pygame.key.get_pressed()

        if pressed_keys[K_LEFT]:
            self.acc.x = -g.ACC
        if pressed_keys[K_RIGHT]:
            self.acc.x = g.ACC

        self.acc.x += self.vel.x * g.FRIC
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc

        if self.pos.x > g.WIDTH:
            self.pos.x = 0
        if self.pos.x < 0:
            self.pos.x = g.WIDTH
    
        self.rect.midbottom = self.pos
    
    def update_gravity(self):
        if (self.pos.y > 225):
            self.gravity = 1
        else:
            self.gravity = -1
    
    def jump(self, platforms, event):
        hits = pygame.sprite.spritecollide(self, platforms, False)
        if hits:
            self.vel.y = -10 * self.gravity
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                self.vel.y = -10 * self.gravity

    def update(self, platforms):
        hits = pygame.sprite.spritecollide(self, platforms, False)
        if self.vel.y > 0:
            if hits:
                self.pos.y = hits[0].rect.top + 1
                self.vel.y = 0

    #def sprite_managment(self, sprite_group=None):
    #    character_sprite = pygame.image.load("img/character/static_red.png")
    #    create_char_sprite = pygame.sprite.Sprite()
    #    create_char_sprite.image = character_sprite
    #    create_char_sprite.rect = create_char_sprite.image.get_rect()
    #    create_char_sprite.rect.x = 100
    #    create_char_sprite.rect.y = 100
    #    if sprite_group is None:
    #        sprite_group = pygame.sprite.Group()
    #    sprite_group.add(create_char_sprite)
