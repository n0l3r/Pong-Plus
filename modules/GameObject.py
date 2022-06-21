import pygame
from abc import ABC, abstractmethod

class GameObject(ABC):
    """
    Abstract Class untuk semua in-game object.
    Constructor mengambil satu argumen yaitu rect (pygame.Rect) dari objeknya
    Punya getter dan setter sendiri buat nentuin posisi (x,y).
    """

    all_objects = []

    def __init__(self, rect:pygame.Rect, has_images = True, has_sounds = True ) -> None:
        super().__init__()
        self.rect = rect
        # Float untuk presisi posisi
        self._x = float(rect.x)
        self._y = float(rect.y)
        self._width = float(rect.width)
        self._height = float(rect.height)

        self.has_image = has_images
        self.has_sounds = has_sounds

        # Store all instantiated game objects
        # self.all_objects.append(self)
        
        # Modifiers for effects
        self.modifiers_timer = {
            "shrink" : {"start" : 0, "end" : 0}, 
            "expand" : {"start" : 0, "end" : 0}, 
            "speed_up" : {"start" : 0, "end" : 0}, 
            "striketrough" : {"start" : 0, "end" : 0}
        }
        
        self.modifiers_active = {
            "shrink" : False, 
            "expand" : False, 
            "speed_up" : False, 
            "striketrough" : False
        }

    @abstractmethod
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


    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, val):
        self._width = val
        self.rect.width = int(self._width)


    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, val):
        self._height = val
        self.rect.height = int(self._height)


    # Modifiers tags (name) untuk pengecekan modfier =====================================
    def add_modifier(self, modifier):
        # Set modifier to active
        if not self.check_modifier(modifier["name"]):
            self.modifiers_active[modifier["name"]] = True

        # Reset time
        current_time = pygame.time.get_ticks()//1000
        self.modifiers_timer[modifier["name"]]["start"] = current_time
        self.modifiers_timer[modifier["name"]]["end"] = modifier["duration"] + current_time


    def remove_modifier(self, modifier_tag:str):
        if self.check_modifier(modifier_tag):
            self.modifiers_active[modifier_tag] = False


    def check_modifier(self, modifier_tag:str):
        # Periksa jika objek memiliki modifier yang ditentukan
        return self.modifiers_active[modifier_tag]


    def handle_modifiers(self):
        pass
    # =====================================================================================
