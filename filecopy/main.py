"""game"""

import pygame
from player import Player
from obstacle import Obstacle
from background import Background
from title_screen import TitleScreen
from game_over import GameOver
import constants

pygame.init()
screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
pygame.display.set_caption("Legends of The Elemental Isles")

# Give the window time to initialize and gain focus
pygame.time.wait(100)
pygame.event.clear()  # Clear any events that happened during initialization

# Create objects
background = Background()
player = Player(50, constants.GROUND_Y - constants.PLAYER_RADIUS)
obstacle = Obstacle(
    constants.SCREEN_WIDTH, constants.GROUND_Y - constants.OBSTACLE_RADIUS
)
title_screen = TitleScreen()
game_over = GameOver()

game_state = "title"

clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break  # Exit the event loop immediately to prevent further processing

        if game_state == "title":
            if event.type == pygame.MOUSEBUTTONUP:
                game_state = "game"

        elif game_state == "game":
            if obstacle.active == False:
                game_state = "game_over"

    if game_state == "title":
        title_screen.draw(screen)
    elif game_state == "game":
        keys = pygame.key.get_pressed()
        player.handle_input(keys)
        player.apply_gravity()

        obstacle.update()
        obstacle.check_collision(player)

        background.update(keys, player)

        background.draw(screen)
        player.draw(screen)
        obstacle.draw(screen)

    elif game_state == "game_over":
        game_over.draw(screen)
        mouse = pygame.mouse.get_pos()
        # Check if the mouse is within the specified range

        # FIX THIS GIRL :)
        if 260 <= mouse[0] <= 300 and 460 <= mouse[1] <= 500:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONUP:
                    game_state = "game"

    pygame.display.update()
    clock.tick(60)

pygame.quit()
