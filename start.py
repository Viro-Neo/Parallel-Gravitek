import pygame
import pygame_menu
import Theme
import platformm
import player
import sys
from pygame.locals import *

import globals as g
from event import event_handler

displaySurface = pygame.display.set_mode((g.WIDTH, g.HEIGHT))
pygame.display.set_caption("Parallel gravitek")

def main():
    pygame.init()
    start_menu()

def start_menu():
    mainmenu = pygame_menu.Menu('Welcome', 1000, 539, theme=Theme.mytheme)
    mainmenu.add.text_input('Name: ', default='Type username', maxchar=20)
    mainmenu.add.button('Play', start_game)
    mainmenu.add.button('Quit', pygame_menu.events.EXIT)
    mainmenu.mainloop(displaySurface)

def start_game():
    FramesPerSecond = pygame.time.Clock()
    PT1 = platformm.platform()#0, 0, 980, 50, (980, 255, 255))
    P1 = player.Player()

    background_image = pygame.image.load("img/background/bg.jpg").convert_alpha()
    background = pygame.sprite.Sprite()
    background.image = background_image
    background.rect = background_image.get_rect()

    sprite_image = pygame.image.load("img/character/static_blue.png").convert_alpha()
    sprite = pygame.sprite.Sprite()
    sprite.image = sprite_image
    sprite.rect = sprite_image.get_rect()
    sprite.rect.x = 100
    sprite.rect.y = 100
    platform_image = pygame.image.load("img/Platform/only_road.png").convert_alpha()
    platform = pygame.sprite.Sprite()
    platform.image = platform_image
    platform.rect = platform_image.get_rect()
    platform.rect.x = -10
    platform.rect.y = 980
    platform_top_image = pygame.image.load("img/Platform/only_road_top.png").convert_alpha()
    platform_top = pygame.sprite.Sprite()
    platform_top.image = platform_top_image
    platform_top.rect = platform_top_image.get_rect()
    platform_top.rect.x = -10
    platform_top.rect.y = 0
    pygame.mixer.music.load("img/Music/menu.mp3")
    pygame.mixer.music.play()
    obstacle_image = pygame.image.load("img/obstacles/obstacle_1.png").convert_alpha()
    obstacle = pygame.sprite.Sprite()
    obstacle.image = obstacle_image
    obstacle.rect = obstacle_image.get_rect()
    obstacle.rect.x = -6
    obstacle.rect.y = 901

    PT1 = platformm.platform()#0, 100, 980, 980, (255, 255, 255))
    P1 = player.Player()
    all_sprites = pygame.sprite.Group()
    all_sprites.add(background)
    #all_sprites.add(P1)
    all_sprites.add(platform)
    all_sprites.add(platform_top)
    all_sprites.add(obstacle)
    all_sprites.add(sprite)
    #all_sprites.add(PT1)


    platforms = pygame.sprite.Group()
    platforms.add(PT1)
    platforms.add(sprite)
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    P1.jump(platforms, event)
        
        P1.update(platforms)
        P1.update_gravity()
        P1.move()
        sprite.rect.x = P1.pos.x
        sprite.rect.y = P1.pos.y
        displaySurface.fill((0,0,0))
        all_sprites.draw(displaySurface)
        pygame.display.update()
        FramesPerSecond.tick(g.FPS)
