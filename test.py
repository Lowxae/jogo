import pygame
import sys
import time

pygame.init()

WIDTH, HEIGHT = 800, 600
MENU_IMAGE = "menu_background.jpg"
LOGO_IMAGE = "mih-logo.png"
LAUGH_SOUND = "Laugh.mp3"

WHITE = (255, 255, 255)
RED = (255, 0, 0)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Made in Hell")

background = pygame.image.load(MENU_IMAGE)
background = pygame.transform.scale(background, (WIDTH, HEIGHT))

logo = pygame.image.load(LOGO_IMAGE)
logo = pygame.transform.scale(logo, (600, 600))

font = pygame.font.Font(None, 36)
message = font.render("Press F to start and be RESPECTFUL", True, WHITE)

game_state = "menu"
audio_played = False
start_time = 0

pygame.mixer.init()
laugh_sound = pygame.mixer.Sound(LAUGH_SOUND)
laugh_sound.set_volume(0.5)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            if event.key == pygame.K_f and game_state == "menu":
                if not audio_played:
                    laugh_sound.play()
                    start_time = time.time()
                    audio_played = True

    screen.fill(WHITE)

    if game_state == "menu":
        screen.blit(background, (0, 0))
        screen.blit(logo, (WIDTH // 2 - logo.get_width() // 2, 0))
        screen.blit(message, (WIDTH // 2 - message.get_width() // 2, 400))

        if audio_played and time.time() - start_time >= 2:
            game_state = "game"
    elif game_state == "game":
        pygame.draw.circle(screen, RED, (WIDTH // 2, HEIGHT // 2), 100)

    pygame.display.flip()

pygame.quit()
sys.exit()
