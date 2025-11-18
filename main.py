"""Main game loop for Legends of The Elemental Isles."""

# import necessary modules
import pygame
import constants
from player import Player
from obstacle import Obstacle
from background import Background
from title_screen import TitleScreen
from game_over import GameOver
from map_screen import MapScreen

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
        # switch between game states
        if game_state == "title":
            if event.type == pygame.MOUSEBUTTONDOWN:
                game_state = "game"
        elif game_state == "game":
            if obstacle.active == False:
                game_state = "game_over"
            if keys[pygame.K_m]:
                game_state = "map"
        elif game_state == "game_over":
            game_over.draw(screen)
            mouse = pygame.mouse.get_pos()
        elif game_state == "map":
            if keys[pygame.K_m]:
                game_state = "game"
        # error that any key pressed goes from map screen to game screen and map size is not right

    # calls appropriate methods based on game state
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

    elif game_state == "map":
        map_screen = MapScreen()
        map_screen.draw(screen)

    elif game_state == "game_over":
        game_over.draw(screen)
        mouse = pygame.mouse.get_pos()

        # Check if the mouse is within the specified range
        if 225 <= mouse[0] <= 335 and 460 <= mouse[1] <= 505:
            if event.type == pygame.MOUSEBUTTONUP:
                # Reset player and obstacle to restart the game
                player = Player(
                    constants.PLAYER_RADIUS,
                    constants.GROUND_Y - constants.PLAYER_RADIUS,
                )
                obstacle = Obstacle(
                    constants.SCREEN_WIDTH,
                    constants.GROUND_Y - constants.OBSTACLE_RADIUS,
                )
                obstacle.active = True  # Ensure the obstacle is active
                game_state = "game"

        # exits the game when no is clicked
        if 600 <= mouse[0] <= 680 and 460 <= mouse[1] <= 505:
            if event.type == pygame.MOUSEBUTTONUP:
                running = False
                break

    pygame.display.update()
    clock.tick(60)

pygame.quit()
