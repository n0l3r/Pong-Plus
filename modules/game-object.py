import pygame

class Game_Object(pygame.sprite.Sprite):
    def __init__(self, rect:pygame.Rect ) -> None:
        super().__init__()
        self.rect = rect
        self._x = float(rect.x)
        self._y = float(rect.y)
    
    @property
    def x(self):
        return self._x
    @x.setter
    def x(self, val:float):
        self._x = val
        self.rect.x = int(self._x)
    @property
    def y(self):
        return self._y
    @y.setter
    def y(self, val:float):
        self._y = val
        self.rect.y = int(self._y)