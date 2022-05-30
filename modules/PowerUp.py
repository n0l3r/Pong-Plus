import pygame
from abc import abstractmethod
from modules.GameObject import GameObject

class PowerUp(GameObject):
    def __init__(self, x, y, image:pygame.Surface = None) -> None:
        self.size = 60
        self.rect = pygame.Rect(x, y, self.size, self.size)
        
        self.image = image
        self.image = pygame.transform.scale(image, [self.size, self.size])

        super().__init__(self.rect, True, True)

    @abstractmethod
    def give_effect(self):
        pass

    def render(self, screen):
        screen.blit(self.image, (self.x, self.y))


class SpeedUp(PowerUp):
    def __init__(self, x, y) -> None:
        super().__init__(x, y)

    def give_effect(self, ball):
        ball.add_modifiers({
            "name": "speed_up",
            "duration": 15,
        })


class Striketrough(PowerUp):
    def __init__(self, x, y) -> None:
        super().__init__(x, y)

    def give_effect(self, ball):
        ball.add_modifiers({
            "name": "striketrough",
            "duration": 15,
        })


class Expand(PowerUp):
    def __init__(self, x, y) -> None:
        super().__init__(x, y)

    def give_effect(self, player):
        player.add_modifiers({
            "name": "expand",
            "duration": 15,
        })


class Shrink(PowerUp):
    def __init__(self, x, y) -> None:
        super().__init__(x, y)

    def give_effect(self, player):
        player.add_modifiers({
            "name": "shrink",
            "duration": 15,
        })