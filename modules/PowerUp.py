import pygame
from abc import abstractmethod
from modules.GameObject import GameObject

class PowerUp(GameObject):
    def __init__(self,x, y) -> None:
        self.rect = pygame.Rect(x, y, 60, 60)
        super().__init__(self.rect, True, True)

    @abstractmethod
    def give_effect(self):
        pass

class SpeedUp(PowerUp):
    def __init__(self, x, y) -> None:
        super().__init__(x, y)

    def give_effect(self, ball):
        modifier = {
            "name": "speed_up",
            "duration": 15,
        }
        ball.add_modifiers(modifier)


class Striketrough(PowerUp):
    def __init__(self, x, y) -> None:
        super().__init__(x, y)

    def give_effect(self, ball):
        modifier = {
            "name": "striketrough",
            "duration": 15,
        }
        ball.add_modifiers(modifier)


class Expand(PowerUp):
    def __init__(self, x, y) -> None:
        super().__init__(x, y)

    def give_effect(self, player):
        modifier = {
            "name": "expand",
            "duration": 15,
        }
        player.add_modifiers(modifier)


class Shrink(PowerUp):
    def __init__(self, x, y) -> None:
        super().__init__(x, y)

    def give_effect(self, player):
        modifier = {
            "name": "shrink",
            "duration": 15,
        }
        player.add_modifiers(modifier)