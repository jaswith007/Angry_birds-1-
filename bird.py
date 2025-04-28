import pygame 
import math 
import random

pygame.init()
class Bird:
    def __init__(self, x, y, radius, type):
        self.x = x
        self.y = y
        self.radius = radius
        self.type = type
        self.gravity = 1000
        self.velocityX = 0
        self.velocityY = 0
        if self.type == "red":
            self.image = pygame.image.load("images/red_bird.png")
        elif self.type == "blue":
            self.image = pygame.image.load("images/blue_bird.png")
        elif self.type == "yellow":
            self.image = pygame.image.load("images/yellow_bird.png")
        elif self.type == "black":
            self.image = pygame.image.load("images/black_bird.png") 
        self.image = pygame.transform.scale(self.image, (self.radius*2, self.radius*2))

    def bird_place(self, screen):
        screen.blit(self.image, (self.x, self.y))

def update_pos(self, x, y):
        self.x = x
        self.y = y