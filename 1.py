import pygame
import time
import math

pygame.init()

WIDTH, HEIGHT = 500, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mickey Mouse Clock")

clock_img = pygame.image.load("image.png")
clock_img = pygame.transform.scale(clock_img, (WIDTH, HEIGHT))

def draw_hand(surface, angle, center, length, width, color):
    end_x = center[0] + length * math.cos(math.radians(angle))
    end_y = center[1] - length * math.sin(math.radians(angle))
    pygame.draw.line(surface, color, center, (end_x, end_y), width)

running = True
while running:
    screen.fill((255, 255, 255))
    screen.blit(clock_img, (0, 0))

    current_time = time.localtime()
    hours = current_time.tm_hour % 12
    minutes = current_time.tm_min
    seconds = current_time.tm_sec

    sec_angle = -(seconds * 6 - 90)
    min_angle = -(minutes * 6 - 90)
    hour_angle = -(hours * 30 + minutes * 0.5 - 90)

    draw_hand(screen, hour_angle, (WIDTH // 2, HEIGHT // 2), 80, 8, (0, 0, 0))
    draw_hand(screen, min_angle, (WIDTH // 2, HEIGHT // 2), 100, 5, (0, 0, 0))
    draw_hand(screen, sec_angle, (WIDTH // 2, HEIGHT // 2), 120, 2, (255, 0, 0))

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()