import pygame
import time
import math

pygame.init()

WIDTH, HEIGHT = 500, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mickey Mouse Clock")

clock_img = pygame.image.load("image.png")
clock_img = pygame.transform.scale(clock_img, (WIDTH, HEIGHT))

def draw_hand(image, angle, center, length, offset=(0, 0)):
    rotated_image = pygame.transform.rotate(image, angle)
    rect = rotated_image.get_rect(center=center)
    screen.blit(rotated_image, (rect.x + offset[0], rect.y + offset[1]))

hand_image = pygame.Surface((10, 100), pygame.SRCALPHA)
pygame.draw.rect(hand_image, (0, 0, 0), (4, 0, 2, 100))

running = True
while running:
    screen.fill((255, 255, 255))
    screen.blit(clock_img, (0, 0))

    current_time = time.localtime()
    minutes = current_time.tm_min
    seconds = current_time.tm_sec

    min_angle = -(minutes * 6)
    sec_angle = -(seconds * 6)

    draw_hand(hand_image, min_angle, (WIDTH // 2, HEIGHT // 2), 100)
    draw_hand(hand_image, sec_angle, (WIDTH // 2, HEIGHT // 2), 120)

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
