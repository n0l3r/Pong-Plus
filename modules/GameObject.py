import pygame, abc

class GameObject(pygame.sprite.Sprite):
    """
    Class (turunan dari pygame.sprite.Sprites) untuk semua in-game object.
    Constructor mengambil satu argumen yaitu rect (pygame.Rect) dari objeknya
    Punya getter dan setter sendiri buat nentuin posisi (x,y).
    """

    all_objects = []

    def __init__(self, rect:pygame.Rect, has_images = False, has_sounds = False ) -> None:
        super().__init__()
        self.rect = rect
        # Float untuk presisi posisi
        self._x = float(rect.x)
        self._y = float(rect.y)

        self.has_image = has_images
        self.has_sounds = has_sounds

        # Store all instantiated game objects
        # self.all_objects.append(self)

    @abc.abstractmethod
    def render(self, screen):
        pass
    
    
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
