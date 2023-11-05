import pygame
import sys
import time

pygame.init()

WIDTH, HEIGHT = 1280, 720
MENU_IMAGE = "menu_background.png"
LOGO_IMAGE = "mih-logo.png"
LAUGH_SOUND = "Laugh.mp3"
FULL_SCREEN_TEXT = "F11 - Full Screen"
ROUND_IMAGE = "round_1.png"
SPRITE_IMAGE = "sprite_1.png"
BACKGROUND_IMAGE = "background_game.png"
WHITE = (255, 255, 255)
AUDIO_STATUS_TEXT = "M - Music - ON"
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Made in Hell")

background = pygame.image.load(MENU_IMAGE)
background = pygame.transform.scale(background, (WIDTH, HEIGHT))

background_game = pygame.image.load(BACKGROUND_IMAGE)
background_game = pygame.transform.scale(background_game, (WIDTH, HEIGHT))

logo = pygame.image.load(LOGO_IMAGE)
logo = pygame.transform.scale(logo, (600, 600))

font = pygame.font.Font(None, 36)
start_game_menu_text = font.render("Press F to start and be RESPECTFUL", True, WHITE)

font2 = pygame.font.Font(None, 20)
fullScreen_menu_text = font2.render(FULL_SCREEN_TEXT, True, WHITE)
audio_menu_text = font2.render(AUDIO_STATUS_TEXT, True, WHITE)

game_state = "menu"
audio_played = False
start_time = 0

pygame.mixer.init()
laugh_sound = pygame.mixer.Sound(LAUGH_SOUND)
laugh_sound.set_volume(0.5)

fullscreen = False
audio = True

round_start_time = 0
show_round_screen = False

player_x = WIDTH // 2
player_y = HEIGHT // 2
player_speed = 0.6

sprite_image = pygame.image.load(SPRITE_IMAGE)
sprite_image = pygame.transform.scale(sprite_image, (110, 110))
sprite_x = player_x
sprite_y = player_y
sprite_angle = 0.0
sprite_rotate_speed = 1

rotate_sprite = False
can_move = True
reverse_rotation = False

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
                    FULL_SCREEN_TEXT = "F11 - Leave Full Screen"
                else:
                    screen = pygame.display.set_mode((WIDTH, HEIGHT))
                    FULL_SCREEN_TEXT = "F11 - Full Screen"
                fullScreen_menu_text = font2.render(FULL_SCREEN_TEXT, True, WHITE)
            if event.key == pygame.K_m:
                audio = not audio
                if not audio:
                    AUDIO_STATUS_TEXT = "M - Music - OFF"
                else:
                    AUDIO_STATUS_TEXT = "M - Music - ON"
                audio_menu_text = font2.render(AUDIO_STATUS_TEXT, True, WHITE)
            if event.key == pygame.K_c:
                rotate_sprite = True
                can_move = False
            if event.key == pygame.K_v:
                rotate_sprite = True
                can_move = False
                reverse_rotation = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_c:
                rotate_sprite = False
                can_move = True
            if event.key == pygame.K_v:
                rotate_sprite = False
                can_move = True
                reverse_rotation = False

    keys = pygame.key.get_pressed()

    if can_move:
        if keys[pygame.K_LEFT]:
            player_x -= player_speed
        if keys[pygame.K_RIGHT]:
            player_x += player_speed
        if keys[pygame.K_UP]:
            player_y -= player_speed
        if keys[pygame.K_DOWN]:
            player_y += player_speed

    player_x = max(0, min(player_x, WIDTH))
    player_y = max(0, min(player_y, HEIGHT))

    screen.blit(background_game, (0, 0))

    if game_state == "menu":
        screen.blit(background, (0, 0))
        screen.blit(logo, (WIDTH // 2 - logo.get_width() // 2, 0))
        screen.blit(start_game_menu_text, (WIDTH // 2 - start_game_menu_text.get_width() // 2, 400))
        screen.blit(fullScreen_menu_text, (WIDTH // 2 - fullScreen_menu_text.get_width() // 2, 550))
        screen.blit(audio_menu_text, (WIDTH // 2 - audio_menu_text.get_width() // 2, 570))

        if audio_played and time.time() - start_time >= 2:
            show_round_screen = True
            round_start_time = time.time()
            game_state = "round"

    elif game_state == "round":
        if show_round_screen:
            round_screen = pygame.Surface((WIDTH, HEIGHT))
            round_screen.fill((0, 0, 0))
            round_image = pygame.image.load(ROUND_IMAGE)
            round_image = pygame.transform.scale(round_image, (400, 400))
            round_screen.blit(round_image, (WIDTH // 2 - round_image.get_width() // 2, HEIGHT // 2 - round_image.get_height() // 2))
            screen.blit(round_screen, (0, 0))

            if time.time() - round_start_time >= 3:
                show_round_screen = False
                game_state = "game"

    elif game_state == "game":
        if rotate_sprite:
            if reverse_rotation:
                sprite_angle -= sprite_rotate_speed
                if sprite_angle < 0:
                    sprite_angle = 360
            else:
                sprite_angle += sprite_rotate_speed
                if sprite_angle >= 360:
                    sprite_angle = 0

        rotated_sprite = pygame.transform.rotate(sprite_image, sprite_angle)
        sprite_rect = rotated_sprite.get_rect(center=(player_x, player_y))
        screen.blit(rotated_sprite, sprite_rect.topleft)

    pygame.display.flip()

pygame.quit()
sys.exit()
