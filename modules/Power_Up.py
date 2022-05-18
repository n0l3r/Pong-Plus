from abc import ABC, abstractmethod

class Power_Up(ABC):
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

class SpeedUp(Power_Up):
    def __init__(self, size, pos_x, pos_y, lifetime, duration):
        super().__init__(size, pos_x, pos_y, lifetime, duration)

    def effect(self):
        pass

    def show_icon(self):
        pass

class Striketrough(Power_Up):
    def __init__(self, size, pos_x, pos_y, lifetime, duration):
        super().__init__(size, pos_x, pos_y, lifetime, duration)

    def effect(self):
        pass

    def show_icon(self):
        pass

class Expand(Power_Up):
    def __init__(self, size, pos_x, pos_y, lifetime, duration):
        super().__init__(size, pos_x, pos_y, lifetime, duration)

    def effect(self):
        pass

    def show_icon(self):
        pass

class Shrink(Power_Up):
    def __init__(self, size, pos_x, pos_y, lifetime, duration):
        super().__init__(size, pos_x, pos_y, lifetime, duration)

    def effect(self):
        pass

    def show_icon(self):
        pass