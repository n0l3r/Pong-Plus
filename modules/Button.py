import pygame
class Button:
    def __init__(self, image:pygame.Surface, pos):
        self.image = image
        self.image.set_alpha(255)
        self.pos_x = pos[0]
        self.pos_y = pos[1]
        self.width = image.get_width() - 20
        self.height = image.get_height() - 20
        
    def render(self, screen):
        if self.check(pygame.mouse.get_pos()):
            self.image.set_alpha(100)
        else:
            self.image.set_alpha(255)
        screen.blit(self.image, (self.pos_x, self.pos_y))
    
    def check(self, mouse_pos):
        if pygame.Rect(self.pos_x+10, self.pos_y+5, self.width, self.height).collidepoint(mouse_pos):
            return True
        return False

