import pygame
import constants
from player import Player
from obstacle import Obstacle
from background import Background
from title_screen import TitleScreen

pygame.init()
screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
pygame.display.set_caption("Legends of The Elemental Isles")

# Create objects
background = Background()
player = Player(50, constants.GROUND_Y - constants.PLAYER_RADIUS)
obstacle = Obstacle(
    constants.SCREEN_WIDTH, constants.GROUND_Y - constants.OBSTACLE_RADIUS
)
title_screen = TitleScreen()

game_state = "title"

clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break  # Exit the event loop immediately to prevent further processing

        if game_state == "title":
            if event.type == pygame.MOUSEBUTTONDOWN:
                game_state = "game"

    if game_state == "title":
        title_screen.draw(screen)
    elif game_state == "game":
        keys = pygame.key.get_pressed()
        player.handle_input(keys)
        player.apply_gravity()

        obstacle.update()
        obstacle.check_collision(player)

        background.update(keys)

        background.draw(screen)
        player.draw(screen)
        obstacle.draw(screen)

    pygame.display.update()
    clock.tick(60)

pygame.quit()
