import pygame
import sys
import time

pygame.init()

WIDTH, HEIGHT = 1280, 720
MENU_IMAGE = "menu_background.png"
LOGO_IMAGE = "mih-logo.png"
LAUGH_SOUND = "Laugh.mp3"
FULL_SCREEN_TEXT = "F11 - Full Screen"
WHITE = (255, 255, 255)
RED = (255, 0, 0)
AUDIO_STATUS_TEXT = "M - Music - ON"
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Made in Hell")

background = pygame.image.load(MENU_IMAGE)
background = pygame.transform.scale(background, (WIDTH, HEIGHT))

logo = pygame.image.load(LOGO_IMAGE)
logo = pygame.transform.scale(logo, (600, 600))

font = pygame.font.Font(None, 36)
start_game_menu_text = font.render("Press F to start and be RESPECTFUL", True, WHITE)


font2=pygame.font.Font(None, 20)
fullScreen_menu_text = font2.render(FULL_SCREEN_TEXT,True,WHITE)
audio_menu_text = font2.render(AUDIO_STATUS_TEXT,True,WHITE)


game_state = "menu"
audio_played = False
start_time = 0

pygame.mixer.init()
laugh_sound = pygame.mixer.Sound(LAUGH_SOUND)
laugh_sound.set_volume(0.5)

fullscreen = False
audio=True

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
            if event.key == pygame.K_F11:
                fullscreen = not fullscreen
                if fullscreen:
                    screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
                    FULL_SCREEN_TEXT="F11 - Leave Full Screen"
                else:
                    screen = pygame.display.set_mode((WIDTH, HEIGHT))
                    FULL_SCREEN_TEXT = "F11 - Full Screen"
                fullScreen_menu_text = font2.render(FULL_SCREEN_TEXT, True, WHITE)
            if event.key ==pygame.K_m:
                audio = not audio
                if not audio:
                    AUDIO_STATUS_TEXT = "M - Music - OFF"
                else:
                     AUDIO_STATUS_TEXT = "M - Music - ON" 
                audio_menu_text = font2.render(AUDIO_STATUS_TEXT,True,WHITE)            
                

                


    screen.fill(WHITE)

    if game_state == "menu":
        screen.blit(background, (0, 0))
        screen.blit(logo, (WIDTH // 2 - logo.get_width() // 2, 0))
        screen.blit(start_game_menu_text, (WIDTH // 2 - start_game_menu_text.get_width() // 2, 400))
        screen.blit(fullScreen_menu_text, (WIDTH // 2 - fullScreen_menu_text.get_width() // 2, 550))
        screen.blit(audio_menu_text,(WIDTH//2-audio_menu_text.get_width()//2,570))

        if audio_played and time.time() - start_time >= 2:
            game_state = "game"
    elif game_state == "game":
        pygame.draw.circle(screen, RED, (WIDTH // 2, HEIGHT // 2), 100)

    pygame.display.flip()

pygame.quit()
sys.exit()
