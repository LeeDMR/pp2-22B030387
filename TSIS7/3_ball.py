import pygame

pygame.init()

WINDOW_SIZE = (800, 600)
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Moving Circle")

BALL_SIZE = 50
BALL_RADIUS = BALL_SIZE // 2
ball_color = (255, 0, 0)  # red
ball_x = WINDOW_SIZE[0] // 2
ball_y = WINDOW_SIZE[1] // 2

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and ball_y - 20 > BALL_RADIUS:
        ball_y -= 20
    if keys[pygame.K_DOWN] and ball_y + 20 < WINDOW_SIZE[1] - BALL_RADIUS:
        ball_y += 20
    if keys[pygame.K_LEFT] and ball_x - 20 > BALL_RADIUS:
        ball_x -= 20
    if keys[pygame.K_RIGHT] and ball_x + 20 < WINDOW_SIZE[0] - BALL_RADIUS:
        ball_x += 20

    screen.fill((255, 255, 255))
    pygame.draw.circle(screen, ball_color, (ball_x, ball_y), BALL_RADIUS)

    pygame.display.update()
    clock.tick(60)
