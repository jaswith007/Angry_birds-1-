import pygame
import menu
import catapult
import bird
import fortress
import random
import sys


x_length = 1280
y_length = 720

font = pygame.font.Font("sf-cartoonist-hand.italic.ttf", 35)

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

fortress_x_size = 1
fortress_y_size = 1

fortress_left = fortress.Fortress(100, 615, fortress_x_size, fortress_y_size)
fortress_right = fortress.Fortress(x_length - (fortress_x_size+2)*35, 615, fortress_x_size, fortress_y_size)

top_bird_1 = None
top_bird_2 = None

MAX_drag = 100

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((x_length, y_length))

background = pygame.image.load("images/background.png")
background = pygame.transform.scale(background, (x_length, y_length)) 

running = True
game_state = "menu"
dragging_1 = False
released_1 = False
dragging_2 = False
released_2 = False
player_1 = ""
player_2 = ""
turn = random.choice(["player1","player2"])
game_over = False

def calculate_trajectory(x, y, velocityX, velocityY, gravity, steps=150, dT=clock.tick(120)/1000):
    points = []
    for i in range(steps):
        t = i * dT
        new_x = x + velocityX * t
        new_y = y + velocityY * t + 0.5 * gravity * t**2
        points.append((new_x, new_y))
    return points

while running:
    dt = clock.tick(120)/1000
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False

    if game_state == "menu":
        game_state = menu.menu_screen(screen, background)
        player_1 = menu.text1
        player_2 = menu.text2

        # After leaving menu, show who starts
        screen.fill((255, 255, 255))
        screen.blit(background, (0, 0))
        start_msg = f"{player_1 if turn == 'player1' else player_2} starts the match!"
        start_text = font.render(start_msg, True, (0, 0, 0))
        start_rect = start_text.get_rect(center=(x_length // 2, y_length // 2))
        screen.blit(start_text, start_rect)
        pygame.display.flip()
        pygame.time.wait(3000)  # Show for 3 seconds

    if game_state == "game":
        screen.fill((255, 255, 255)) 
        screen.blit(background, (0, 0))
        player1 = font.render(player_1, True, (0, 0, 0)) 
        player2 = font.render(player_2, True, (0, 0, 0))
        player1_rect = player1.get_rect(topleft = (10, 10))
        player2_rect = player2.get_rect(topright = (1270, 10))
        screen.blit(player1, player1_rect)
        screen.blit(player2, player2_rect)

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
                if turn == "player1":
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
                if turn == "player2":
                    if bird1_2.is_clicked():
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
                if top_bird_1 and dragging_1:
                    dragging_1 = False
                    released_1 = True
                    top_bird_1.velocityX = -k*(event.pos[0] - 0.26*x_length)
                    top_bird_1.velocityY = -k*(event.pos[1] - 515)
                    turn = "player2"
                if top_bird_2 and dragging_2:
                    dragging_2 = False
                    released_2 = True
                    top_bird_2.velocityX = -k*(event.pos[0] - 0.76*x_length)
                    top_bird_2.velocityY = -k*(event.pos[1] - 515)
                    turn = "player1"

            if event.type == pygame.MOUSEMOTION:
                catapult_center = (0.26*x_length, 515) if top_bird_1 else (0.76*x_length, 515)
                magnitude = ((event.pos[0] - catapult_center[0])**2 + (event.pos[1] - catapult_center[1])**2)**0.5
                normalized_x = (event.pos[0] - catapult_center[0]) / magnitude
                normalized_y = (event.pos[1] - catapult_center[1]) / magnitude

                if dragging_1:
                    if magnitude <= MAX_drag and not event.pos == (0, 0) :
                        top_bird_1.rect.center = event.pos
                        top_bird_1.x, top_bird_1.y = top_bird_1.rect.topleft
                    else:
                        top_bird_1.rect.center = (catapult_center[0] + normalized_x*MAX_drag, catapult_center[1] + normalized_y*MAX_drag)
                        top_bird_1.x, top_bird_1.y = top_bird_1.rect.topleft
                if dragging_2:
                    if magnitude <= MAX_drag and not event.pos == (0, 0):
                        top_bird_2.rect.center = event.pos
                        top_bird_2.x, top_bird_2.y = top_bird_2.rect.topleft
                    else:
                        top_bird_2.rect.center = (catapult_center[0] + normalized_x*MAX_drag, catapult_center[1] + normalized_y*MAX_drag)
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
                block.damage(top_bird_1)
                if block.hp <= 0:
                    fortress_right.blocks.remove(block)
                dx_1 = (top_bird_1.rect.centerx - block.rect.centerx)
                dy_1 = (top_bird_1.rect.centery - block.rect.centery)

                if abs(dx_1) > abs(dy_1):  # Horizontal collision
                    top_bird_1.velocityX *= -1
                else:                  # Vertical collision
                    top_bird_1.velocityY *= -1
                if fortress_right.blocks == [] and not game_over:
                    win = player_1 + " won the game!"
                    winner_message = font.render(win, True, (0, 0, 0))
                    win_rect = winner_message.get_rect(center=(640, 200))
                    screen.blit(winner_message, win_rect)
                    pygame.display.flip()
                    print(f"{player_1} won the game")
                    game_over = True
                    pygame.time.wait(3000)
                    pygame.quit()
                    sys.exit()

           
        for block in fortress_left.blocks:
            if top_bird_2 and top_bird_2.rect.colliderect(block.rect):
                block.damage(top_bird_2)
                if block.hp <= 0:
                    fortress_left.blocks.remove(block)
                dx_2 = (top_bird_2.rect.centerx - block.rect.centerx)
                dy_2 = (top_bird_2.rect.centery - block.rect.centery)

                if abs(dx_2) > abs(dy_2):  # Horizontal collision
                    top_bird_2.velocityX *= -1
                else:                  # Vertical collision
                    top_bird_2.velocityY *= -1
                if fortress_left.blocks == [] and not game_over:
                    win = player_2 + " won the game!"
                    winner_message = font.render(win, True, (0, 0, 0))
                    win_rect = winner_message.get_rect(center=(640, 200))
                    screen.blit(winner_message, win_rect)
                    pygame.display.flip()
                    print(f"{player_2} won the game")
                    game_over = True
                    pygame.time.wait(3000)
                    pygame.quit()
                    sys.exit()

        # For player 1
        if dragging_1 and top_bird_1:
            catapult_center = (0.26*x_length, 515)
            dx = top_bird_1.rect.centerx - catapult_center[0]
            dy = top_bird_1.rect.centery - catapult_center[1]
            velocityX = -k * dx
            velocityY = -k * dy

            traj_points = calculate_trajectory(catapult_center[0], catapult_center[1], velocityX, velocityY, top_bird_1.gravity)
            for point in traj_points:
                pygame.draw.circle(screen, (0, 0, 0), (int(point[0]), int(point[1])), 3)
        # For player 1
        if dragging_2 and top_bird_2:
            catapult_center = (0.76*x_length, 515)
            dx = top_bird_2.rect.centerx - catapult_center[0]
            dy = top_bird_2.rect.centery - catapult_center[1]
            velocityX = -k * dx
            velocityY = -k * dy

            traj_points = calculate_trajectory(catapult_center[0], catapult_center[1], velocityX, velocityY, top_bird_2.gravity)
            for point in traj_points:
                pygame.draw.circle(screen, (0, 0, 0), (int(point[0]), int(point[1])), 3)

        pygame.display.flip()
