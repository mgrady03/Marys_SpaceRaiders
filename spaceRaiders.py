import pygame


pygame.init()


screen_width = 600
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))


pygame.display.set_caption("Space Raiders")


player_x = 300
player_y = 700
player_speed = 5


enemy_x = 50
enemy_y = 50
enemy_speed = 2


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_x += player_speed


    enemy_x += enemy_speed
    if enemy_x > screen_width or enemy_x < 0:
        enemy_speed = -enemy_speed

    screen.fill((0, 0, 0))


    pygame.draw.rect(screen, (255, 255, 255), (player_x, player_y, 50, 50))


    pygame.draw.rect(screen, (255, 0, 0), (enemy_x, enemy_y, 50, 50))


    pygame.display.update()


pygame.quit()
