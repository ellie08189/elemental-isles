"""Constant values for the game."""

import pygame

# screen
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
PLAY_BUTTON = "assets/play_button.png"

# game over settings
GAME_OVER_IMAGE = "assets/game_over.png"
GAME_OVER_POSITION = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
GAME_OVER_ACTIVE = True

# map settings
MAP_IMAGE = "assets/treasure_map.jpg"
MAP_POSITION = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

# Character settings
WALKING = [
    pygame.image.load(f"assets/walk{i}.png") for i in range(1, 9) for _ in range(5)
]
WALKBACK = [
    pygame.transform.flip(pygame.image.load(f"assets/walk{i}.png"), True, False)
    for i in range(1, 9)
    for _ in range(5)
]
IDLE = pygame.image.load("assets/idle1.png")
CHARACTER_HEIGHT = 105
CHARACTER_WIDTH = 72
POWERSPRITE = [
    pygame.image.load(f"assets/power{i}.png") for i in range(1, 3) for _ in range(5)
]
POWERSPRITE = [
    pygame.transform.scale(img, (CHARACTER_WIDTH, CHARACTER_HEIGHT))
    for img in POWERSPRITE
]

POWER_WIDTH = 100
POWER_HEIGHT = 55
POWER = [
    pygame.image.load(f"assets/water/water{i}.png")
    for i in range(1, 8)
    for _ in range(5)
]  # 600x320
POWER = [pygame.transform.scale(img, (POWER_WIDTH, POWER_HEIGHT)) for img in POWER]
POWER = [pygame.transform.flip(img, True, False) for img in POWER]
POWER_SPEED = 8

# pillar settings
PILLAR_IMAGE = "assets/pillar.png"
PILLAR_WIDTH = 80
PILLAR_HEIGHT = 150
PILLAR_SPEED = -5

# bush settings
BUSH1_WIDTH = 120
BUSH1_HEIGHT = 80
BUSH_IMAGES = [
    "assets/bush1.png",
    "assets/bush2.png",
    "assets/bush3.png",
    "assets/bush4.png",
]
BUSH1_IMAGE = pygame.image.load("assets/bush1.png")
BUSH1_IMAGE = pygame.transform.scale(BUSH1_IMAGE, (BUSH1_WIDTH, BUSH1_HEIGHT))
BUSH1_SPEED = -5

# fireball settings
FIREBALL_SPEED = -7
FIREBALL_WIDTH = 100
FIREBALL_HEIGHT = 55
FIREBALL_IMAGE = [
    pygame.image.load(f"assets/Fire Arrow/PNG/fireball{i}.png")
    for i in range(1, 8)
    for _ in range(5)
]  # 600x320
FIREBALL_IMAGE = [
    pygame.transform.scale(img, (FIREBALL_WIDTH, FIREBALL_HEIGHT))
    for img in FIREBALL_IMAGE
]


# log settings
LOG_WIDTH = 80
LOG_HEIGHT = 80
LOG_IMAGE = [
    pygame.image.load(f"assets/log{i}.png") for i in range(1, 4) for _ in range(5)
]
LOG_IMAGE = [pygame.transform.scale(img, (LOG_WIDTH, LOG_HEIGHT)) for img in LOG_IMAGE]
LOG_SPEED = -5

# key settings
KEY_IMAGE = "assets/key.png"
KEY_SPEED = -5
KEY_WIDTH = 40
KEY_HEIGHT = 40

# platforms settings
PLATFORM_IMAGES = [
    "assets/tree1.png",
    "assets/tree2.png",
    "assets/tree3.png",
]
PLATFORM_WIDTH = 155
PLATFORM_HEIGHT = 55

# sound settings
COLLECT_KEY_SOUND = "assets/sounds/coincollector1.wav"
MAIN_THEME_MUSIC = "assets/sounds/maingamemusic.wav"
