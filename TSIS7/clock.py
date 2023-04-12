import pygame
import time

pygame.init()

WINDOW_WIDTH = 1400
WINDOW_HEIGHT = 1050

screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Mickey Clock")

mickey_image = pygame.image.load("./images/mickeyclock.jpeg")

mickey_center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    current_time = time.localtime()
    seconds = current_time.tm_sec
    minutes = current_time.tm_min

    minute_hand_image = pygame.transform.rotate(mickey_image, -6 * minutes)

    second_hand_image = pygame.transform.rotate(mickey_image, -6 * seconds)

    screen.blit(minute_hand_image, minute_hand_image.get_rect(center=mickey_center))
    screen.blit(second_hand_image, second_hand_image.get_rect(center=mickey_center))

    pygame.display.flip()

    clock.tick(1)

