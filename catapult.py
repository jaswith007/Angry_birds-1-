import pygame # type: ignore

class Catapult:
    def __init__(self, x, y, image):
        self.x = x
        self.y = y
        self.image = image

def catapult_place(screen , catapult1: Catapult, catapult2: Catapult):
    pygame.init()

    pygame.display.set_caption("Angry Birds - 2 Player")
    pygame.display.set_icon(pygame.image.load("images/icon.png"))
    background = pygame.image.load("images/background.png")
    background = pygame.transform.scale(background, (800, 500))

    pygame.display.set_caption("Angry Birds - 2 Player")
    pygame.display.set_icon(pygame.image.load("images/icon.png"))
    background = pygame.image.load("images/background.png")
    background = pygame.transform.scale(background, (1280, 720)) # Changes the size of the image to 800x500

    
    screen.blit(catapult1.image, (catapult1.x, catapult1.y))
    screen.blit(catapult2.image, (catapult2.x, catapult2.y))