import pygame
import menu
import catapult
import bird
import fortress

x_length = 1280
y_length = 720

image1 = pygame.image.load("images/catapult.png")
image1 = pygame.transform.scale(image1, (0.15*x_length, 100))
image2 = pygame.transform.flip(image1, True, False)
catapult1 = catapult.Catapult(0.2*x_length, 520, image1)
catapult2 = catapult.Catapult(0.7*x_length, 520, image2)

bird1_1 = bird.Bird(0.27*x_length, 590, 15, "red")
bird2_1 = bird.Bird(0.3*x_length, 590, 15, "blue")
bird3_1 = bird.Bird(0.33*x_length, 590, 15, "yellow")
bird4_1 = bird.Bird(0.36*x_length, 590, 15, "black")

bird1_2 = bird.Bird(0.76*x_length, 590, 15, "red")
bird2_2 = bird.Bird(0.73*x_length, 590, 15, "blue")
bird3_2 = bird.Bird(0.70*x_length, 590, 15, "yellow")
bird4_2 = bird.Bird(0.67*x_length, 590, 15, "black")

ice1 = pygame.transform.scale(pygame.image.load("images/ice_block1.png"), (35, 35))
ice2 = pygame.transform.scale(pygame.image.load("images/ice_block2.png"), (35, 35))
wood1 = pygame.transform.scale(pygame.image.load("images/wooden_block1.png"), (35, 35))
wood2 = pygame.transform.scale(pygame.image.load("images/wooden_block2.png"), (35, 35))
stone1 = pygame.transform.scale(pygame.image.load("images/stone_block1.png"), (35, 35))
stone2 = pygame.transform.scale(pygame.image.load("images/stone_block2.png"), (35, 35))

fortress_x_size = 4
fortress_y_size = 5

fortress_left = fortress.Fortress(100, 615, fortress_x_size, fortress_y_size)
fortress_right = fortress.Fortress(x_length - (fortress_x_size+2)*35, 615, fortress_x_size, fortress_y_size)

pygame.init()
screen = pygame.display.set_mode((x_length, y_length))

background = pygame.image.load("images/background.png")
background = pygame.transform.scale(background, (x_length, y_length)) 

running = True
game_state = "game"
while running:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False

    if game_state == "menu":
        game_state = menu.menu_screen(screen, background)

    if game_state == "game":
        screen.fill((255, 255, 255)) 
        screen.blit(background, (0, 0))

        catapult.catapult_place(screen, catapult1, catapult2)
        bird1_1.bird_place(1, screen)
        bird2_1.bird_place(1, screen)
        bird3_1.bird_place(1, screen)
        bird4_1.bird_place(1, screen)
        bird1_2.bird_place(2, screen)
        bird2_2.bird_place(2, screen)
        bird3_2.bird_place(2, screen)
        bird4_2.bird_place(2, screen)

        fortress_left.fortress_place(screen)
        fortress_right.fortress_place(screen)

        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if bird1_1.is_clicked():
                    bird1_1.update(1)
                    bird2_1.revert(1)
                    bird3_1.revert(1)
                    bird4_1.revert(1)
                elif bird2_1.is_clicked():
                    bird2_1.update(1)
                    bird1_1.revert(1)
                    bird3_1.revert(1)
                    bird4_1.revert(1)
                elif bird3_1.is_clicked():
                    bird3_1.update(1)
                    bird1_1.revert(1)
                    bird2_1.revert(1)
                    bird4_1.revert(1)
                elif bird4_1.is_clicked():
                    bird4_1.update(1)
                    bird1_1.revert(1)
                    bird2_1.revert(1)
                    bird3_1.revert(1)
                elif bird1_2.is_clicked():
                    bird1_2.update(2)
                    bird2_2.revert(2)
                    bird3_2.revert(2)
                    bird4_2.revert(2)
                elif bird2_2.is_clicked():
                    bird2_2.update(2)
                    bird1_2.revert(2)
                    bird3_2.revert(2)
                    bird4_2.revert(2)
                elif bird3_2.is_clicked():
                    bird3_2.update(2)
                    bird1_2.revert(2)
                    bird2_2.revert(2)
                    bird4_2.revert(2)
                elif bird4_2.is_clicked():
                    bird4_2.update(2)
                    bird1_2.revert(2)
                    bird2_2.revert(2)
                    bird3_2.revert(2)        
        pygame.display.flip()
