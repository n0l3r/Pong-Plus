import pygame, abc

class GameObject(abc.ABC):
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
        self.modifiers = []

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


    # Modifiers tags (name) untuk pengecekan modfier =======================
    @property
    def modifier_tags(self):
        return list(i["name"] for i in self.modifiers)


    def add_modifiers(self, modifier):
        # If already have the modifiers, reset time
        if modifier["name"] in self.modifier_tags:
            self.modifiers[self.modifiers.index(modifier)]["duration"] = 15
        # else, add the modifiers
        else:
            self.modifiers.append(modifier)


    def remove_modifiers(self, modifier):
        if modifier["name"] in self.modifier_tags:
            self.modifiers.pop(self.modifiers.index(modifier))


    def check_modifier(self, modifier_tag:str):
        """Periksa jika bola memiliki modifier yang ditentukan."""
        return modifier_tag in self.modifier_tags
    # ======================================================================