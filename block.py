import pygame
import random

ice1 = pygame.transform.scale(pygame.image.load("images/ice_block1.png"), (35, 35))
ice2 = pygame.transform.scale(pygame.image.load("images/ice_block2.png"), (35, 35))
wood1 = pygame.transform.scale(pygame.image.load("images/wooden_block1.png"), (35, 35))
wood2 = pygame.transform.scale(pygame.image.load("images/wooden_block2.png"), (35, 35))
stone1 = pygame.transform.scale(pygame.image.load("images/stone_block1.png"), (35, 35))
stone2 = pygame.transform.scale(pygame.image.load("images/stone_block2.png"), (35, 35))

class Block:
    def __init__(self, x, y, size, type):
        self.x = x
        self.y = y
        self.size = size
        self.type = type
        self.hp = 100
        if self.type == 1:
            self.image = ice1
        if self.type == 2:
            self.image = wood1
        if self.type == 3:
            self.image = stone1