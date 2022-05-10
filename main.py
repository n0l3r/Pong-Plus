import pygame
from modules import Menu
from modules import Board
from modules.Paddle import Paddle

pygame.init()
SIZE = (1280, 720)
icon = pygame.image.load("assets/images/icon.png")
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("Pong Plus")
pygame.display.set_icon(icon)

def main_menu():
    PLAY = True
    page_menu = "main_menu"

    main_menu = Menu.Main()
    main_menu.render(screen)
    play_menu = Menu.Play()
    about_menu = Menu.About("assets/images/about_text.png")
    info_menu = Menu.About("assets/images/info_text.png")
    
    menu_dict = {
        "main_menu":main_menu,
        "play_menu":play_menu,
        "about_menu":about_menu,
        "info_menu":info_menu
    }

    # kecepatan bola (bisa dirubah)
    game_diff = {"play_easy":1, "play_medium":2, "play_hard":3}

    while PLAY:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                # Menu button clicks
                page_menu = Menu.change_menu(menu_dict, page_menu, screen)

                if page_menu == "<exit>": 
                    PLAY = False
                    break

                if page_menu in game_diff:
                    game_play(game_diff[page_menu], menu_dict["play_menu"].max_score)

            menu_dict[page_menu].render(screen)
               
        pygame.display.update()

    pygame.quit()

def game_play(diff, max_score):

    screen.fill((0,0,0))
    board = Board.Board()
    board.render(screen)
    # Test speed 7
    gameScreen = pygame.Surface([1091,601], pygame.SRCALPHA, 32)
    gameScreen = gameScreen.convert_alpha()
    paddles = [paddle_left, paddle_right] = [Paddle(0, board, 7), Paddle(1, board, 7)]

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            # Keydown
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    paddle_left.speed -= paddle_left.base_speed
                elif event.key == pygame.K_s:
                    paddle_left.speed += paddle_left.base_speed

                if event.key == pygame.K_UP:
                    paddle_right.speed -= paddle_right.base_speed
                elif event.key == pygame.K_DOWN:
                    paddle_right.speed += paddle_right.base_speed

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    paddle_left.speed += paddle_left.base_speed
                elif event.key == pygame.K_s:
                    paddle_left.speed -= paddle_left.base_speed
                    
                if event.key == pygame.K_UP:
                    paddle_right.speed += paddle_right.base_speed
                elif event.key == pygame.K_DOWN:
                    paddle_right.speed -= paddle_right.base_speed

        screen.fill(pygame.Color(0,0,0,0))
        gameScreen.fill(pygame.Color(0,0,0,0))
        # board.render(screen)
        board.score_render(screen)

        for i in paddles:
            i.render(gameScreen)

        # pygame.draw.rect(gameScreen, (0,255,0), [0, 0, board.width, board.height], 1) # for debugging

        screen.blit(gameScreen, [board.x + 30, board.y + 30])

        pygame.display.flip()


if __name__ == "__main__":
    main_menu()

