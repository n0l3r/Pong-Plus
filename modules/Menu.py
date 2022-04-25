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
    def __init__(self, text_img_path):
        self.text_img_path = text_img_path
        super().__init__("about_menu")

    def render(self, screen):
        screen.fill(MENU_BG)

        logo_pbb = pygame.image.load("assets/images/logo_pbb.png")
        logo_pbb.set_alpha(255)
        screen.blit(logo_pbb, (15, 15))

        logo_img = pygame.image.load("assets/images/Pong_Logo.png")
        logo_img.set_alpha(255)
        screen.blit(logo_img, (494, 173))
        
        about_text = pygame.image.load(self.text_img_path)
        about_text.set_alpha(255)
        screen.blit(about_text, (215, 125))

        back_img = pygame.image.load("assets/button/back_btn.png")
        self.back_btn = Button(image=back_img, pos=(505, 575))
        self.back_btn.render(screen)

class Play(Menu):
    def __init__(self):
        super().__init__("play_menu")

    def render(self, screen):
        screen.fill(MENU_BG)

        logo_pbb = pygame.image.load("assets/images/logo_pbb.png")
        logo_pbb.set_alpha(255)
        screen.blit(logo_pbb, (15, 15))   

        easy_img = pygame.image.load("assets/button/easy_btn.png")
        self.easy_btn = Button(image=easy_img, pos=(505, 203))
        self.easy_btn.render(screen)

        medium_img = pygame.image.load("assets/button/medium_btn.png")
        self.medium_btn = Button(image=medium_img, pos=(505, 268))
        self.medium_btn.render(screen)

        hard_img = pygame.image.load("assets/button/hard_btn.png")
        self.hard_btn = Button(image=hard_img, pos=(505, 333))
        self.hard_btn.render(screen)

        score_img = pygame.image.load("assets/images/score_text.png")
        score_img.set_alpha(255)
        screen.blit(score_img, (494, 422))

        increase_img = pygame.image.load("assets/button/increase_btn.png")
        self.increase_btn = Button(image=increase_img, pos=(734, 426))
        self.increase_btn.render(screen)

        decrease_img = pygame.image.load("assets/button/decrease_btn.png")
        self.decrease_btn = Button(image=decrease_img, pos=(728, 450))
        self.decrease_btn.render(screen)


        back_img = pygame.image.load("assets/button/back_btn.png")
        self.back_btn = Button(image=back_img, pos=(505, 575))
        self.back_btn.render(screen)


       

        