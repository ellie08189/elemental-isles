# Screen
import pygame


SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800
# Colors
BACKGROUND = (189, 244, 250)
GROUND_COLOR = (72, 201, 32)
PLAYER_COLOR = (255, 0, 0)
OBSTACLE_COLOR = (0, 0, 255)
# Player settings
PLAYER_RADIUS = 50
PLAYER_SPEED = 5
JUMP_STRENGTH = -25
GRAVITY = 1
# Ground
GROUND_Y = 750
# Obstacle settings
OBSTACLE_RADIUS = 50
OBSTACLE_SPEED = -5

# background settings
BACKGROUND_IMAGE = "assets/forest.png"
BACKGROUND_SPEED = 5
BACKGROUND_ACTIVE = True

# title settings
TITLE_IMAGE = "assets/title_screen.png"
TITLE_POSITION = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
TITLE_ACTIVE = True

# game over settings
GAME_OVER_IMAGE = "assets/game_over.png"
GAME_OVER_POSITION = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
GAME_OVER_ACTIVE = True

# map settings
MAP_IMAGE = "assets/treasure_map.jpg"
MAP_POSITION = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

# sprite settings
WALK = [pygame.image.load(f"assets/walk{i}.png") for i in range(1, 9)]
