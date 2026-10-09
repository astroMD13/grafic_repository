# Oi.
#Faz o que quiseres
#Sou o Mateus
# Example file showing a circle moving on screen
import pygame
import random 
# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)


estrelas = []
for _ in range(100):
    x = random.randint(0, 1280)
    y = random.randint(0, 720)
    estrelas.append((x, y))

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        player_pos.x -= 300 * dt
    if keys[pygame.K_d]:
        player_pos.x += 300 * dt

    LARGURA_PLAYER = 40
    ALTURA_PLAYER = 40

    if player_pos.x > 1280 - LARGURA_PLAYER: player_pos.x = 1280 - LARGURA_PLAYER
    if player_pos.x < 0: player_pos.x = 0
    if player_pos.y > 720 - ALTURA_PLAYER: player_pos.y = 720 - ALTURA_PLAYER
    if player_pos.y < 0: player_pos.y = 0

    screen.fill("black")
    square_rect = pygame.Rect(player_pos.x, player_pos.y, 40, 40)
    pygame.draw.rect(screen, "white", square_rect)
    square_rect_window = pygame.Rect(player_pos.x + 17.5, player_pos.y - 20, 5, 40)
    pygame.draw.rect(screen, "white", square_rect_window)
    square_rect_back = pygame.Rect(player_pos.x - 10, player_pos.y + 20, 60, 40)
    pygame.draw.rect(screen, "white", square_rect_back)



    for x, y in estrelas:
        pygame.draw.circle(screen, (255, 255, 255), (x, y), 2)
  

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()
