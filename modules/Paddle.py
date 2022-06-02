from modules.GameObject import GameObject
import pygame

# Neon pada image paddle
PADDLE_NEON = 15
PADDLE_BASE_HEIGHT = 170

class Paddle(GameObject):
    def __init__(self, side:bool, base_speed:int):
        self.side = side # 0 = kiri, 1 = kanan
        # Rect paddle
        super().__init__(pygame.rect.Rect(0, 0, 20, PADDLE_BASE_HEIGHT))
        self.image = "assets/game_board/paddle_1.png" if not side else "assets/game_board/paddle_2.png"
        self.image = pygame.image.load(self.image)
        self.image = pygame.transform.scale(self.image,[50, 200])

        self.x = (1041 if side else 30)
        self.y = 240
        self.base_speed = base_speed
        self.speed = 0 # Kecepatan paddle


    # Control gerakan paddle berdasarkan event
    def control(self, event):
        key_control = []

        if event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
            key_control = [
                [event.key == pygame.K_w, event.key == pygame.K_s], # Kontrol paddle kiri
                [event.key == pygame.K_UP, event.key == pygame.K_DOWN] # Kontrol paddle kanan
            ]

        # Check Keydown
        if event.type == pygame.KEYDOWN:
            # Mulai gerakan paddle
            if key_control[self.side][0]:
                self.speed = -self.base_speed # Ubah arah gerak keatas
            elif key_control[self.side][1]: 
                self.speed = self.base_speed # Ubah arah gerak kebawah
        
        # Check keyup
        if event.type == pygame.KEYUP:
            # Stop gerakan paddle
            if key_control[self.side][0] or key_control[self.side][1]:
                self.speed = 0 # Hentikan gerak


    def move(self, top_boundary, bottom_boundary):
        if self.rect.bottom >=  bottom_boundary and self.speed > 0:
            return
        
        if self.rect.top <= top_boundary and self.speed < 0:
            return

        self.y += self.speed

        if self.rect.bottom >  bottom_boundary:
            self.y -= self.rect.bottom - bottom_boundary
            return
        
        if self.rect.top < top_boundary:
            self.y -= self.rect.top - top_boundary
            return

    
    # Mengatur aktifasi/deaktifasi efek PowerUp objek
    def handle_modifiers(self):
        current_time = pygame.time.get_ticks()//1000
        expand_len = 50
        shrink_len = 50

        if self.check_modifier("expand"):
            if current_time > self.modifiers_timer["expand"]["end"]:
                self.height = PADDLE_BASE_HEIGHT
                self.image = pygame.transform.scale(self.image,[50, self.height + 30])
                self.remove_modifier("expand")

            elif self.height != PADDLE_BASE_HEIGHT + expand_len:
                self.height = PADDLE_BASE_HEIGHT + expand_len
                self.image = pygame.transform.scale(self.image,[50, self.height + 30])
                self.remove_modifier("shrink")

        if self.check_modifier("shrink"):
            if current_time > self.modifiers_timer["shrink"]["end"]:
                self.height = PADDLE_BASE_HEIGHT
                self.image = pygame.transform.scale(self.image,[50, self.height + 30])
                self.remove_modifier("shrink")
            
            elif self.height != PADDLE_BASE_HEIGHT - shrink_len:
                self.height = PADDLE_BASE_HEIGHT - shrink_len
                self.image = pygame.transform.scale(self.image,[50, self.height + 30])
                self.remove_modifier("expand")


    # Render function
    def render(self, screen:pygame.surface.Surface):
        screen.blit(self.image, [self.x - PADDLE_NEON, self.y - PADDLE_NEON])
        # pygame.draw.rect(screen, (255,0,0), self.rect) # for debugging