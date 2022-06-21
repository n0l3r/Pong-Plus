# Modules
import pygame
import random
from modules import Menu
from modules import Board
from modules import PowerUp
from modules.Paddle import Paddle
from modules.Ball import Ball
from modules.Player import Player
from modules.Loader import Loader


# PYGAME INIT
pygame.init()

# Display Setting
SIZE = (1280, 720)
icon = pygame.image.load("assets/images/icon.png")
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("Pong Plus")
pygame.display.set_icon(icon)

# Loaders
loader = Loader()
menu_dict = loader.load_menu()
game_dict = {}
items_list = [PowerUp.SpeedUp, PowerUp.Striketrough, PowerUp.Expand, PowerUp.Shrink]


# Menu loop
def menu_loop():
    current_menu = "main_menu"

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                # Menu button clicks
                current_menu = Menu.change_menu(menu_dict, current_menu, screen)

                # Exit menu
                if current_menu not in menu_dict: 
                    return current_menu

            # Render menu
            menu_dict[current_menu].render(screen)
               
        pygame.display.update()


# Pause menu
def pause_loop():
    pass


# Summon PowerUp acak pada koordinat acak
def spawn_item(active_items_list):
    item_idx = random.randint(0, 3)
    item_rnd = items_list[item_idx](random.randint(445, 645), random.randint(100, 501))

    while True:
        for i in active_items_list:
            if(item_rnd.rect.colliderect(i.rect)):
                item_rnd.x = random.randint(445, 645)
                item_rnd.y = random.randint(100, 501)
                break
        else:
            break

    active_items_list.append(item_rnd)


# Mengurus rendering PowerUp dan check collision dengan bola
def item_handler(active_items_list, screen, ball, paddle_right, paddle_left):
    new_list = []

    for item in active_items_list:
        item.render(screen)

        if ball.rect.colliderect(item.rect):
            if item.item_id == 0 or item.item_id == 1: # speed_up / striketrough
                item.give_effect(ball)

            if item.item_id == 2: # expand
                item.give_effect(paddle_left if ball.vec_x > 0 else paddle_right)

            if item.item_id == 3: # shrink
                item.give_effect(paddle_left if ball.vec_x < 0 else paddle_right)

        else:
            new_list.append(item)
    
    return new_list # Kembalikan list baru yang berisi item yang belum ditabrak bola


# Gameplay loop
def game_loop(difficulty, max_score):
    BALL_BASE_SPEED = (difficulty + 1)*2
    game_dict = loader.load_game(BALL_BASE_SPEED)

    board = game_dict["board"]
    ball = game_dict["ball"]
    paddle_left = game_dict["paddle_left"]
    paddle_right = game_dict["paddle_right"]
    player_left = game_dict["player_left"]
    player_right = game_dict["player_right"]
    
    active_item_list = []
    can_spawn_item = False

    # Reset screen
    screen.fill((0,0,0))

    # Render board
    screen_cpy = screen.copy()
    board.render(screen_cpy) # board di render ke copy dari screen utk mengurangi lag
    pygame.display.flip()

    # Screen baru untuk game
    game_screen = pygame.Surface([1091,601], pygame.SRCALPHA, 32).convert_alpha()
    game_dict["game_music"].set_volume(0.1)
    game_dict["game_music"].play(-1)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "<exit>"

            paddle_left.control(event)
            paddle_right.control(event)

        # Reset screen / render score
        game_screen.fill(pygame.Color(0,0,0,0))
        screen.fill(pygame.Color(0,0,0,0))
        screen.blit(screen_cpy, [0, 0])
        board.score_render(screen)

        # Gerakan objek game
        paddle_left.move(0, 601)
        paddle_right.move(0, 601)
        ball.move()

        # Render objek game
        paddle_left.render(game_screen)
        paddle_right.render(game_screen)
        ball.render(game_screen)

        # Summon item setiap 5 detik
        current_time = pygame.time.get_ticks() - board.timer.start_time
        summon_interval = 5000

        if current_time % summon_interval > 2000 and current_time > 1000:
            can_spawn_item = True

        if can_spawn_item and current_time % summon_interval < 1000 and len(active_item_list) <= 3:
            spawn_item(active_item_list)
            can_spawn_item = False

        # Tampilkan Item, cek collision dengan bola, dan perbarui list item aktif jika collision terjadi
        active_item_list = item_handler(active_item_list, game_screen, ball, paddle_right, paddle_left)

        # Jalankan efek item/powerup
        paddle_left.handle_modifiers()
        paddle_right.handle_modifiers()
        ball.handle_modifiers()
                
        # Reset bola jika skor didapatkan
        if ball.rect.centerx < 0:
            ball = Ball(ball.image, 545, 300, (difficulty + 1)*2, 180)
            player_right.update_score()
            board.score_boxes[1].set_value(player_right.score)

        if ball.rect.centerx > 1096:
            ball = Ball(ball.image, 545, 300, (difficulty + 1)*2, 0)  
            player_left.update_score()
            board.score_boxes[0].set_value(player_left.score)

        # Cek utk menentukan pantulan bola
        ball.bounce_check(0, 601, paddle_left, paddle_right)

        screen.blit(game_screen, [board.x + 30, board.y + 30])
        pygame.display.update([board.x, 0, board.width + 55, SIZE[1]])

        # Sementara exit setelah menang (Nanti diubah ketika halaman pemenang sudah dibuat)
        if player_left.score >= max_score or player_right.score >= max_score:
            return "<exit>"


# Page pemenang game
def winner_page():
    pass


# Main function
def main():
    current_loop = "menu"

    while True:
        if current_loop == "menu":
            current_loop = menu_loop()

        if current_loop == "<in-game>":
            current_loop = game_loop(menu_dict["play_menu"].difficulty, menu_dict["play_menu"].max_score)

        if current_loop == "<exit>":
            break

    pygame.quit()

if __name__ == "__main__":
    main()
