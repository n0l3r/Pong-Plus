# Modules
import pygame
from modules import Menu
from modules import Board
from modules.Paddle import Paddle
from modules.Ball import Ball
from modules.Player import Player
from modules.Loader import Loader


# PYGAME INIT
pygame.init()

# Display Setting
SIZE = (1280, 720)
icon = pygame.image.load("assets/images/icon.png")
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("Pong Plus")
pygame.display.set_icon(icon)

# Loaders
loader = Loader()
menu_dict = loader.load_menu()
game_dict = {}


# Menu loop
def menu_loop():
    current_menu = "main_menu"

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                # Menu button clicks
                current_menu = Menu.change_menu(menu_dict, current_menu, screen)

                # Exit menu
                if current_menu not in menu_dict: 
                    return current_menu

            # Render menu
            menu_dict[current_menu].render(screen)
               
        pygame.display.update()


# Pause menu
def pause_loop():
    pass


# Gameplay loop
def game_loop(difficulty, max_score):
    game_dict = loader.load_game(difficulty)

    board = game_dict["board"]
    ball = game_dict["ball"]
    paddle_left = game_dict["paddle_left"]
    paddle_right = game_dict["paddle_right"]
    player_left = game_dict["player_left"]
    player_right = game_dict["player_right"]

    # Reset screen
    screen.fill((0,0,0))

    # Render board
    screen_cpy = screen.copy()
    board.render(screen_cpy) # board di render ke copy dari screen utk mengurangi lag
    pygame.display.flip()

    # Screen baru untuk game
    game_screen = pygame.Surface([1091,601], pygame.SRCALPHA, 32).convert_alpha()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "<exit>"

            # Check Keydown
            if event.type == pygame.KEYDOWN:
                # Kontrol paddle kiri
                if event.key == pygame.K_w:
                    paddle_left.go_up()
                elif event.key == pygame.K_s:
                    paddle_left.go_down()

                # Kontrol paddle kanan
                if event.key == pygame.K_UP:
                    paddle_right.go_up()
                elif event.key == pygame.K_DOWN:
                    paddle_right.go_down()

            # Check keyup
            if event.type == pygame.KEYUP:
                # Kontrol paddle kiri
                if event.key == pygame.K_w or event.key == pygame.K_s:
                    paddle_left.stop()
                    
                # Kontrol paddle kiri
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    paddle_right.stop()

        # Reset screen / render score
        game_screen.fill(pygame.Color(0,0,0,0))
        screen.fill(pygame.Color(0,0,0,0))
        screen.blit(screen_cpy, [0, 0])
        board.score_render(screen)

        # Gerakan objek game
        paddle_left.move(0, 601)
        paddle_right.move(0, 601)
        ball.move()

        # Render objek game
        paddle_left.render(game_screen)
        paddle_right.render(game_screen)
        ball.render(game_screen)
                
        # Reset bola jika skor didapatkan
        if ball.rect.centerx < 0:
            ball = Ball(ball.image, 545, 300, (difficulty + 1)*2, 180)
            player_right.update_score()
            board.score_boxes[1].set_value(player_right.score)

        if ball.rect.centerx > 1096:
            ball = Ball(ball.image, 545, 300, (difficulty + 1)*2, 0)  
            player_right.update_score()
            board.score_boxes[1].set_value(player_right.score)

        # Cek utk menentukan pantulan bola
        ball.bounce_check(0, 601, paddle_left, paddle_right)

        screen.blit(game_screen, [board.x + 30, board.y + 30])
        pygame.display.update([board.x, 0, board.width + 55, SIZE[1]])

        # Sementara exit setelah menang (Nanti diubah ketika halaman pemenang sudah dibuat)
        if player_left.score >= max_score or player_right.score >= max_score:
            return "<exit>"


# Page pemenang game
def winner_loop():
    pass


# Main function
def main():
    current_loop = "menu"

    while True:
        if current_loop == "menu":
            current_loop = menu_loop()

        if current_loop == "<in-game>":
            current_loop = game_loop(menu_dict["play_menu"].difficulty, menu_dict["play_menu"].max_score)

        if current_loop == "<exit>":
            break

    pygame.quit()

if __name__ == "__main__":
    main()