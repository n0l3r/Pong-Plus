# Modules
import pygame
from modules import Menu
from modules import Board
from modules.Paddle import Paddle
from modules.Ball import Ball
from modules.Player import Player

# PYGAME INIT
pygame.init()

# Display Setting
SIZE = (1280, 720)
icon = pygame.image.load("assets/images/icon.png")
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("Pong Plus")
pygame.display.set_icon(icon)

# Main menu Function
def main_menu():
    PLAY = True
    page_menu = "main_menu"

    main_menu = Menu.Main()
    main_menu.render(screen)
    play_menu = Menu.Play()
    about_menu = Menu.About("assets/images/about_text.png")
    info_menu = Menu.About("assets/images/info_text.png")
    
    # Dictionary menu
    menu_dict = {
        "main_menu":main_menu,
        "play_menu":play_menu,
        "about_menu":about_menu,
        "info_menu":info_menu
    }

    # Kecepatan bola berdasarkan difficulty yang dipilih
    game_diff = {"play_easy":5, "play_medium":10, "play_hard":15}

    # Main Loop
    while PLAY:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                # Menu button clicks
                page_menu = Menu.change_menu(menu_dict, page_menu, screen)
                # Load selected menu
                if page_menu == "<exit>": 
                    PLAY = False
                    break

                # Cek jika game dimulai
                if page_menu in game_diff:
                    game_play(game_diff[page_menu], menu_dict["play_menu"].max_score)

            # Render menu
            menu_dict[page_menu].render(screen)
               
        pygame.display.update()
    pygame.quit()

# Funtion untuk main
def game_play(diff, max_score):
    # Reset screen
    screen.fill((0,0,0))

    # Board render
    board = Board.Board()
    board.render(screen)

    pygame.display.flip()

    # New screen untuk boards
    gameScreen = pygame.Surface([1091,601], pygame.SRCALPHA, 32)
    gameScreen = gameScreen.convert_alpha()

    # Paddles kanan dan kiri
    paddles = [paddle_left, paddle_right] = [Paddle(0, board, 7), Paddle(1, board, 7)]
    
    # Bola
    ball_img = pygame.image.load("assets/game_board/Ball-Reacr.png")
    ball = Ball(ball_img, diff, 0, 545, 300)

    # Player
    player_1 = Player(0)
    player_2 = Player(1)

    # loop in-game
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            # Check Keydown
            if event.type == pygame.KEYDOWN:
                # Kontrol paddle kiri
                if event.key == pygame.K_w:
                    paddle_left.speed -= paddle_left.base_speed
                elif event.key == pygame.K_s:
                    paddle_left.speed += paddle_left.base_speed

                # Kontrol paddle kanan
                if event.key == pygame.K_UP:
                    paddle_right.speed -= paddle_right.base_speed
                elif event.key == pygame.K_DOWN:
                    paddle_right.speed += paddle_right.base_speed

            # Check keyup
            if event.type == pygame.KEYUP:
                # Kontrol paddle kiri
                if event.key == pygame.K_w:
                    paddle_left.speed += paddle_left.base_speed
                elif event.key == pygame.K_s:
                    paddle_left.speed -= paddle_left.base_speed
                    
                # Kontrol paddle kiri
                if event.key == pygame.K_UP:
                    paddle_right.speed += paddle_right.base_speed
                elif event.key == pygame.K_DOWN:
                    paddle_right.speed -= paddle_right.base_speed

        # Rendering
        screen.fill(pygame.Color(0,0,0,0))
        gameScreen.fill(pygame.Color(0,0,0,0))
        board.render(screen)
        board.score_render(screen)

        for i in paddles:
            i.render(gameScreen)

        # pygame.draw.rect(gameScreen, (0,255,0), [0, 0, board.width, board.height], 1) # for debugging

        # gerakan bola
        ball.move()
        ball.render(gameScreen)

        # Cek collision bola dengan tembok kiri
        if ball.rect.left <= 0:
            ball.x = 545
            ball.y = 300
            ball.vec_x = -diff
            ball.vec_y = 0

            # Tambahan skor untuk player
            player_2.update_score()
            board.score_boxes[1].set_value(player_2.score)
            board.score_render(screen)
        
        # Cek collision bola dengan tembok kanan
        elif ball.rect.right >= 1096:
            ball.x = 545
            ball.y = 300
            ball.vec_x = diff
            ball.vec_y = 0

            # Tambahan skor untuk player
            player_1.update_score()
            board.score_boxes[0].set_value(player_1.score)
            board.score_render(screen)

        # Cek collision bola dengan tembok atas dan bawah
        if ball.rect.top <= 0 or ball.rect.bottom >= 601:
            ball.bounce(0)

        # Cek collision bola dengan paddle
        if ball.rect.colliderect(paddle_left.rect):
            ball.bounce(1, paddle_left)
        elif ball.rect.colliderect(paddle_right.rect):
            ball.bounce(1, paddle_right)


        screen.blit(gameScreen, [board.x + 30, board.y + 30])
        pygame.display.update([board.x, 0, board.width + 55, SIZE[1]])


if __name__ == "__main__":
    main_menu()

