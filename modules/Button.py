import pygame
class Button:
    def __init__(self, image, pos):
        self.image = image
        self.image.set_alpha(255)
        self.pos_x = pos[0]
        self.pos_y = pos[1]
        
    def render(self, screen):
        screen.blit(self.image, (self.pos_x, self.pos_y))
    
    def check(self, mouse_pos):
        rect = pygame.Rect(self.pos_x, self.pos_y, self.image.get_width(), self.image.get_height())
        return rect.collidepoint(mouse_pos)

