import pygame
from abc import abstractmethod
from modules.GameObject import GameObject
from modules.Ball import Ball
from modules.Paddle import Paddle

class PowerUp(GameObject):
    def __init__(self, x, y, image:pygame.Surface = None) -> None:
        self.size = 100
        self.rect = pygame.Rect(x, y, self.size, self.size)
        
        self.image = image
        self.image = pygame.transform.scale(image, [self.size, self.size])

        super().__init__(self.rect, True, True)

    @abstractmethod
    def give_effect(self):
        pass

    def render(self, screen):
        screen.blit(self.image, (self.x, self.y))
        # pygame.draw.rect(screen, (255,0,0), self.rect) # for debugging


class SpeedUp(PowerUp):
    def __init__(self, x, y) -> None:
        self.item_id = 0
        super().__init__(x, y, pygame.image.load("assets/game_board/Item-SpeedUp.png"))

    def give_effect(self, ball):
        ball.add_modifier({
            "name": "speed_up",
            "duration": 5
        })


class Striketrough(PowerUp):
    def __init__(self, x, y) -> None:
        self.item_id = 1
        super().__init__(x, y, pygame.image.load("assets/game_board/Item-Striketrough.png"))

    def give_effect(self, ball):
        ball.add_modifier({
            "name": "striketrough",
            "duration": 5
        })


class Expand(PowerUp):
    def __init__(self, x, y) -> None:
        self.item_id = 2
        super().__init__(x, y, pygame.image.load("assets/game_board/Item-Expand.png"))

    def give_effect(self, paddle):
        paddle.add_modifier({
            "name": "expand",
            "duration": 5
        })


class Shrink(PowerUp):
    def __init__(self, x, y) -> None:
        self.item_id = 3
        super().__init__(x, y, pygame.image.load("assets/game_board/Item-Shrink.png"))

    def give_effect(self, paddle):
        paddle.add_modifier({
            "name": "shrink",
            "duration": 5
        })