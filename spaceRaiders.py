import pygame

# initialize pygame
pygame.init()

# set screen size
screen_width = 600
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))

# set title
pygame.display.set_caption("Space Raiders")

# set player variables
player_x = 300
player_y = 700
player_speed = 5

# set enemy variables
enemy_x = 50
enemy_y = 50
enemy_speed = 2

# game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # move player
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_x += player_speed

    # move enemy
    enemy_x += enemy_speed
    if enemy_x > screen_width or enemy_x < 0:
        enemy_speed = -enemy_speed

    # clear screen
    screen.fill((0, 0, 0))

    # draw player
    pygame.draw.rect(screen, (255, 255, 255), (player_x, player_y, 50, 50))

    # draw enemy
    pygame.draw.rect(screen, (255, 0, 0), (enemy_x, enemy_y, 50, 50))

    # update screen
    pygame.display.update()

# close pygame
pygame.quit()
