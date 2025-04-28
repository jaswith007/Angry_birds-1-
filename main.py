import pygame
import menu
import catapult
import bird
import fortress

x_length = 1280
y_length = 720

k = 8

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

fortress_x_size = 10
fortress_y_size = 5

fortress_left = fortress.Fortress(100, 615, fortress_x_size, fortress_y_size)
fortress_right = fortress.Fortress(x_length - (fortress_x_size+2)*35, 615, fortress_x_size, fortress_y_size)

top_bird_1 = None
top_bird_2 = None

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((x_length, y_length))

background = pygame.image.load("images/background.png")
background = pygame.transform.scale(background, (x_length, y_length)) 

running = True
game_state = "game"
dragging_1 = False
released_1 = False
dragging_2 = False
released_2 = False
while running:
    dt = clock.tick(120)/1000
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False

    if game_state == "menu":
        game_state = menu.menu_screen(screen, background)

    if game_state == "game":
        screen.fill((255, 255, 255)) 
        screen.blit(background, (0, 0))

        fortress_left.fortress_place(screen)
        fortress_right.fortress_place(screen)

        catapult.catapult_place(screen, catapult1, catapult2)
        bird1_1.bird_place(1, screen)
        bird2_1.bird_place(1, screen)
        bird3_1.bird_place(1, screen)
        bird4_1.bird_place(1, screen)
        bird1_2.bird_place(2, screen)
        bird2_2.bird_place(2, screen)
        bird3_2.bird_place(2, screen)
        bird4_2.bird_place(2, screen)
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if bird1_1.is_clicked():
                    top_bird_1 = bird1_1
                    top_bird_2 = None
                    bird1_1.update(1)
                    bird1_1.rect.x = 0.26*1280
                    bird1_1.rect.y = 515
                    bird2_1.revert(1)
                    bird3_1.revert(1)
                    bird4_1.revert(1)
                    released_1 = False
                elif bird2_1.is_clicked():
                    top_bird_1 = bird2_1
                    top_bird_2 = None
                    bird2_1.update(1)
                    bird2_1.rect.x = 0.26*1280
                    bird2_1.rect.y = 515
                    bird1_1.revert(1)
                    bird3_1.revert(1)
                    bird4_1.revert(1)
                    released_1 = False
                elif bird3_1.is_clicked():
                    top_bird_1 = bird3_1
                    top_bird_2 = None
                    bird3_1.update(1)
                    bird3_1.rect.x = 0.26*1280
                    bird3_1.rect.y = 515
                    bird1_1.revert(1)
                    bird2_1.revert(1)
                    bird4_1.revert(1)
                    released_1 = False
                elif bird4_1.is_clicked():
                    top_bird_1 = bird4_1
                    top_bird_2 = None
                    bird4_1.update(1)
                    bird4_1.rect.x = 0.26*1280
                    bird4_1.rect.y = 515
                    bird1_1.revert(1)
                    bird2_1.revert(1)
                    bird3_1.revert(1)
                    released_1 = False
                elif bird1_2.is_clicked():
                    top_bird_2 = bird1_2
                    top_bird_1 = None
                    bird1_2.update(2)
                    bird1_2.rect.x = 0.76*1280
                    bird1_2.rect.y = 515
                    bird2_2.revert(2)
                    bird3_2.revert(2)
                    bird4_2.revert(2)
                    released_2 = False
                elif bird2_2.is_clicked():
                    top_bird_2 = bird2_2
                    top_bird_1 = None
                    bird2_2.update(2)
                    bird2_2.rect.x = 0.76*1280
                    bird2_2.rect.y = 515
                    bird1_2.revert(2)
                    bird3_2.revert(2)
                    bird4_2.revert(2)
                    released_2 = False
                elif bird3_2.is_clicked():
                    top_bird_2 = bird3_2
                    top_bird_1 = None
                    bird3_2.update(2)
                    bird3_2.rect.x = 0.76*1280
                    bird3_2.rect.y = 515
                    bird1_2.revert(2)
                    bird2_2.revert(2)
                    bird4_2.revert(2)
                    released_2 = False
                elif bird4_2.is_clicked():
                    top_bird_2 = bird4_2
                    top_bird_1 = None
                    bird4_2.update(2)
                    bird4_2.rect.x = 0.76*1280
                    bird4_2.rect.y = 515
                    bird1_2.revert(2)
                    bird2_2.revert(2)
                    bird3_2.revert(2)
                    released_2 = False
                if top_bird_1 and top_bird_1.rect.collidepoint(event.pos):
                    dragging_1 = True
                if top_bird_2 and top_bird_2.rect.collidepoint(event.pos):
                    dragging_2 = True
            if event.type == pygame.MOUSEBUTTONUP:
                if top_bird_1:
                    if top_bird_1.rect.collidepoint(event.pos):
                        dragging_1 = False
                        released_1 = True
                        if top_bird_1:
                            top_bird_1.velocityX = -k*(event.pos[0] - 0.26*x_length)
                            top_bird_1.velocityY = -k*(event.pos[1] - 515)
                if top_bird_2:
                    if top_bird_2.rect.collidepoint(event.pos):
                        dragging_2 = False
                        released_2 = True
                        if top_bird_2:
                            top_bird_2.velocityX = -k*(event.pos[0] - 0.76*x_length)
                            top_bird_2.velocityY = -k*(event.pos[1] - 515)
                

            if event.type == pygame.MOUSEMOTION:
                if dragging_1:
                    top_bird_1.rect.center = event.pos
                    top_bird_1.x, top_bird_1.y = top_bird_1.rect.topleft
                if dragging_2:
                    top_bird_2.rect.center = event.pos
                    top_bird_2.x, top_bird_2.y = top_bird_2.rect.topleft

        if top_bird_1 and released_1:
            top_bird_1.velocityY += top_bird_1.gravity * dt  # Gravity affects vertical speed
            top_bird_1.x += top_bird_1.velocityX * dt
            top_bird_1.y += top_bird_1.velocityY * dt
            top_bird_1.rect.x = top_bird_1.x
            top_bird_1.rect.y = top_bird_1.y
        if top_bird_2 and released_2:
            top_bird_2.velocityY += top_bird_2.gravity * dt  # Gravity affects vertical speed
            top_bird_2.x += top_bird_2.velocityX * dt
            top_bird_2.y += top_bird_2.velocityY * dt
            top_bird_2.rect.x = top_bird_2.x
            top_bird_2.rect.y = top_bird_2.y

        for block in fortress_right.blocks: 
            if top_bird_1 and top_bird_1.rect.colliderect(block.rect):
                dx_1 = (top_bird_1.rect.centerx - block.rect.centerx)
                dy_1 = (top_bird_1.rect.centery - block.rect.centery)

                if abs(dx_1) > abs(dy_1):  # Horizontal collision
                    top_bird_1.velocityX *= -1
                else:                  # Vertical collision
                    top_bird_1.velocityY *= -1
           
        for block in fortress_left.blocks:
            if top_bird_2 and top_bird_2.rect.colliderect(block.rect):
                dx_2 = (top_bird_2.rect.centerx - block.rect.centerx)
                dy_2 = (top_bird_2.rect.centery - block.rect.centery)

                if abs(dx_2) > abs(dy_2):  # Horizontal collision
                    top_bird_2.velocityX *= -1
                else:                  # Vertical collision
                    top_bird_2.velocityY *= -1
            
        pygame.display.flip()
