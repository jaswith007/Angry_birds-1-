import pygame # type: ignore
import menu
import catapult
import bird

x_length = 1280
y_length = 720

image1 = pygame.image.load("images/catapult.png")
image1 = pygame.transform.scale(image1, (0.1*x_length, 100))
image2 = pygame.transform.flip(image1, True, False)
catapult1 = catapult.Catapult(0.2*x_length, 520, image1)
catapult2 = catapult.Catapult(0.7*x_length, 520, image2)
bird1 = bird.Bird(0.22*x_length, 520, 20, "red")
bird2 = bird.Bird(0.23*x_length, 520, 20, "blue")
bird3 = bird.Bird(0.24*x_length, 520, 20, "yellow")
bird4 = bird.Bird(0.25*x_length, 520, 20, "black")

pygame.init()
screen = pygame.display.set_mode((x_length, y_length))

background = pygame.image.load("images/background.png")
background = pygame.transform.scale(background, (1280,720)) # Changes the size of the image to 800x500

running = True
game_state = "menu"
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if game_state == "menu":
        game_state = menu.menu_screen(screen, background)

    if game_state == "game":
        # FIRST: CLEAR the screen (draw background)
        screen.fill((255, 255, 255))  # Or 
        screen.blit(background, (0, 0))
        
        # THEN: draw all game objects
        catapult.catapult_place(screen, catapult1, catapult2)
        bird1.bird_place(screen)
        bird2.bird_place(screen)
        bird3.bird_place(screen)
        bird4.bird_place(screen)

        # FINALLY: update the display
        pygame.display.flip()
