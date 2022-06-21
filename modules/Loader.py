import pygame
import random
from modules import Menu
from modules.Board import Board
from modules.Paddle import Paddle
from modules.Ball import Ball
from modules.Player import Player

class Loader:
    @staticmethod
    def load_menu():
        return {
            "main_menu": Menu.Main(),
            "about_menu": Menu.About("assets/images/about_text.png"),
            "info_menu": Menu.About("assets/images/info_text.png"),
            "play_menu": Menu.Play()
        }

    @staticmethod
    def load_game(ball_speed,  ball_img = pygame.image.load("assets/game_board/ball_react.png")):
        return {
            "board" : Board(),
            "paddle_left" : Paddle(0, 7),
            "paddle_right" : Paddle(1, 7),
            "ball" : Ball(ball_img, 545, 300, ball_speed, int(random.choice([0, 180]))),
            "player_left" : Player(0),
            "player_right" : Player(1),
            "game_music": pygame.mixer.Sound("assets/sounds/play_board.wav"),
            "winner_music": pygame.mixer.Sound("assets/sounds/winner.wav")
        }