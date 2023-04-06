import pygame
from pygame.locals import *
import sys


def event_handler(P1, platforms, event):
    if event.type == QUIT:
        pygame.quit()
        sys.exit()
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_SPACE:
            P1.jump(platforms)
        if event.key == pygame.K_ESCAPE:
            pygame.quit()
            sys.exit()
