from abc import ABC, abstractmethod

class Item(ABC):
    def __init__(self, size, pos_x, pos_y, lifetime, duration):
        self.size = size
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.lifetime = lifetime
        self.duration = duration

    @abstractmethod
    def effect(self):
        pass

    @abstractmethod
    def show_icon(self):
        pass