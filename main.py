import pygame
from modules import Menu
from modules import Board
from modules.Paddle import Paddle
from modules.Ball import Ball
from modules.Player import Player

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
    game_diff = {"play_easy":5, "play_medium":10, "play_hard":15}

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
    
    ball_img = pygame.image.load("assets/game_board/Ball-Reacr.png")
    ball = Ball(ball_img, diff, diff, 545, 300)

    player_1 = Player(0)
    player_2 = Player(1)


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
        board.render(screen)
        board.score_render(screen)

        for i in paddles:
            i.render(gameScreen)

        pygame.draw.rect(gameScreen, (0,255,0), [0, 0, board.width, board.height], 1) # for debugging

        # gerakan bola
        ball.move()
        ball.render(gameScreen)

        if ball.rect.left <= 0:
            ball.pos_x = 545
            ball.pos_y = 300

            player_2.update_score()
            board.score_boxes[1].set_value(player_2.score)
            board.score_render(screen)
        
        elif ball.rect.right >= 1096:
            ball.pos_x = 545
            ball.pos_y = 300

            player_1.update_score()
            board.score_boxes[0].set_value(player_1.score)
            board.score_render(screen)

        if ball.rect.top <= 0 or ball.rect.bottom >= 601:
            ball.bounce(0)

        if ball.rect.colliderect(paddle_left.rect):
            ball.bounce(1, paddle_left)

        elif ball.rect.colliderect(paddle_right.rect):
            ball.bounce(1, paddle_right)


        screen.blit(gameScreen, [board.x + 30, board.y + 30])

        pygame.display.flip()


if __name__ == "__main__":
    main_menu()

