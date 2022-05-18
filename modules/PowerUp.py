import pygame
from abc import abstractmethod
from modules.GameObject import GameObject

class PowerUp(GameObject):
    def __init__(self, rect: pygame.Rect, has_images=True, has_sounds=True) -> None:
        super().__init__(rect, has_images, has_sounds)

    @abstractmethod
    def effect(self):
        pass

class SpeedUp(PowerUp):
    def __init__(self, size, pos_x, pos_y, lifetime, duration):
        super().__init__(size, pos_x, pos_y, lifetime, duration)

    def effect(self):
        pass

    def show_icon(self):
        pass

class Striketrough(PowerUp):
    def __init__(self, size, pos_x, pos_y, lifetime, duration):
        super().__init__(size, pos_x, pos_y, lifetime, duration)

    def effect(self):
        pass

    def show_icon(self):
        pass

class Expand(PowerUp):
    def __init__(self, size, pos_x, pos_y, lifetime, duration):
        super().__init__(size, pos_x, pos_y, lifetime, duration)

    def effect(self):
        pass

    def show_icon(self):
        pass

class Shrink(PowerUp):
    def __init__(self, size, pos_x, pos_y, lifetime, duration):
        super().__init__(size, pos_x, pos_y, lifetime, duration)

    def effect(self):
        pass

    def show_icon(self):
        pass