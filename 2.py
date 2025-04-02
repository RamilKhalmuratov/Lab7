import pygame
import os

pygame.init()

WIDTH, HEIGHT = 400, 300
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Music Player")

font = pygame.font.Font(None, 36)

MUSIC_FOLDER = "musicc"
songs = [f for f in os.listdir(MUSIC_FOLDER) if f.endswith(".mp3")]
current_song = 0
paused = False

def load_song(index):
    pygame.mixer.music.load(os.path.join(MUSIC_FOLDER, songs[index]))
    pygame.mixer.music.play()

load_song(current_song)

running = True
while running:
    screen.fill((30, 30, 30))
    
    text = font.render(f"Now Playing: {songs[current_song]}", True, (255, 255, 255))
    screen.blit(text, (20, 120))

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                pygame.mixer.music.unpause()
                paused = False
            elif event.key == pygame.K_x:
                pygame.mixer.music.stop()
            elif event.key == pygame.K_c:
                current_song = (current_song + 1) % len(songs)
                load_song(current_song)
            elif event.key == pygame.K_SPACE:
                current_song = (current_song - 1) % len(songs)
                load_song(current_song)
            elif event.key == pygame.K_p:
                if paused:
                    pygame.mixer.music.unpause()
                else:
                    pygame.mixer.music.pause()
                paused = not paused

pygame.quit()
