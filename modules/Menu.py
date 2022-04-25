from abc import ABC, abstractmethod
import pygame, sys
from modules.Button import Button

TITLE = "Pong Plus"

MENU_BG = (8, 32, 50)
GAME_BG = (1, 0, 6)
class Menu(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def render(self):
        pass


class Main(Menu):
    def __init__(self):
        super().__init__("main_menu")

    def render(self, screen):
        screen.fill(MENU_BG)

        logo_pbb = pygame.image.load("assets/images/logo_pbb.png")
        logo_pbb.set_alpha(255)
        screen.blit(logo_pbb, (15, 15))

        logo_img = pygame.image.load("assets/images/Pong_Logo.png")
        logo_img.set_alpha(255)
        screen.blit(logo_img, (494, 173))

        info_img = pygame.image.load("assets/button/info_btn.png")
        self.info_btn = Button(image=info_img, pos=(1220, 15))
        self.info_btn.render(screen)

        play_img = pygame.image.load("assets/button/play_btn.png")
        self.play_btn = Button(image=play_img, pos=(505, 400))
        self.play_btn.render(screen)

        about_img = pygame.image.load("assets/button/about_btn.png")
        self.about_btn = Button(image=about_img, pos=(505, 465))
        self.about_btn.render(screen)

        exit_img = pygame.image.load("assets/button/exit_btn.png")
        self.exit_btn = Button(image=exit_img, pos=(505, 530))
        self.exit_btn.render(screen)

        


class About(Menu):
    def __init__(self):
        super().__init__("about_menu")

    def render(self, screen):
        screen.fill(MENU_BG)

        logo_pbb = pygame.image.load("assets/images/logo_pbb.png")
        logo_pbb.set_alpha(255)
        screen.blit(logo_pbb, (15, 15))

        logo_img = pygame.image.load("assets/images/Pong_Logo.png")
        logo_img.set_alpha(255)
        screen.blit(logo_img, (494, 173))
        
        about_text = pygame.image.load("assets/images/about_text.png")
        about_text.set_alpha(255)
        screen.blit(about_text, (215, 125))

        back_img = pygame.image.load("assets/button/back_btn.png")
        self.back_btn = Button(image=back_img, pos=(505, 575))
        self.back_btn.render(screen)

class Info(Menu):
    def __init__(self):
        super().__init__("info_menu")

    def render(self, screen):
        screen.fill(MENU_BG)

        logo_pbb = pygame.image.load("assets/images/logo_pbb.png")
        logo_pbb.set_alpha(255)
        screen.blit(logo_pbb, (15, 15))

        logo_img = pygame.image.load("assets/images/Pong_Logo.png")
        logo_img.set_alpha(255)
        screen.blit(logo_img, (494, 173))

        info_text = pygame.image.load("assets/images/info_text.png")
        info_text.set_alpha(255)
        screen.blit(info_text, (215, 125))

        back_img = pygame.image.load("assets/button/back_btn.png")
        self.back_btn = Button(image=back_img, pos=(505, 575))
        self.back_btn.render(screen)


def change_menu(menu:dict, crnt_page:str, screen):
    # Main Menu Page
    if crnt_page == "main_menu":
        if menu["main_menu"].play_btn.check(pygame.mouse.get_pos()):
            return "play_menu"

        elif menu["main_menu"].about_btn.check(pygame.mouse.get_pos()):
            menu["about_menu"].render(screen)
            return "about_menu"

        elif menu["main_menu"].info_btn.check(pygame.mouse.get_pos()):
            menu["info_menu"].render(screen)
            return "info_menu"

        elif menu["main_menu"].exit_btn.check(pygame.mouse.get_pos()):
            return "<exit>"

    # About Menu
    elif crnt_page == "about_menu":
        if menu["about_menu"].back_btn.check(pygame.mouse.get_pos()):
            menu["main_menu"].render(screen)
            return "main_menu"

    # Info Menu
    elif crnt_page == "info_menu":
        if menu["info_menu"].back_btn.check(pygame.mouse.get_pos()):
            menu["main_menu"].render(screen)
            return "main_menu"