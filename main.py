import pygame
from modules import Menu
from modules import Board

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

    board = Board.Board()
    board.render(screen)

    while True:
        board.score_render(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        pygame.display.update()


if __name__ == "__main__":
    main_menu()

