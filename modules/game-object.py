import pygame

class Game_Object(pygame.sprite.Sprite):
    """
    Class (turunan dari pygame.sprite.Sprites) untuk semua in-game object.
    Constructor mengambil satu argumen yaitu rect (pygame.Rect) dari objeknya
    Punya getter dan setter sendiri buat nentuin posisi (x,y).
    """
    def __init__(self, rect:pygame.Rect ) -> None:
        super().__init__()
        self.rect = rect
        # Float untuk presisi posisi
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