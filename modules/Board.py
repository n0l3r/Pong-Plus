import pygame
import sys # debugging

pygame.init()

# Rasterized neon size = 15px
BOARD_NEON = 15

class Board:
    # Board aspect ratio = 16 : 9
    # Board : Screen_area ratio = 7 : 8
    default_width = 1120
    default_height = 630
    def _init_(self):

        #    -> img_width / img_heigth adalah size dari GAMBAR board (tanpa size neon).
        #    -> width / height adalah area dalam board (inner board size) yang nanti
        #       jadi acuan WALL COLLISION. (disatukan dalam list size[width, height])

        # Size image board
        self.img_width = 1120
        self.img_height = 630

        # Posisi board + jarak shadow (neon)
        self.x = 80 - BOARD_NEON
        self.y = 67 - BOARD_NEON
        self.image = pygame.image.load("assets/game_board/Board-Stars.png")

        # Scale gambar jadi 1120+neon x 630+neon (1150 x 660)
        self.image = pygame.transform.scale(self.image, [self.img_width + 2*BOARD_NEON, self.img_height + 2*BOARD_NEON])
        
        # Size board di dalam untuk check collision (mantul)
        self.size = self.width,self.height = [1098, 608]
        
        # Scorebox boardnya
        self.score_boxes = [Scores(True, self), Scores(False, self)]
        
        # Timer diatas board
        self.timer = Timer(self)
    
    def render(self, screen):
        # Board (self)
        screen.blit(self.image, [self.x,self.y]) 
        
        # Score boxes
        self.score_boxes[0].render(screen)
        self.score_boxes[1].render(screen)
        
        # Timer
        self.timer.render(screen)