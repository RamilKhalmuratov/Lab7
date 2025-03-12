import pygame

pygame.init()

WIDTH, HEIGHT = 400, 300
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Move the Ball")

ball_radius = 25
ball_x, ball_y = WIDTH // 2, HEIGHT // 2
ball_color = (255, 0, 0)

ball_speed = 20

font = pygame.font.Font(None, 36)

running = True
while running:
    screen.fill((255, 255, 255))
    pygame.draw.circle(screen, ball_color, (ball_x, ball_y), ball_radius)
    text = font.render("Use Arrow Keys to Move", True, (0, 0, 0))
    screen.blit(text, (10, 10))

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if ball_y - ball_radius - ball_speed >= 0:
                    ball_y -= ball_speed
            elif event.key == pygame.K_DOWN:
                if ball_y + ball_radius + ball_speed <= HEIGHT:
                    ball_y += ball_speed
            elif event.key == pygame.K_LEFT:
                if ball_x - ball_radius - ball_speed >= 0:
                    ball_x -= ball_speed
            elif event.key == pygame.K_RIGHT:
                if ball_x + ball_radius + ball_speed <= WIDTH:
                    ball_x += ball_speed

pygame.quit()
