import pygame
from pygame.locals import *
pygame.init()

# CONST VARIABLES
speed = [2, 2]

screen = pygame.display.set_mode([1024, 512])

class Player(pygame.sprite.Sprite): 
    def __init__(self):
        print("a")

dinoGame = True
while dinoGame: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            dinoGame = False


    screen.fill((229, 255, 204))
    pygame.display.flip()