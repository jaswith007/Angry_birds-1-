import pygame
import sys

class Catapult:
    def __init__(self, x, y, image):
        self.x = x
        self.y = y
        self.image = image

def place(screen , catapult1: Catapult, catapult2: Catapult):
    pygame.init()
    clock = pygame.time.Clock()

    pygame.display.set_caption("Angry Birds - 2 Player")
    pygame.display.set_icon(pygame.image.load("images/icon.png"))
    background = pygame.image.load("images/background.png")
    background = pygame.transform.scale(background, (800, 500))

    pygame.display.set_caption("Angry Birds - 2 Player")
    pygame.display.set_icon(pygame.image.load("images/icon.png"))
    background = pygame.image.load("images/background.png")
    background = pygame.transform.scale(background, (1280, 720))

    running = True
    while running:
        screen.blit(background, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.blit(catapult1.image, (catapult1.x, catapult1.y))
        screen.blit(catapult2.image, (catapult2.x, catapult2.y))
        
        pygame.display.flip()
        clock.tick(60)
    pygame.quit()