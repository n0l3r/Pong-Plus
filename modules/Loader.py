import pygame
from modules import Menu
from modules.Board import Board
from modules.Paddle import Paddle
from modules.Ball import Ball
from modules.Player import Player

class Loader:
    def load_menu(self):
        return {
            "main_menu": Menu.Main(),
            "about_menu": Menu.About("assets/images/about_text.png"),
            "info_menu": Menu.About("assets/images/info_text.png"),
            "play_menu": Menu.Play()
        }

    def load_game(self, difficulty,  ball_img = pygame.image.load("assets/game_board/Ball-React.png")):
        return {
            "board" : Board(),
            "paddle_left" : Paddle(0, 7),
            "paddle_right" : Paddle(1, 7),
            "ball" : Ball(ball_img, 545, 300, (difficulty + 1)*2, 0),
            "player_left" : Player(0),
            "player_right" : Player(1)
        }