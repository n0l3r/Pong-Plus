import pygame
from modules import Menu

class Loader:
    def __init__(self) -> None:
        self.menu_assets_loaded = False
        self.game_assets_loaded = False

    def load_menu(self):
        main_menu = Menu.Main()
        about_menu = Menu.About("assets/images/about_text.png")
        info_menu = Menu.About("assets/images/info_text.png")
        play_menu = Menu.Play()

        self.menu_assets_loaded = True
        return {
            "main_menu": main_menu,
            "about_menu": about_menu,
            "info_menu": info_menu,
            "play_menu": play_menu
        }

    def load_game(self):
        pass