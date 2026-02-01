"""all screen classes for different game states"""

import pygame
import constants


class TitleScreen:
    """manages title screen"""

    def __init__(self):
        original_image = pygame.image.load(constants.TITLE_IMAGE)
        self.image = pygame.transform.scale(
            original_image, (original_image.get_width(), constants.SCREEN_HEIGHT)
        )

    def draw(self, screen):
        """draws title screen image"""
        screen.blit(
            self.image,
            (
                constants.TITLE_POSITION[0] - self.image.get_width() // 2,
                constants.TITLE_POSITION[1] - self.image.get_height() // 2,
            ),
        )


class PlayButton:
    """manages play button"""

    def __init__(self):
        original_image = pygame.image.load(constants.PLAY_BUTTON)
        self.image = pygame.transform.scale(original_image, (300, 300))

    def draw(self, screen):
        """draws play button on the screen"""
        screen.blit(
            self.image,
            (
                constants.SCREEN_WIDTH // 2 - self.image.get_width() // 2,
                constants.SCREEN_HEIGHT // 2 - self.image.get_height() // 2,
            ),
        )


class GameOver:
    """manages game over screen"""

    def __init__(self):
        original_image = pygame.image.load(constants.GAME_OVER_IMAGE)
        self.image = pygame.transform.scale(
            original_image, (original_image.get_width(), constants.SCREEN_HEIGHT)
        )

    def draw(self, screen):
        """draws game over screen image"""
        screen.blit(
            self.image,
            (
                constants.GAME_OVER_POSITION[0] - self.image.get_width() // 2,
                constants.GAME_OVER_POSITION[1] - self.image.get_height() // 2,
            ),
        )


class MapScreen:
    """manages map screen"""

    def __init__(self):
        original_image = pygame.image.load(constants.MAP_IMAGE)
        self.image = pygame.transform.scale(
            original_image, (constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT)
        )

    def draw(self, screen):
        """draws map screen image"""
        screen.blit(
            self.image,
            (
                constants.MAP_POSITION[0] - self.image.get_width() // 2,
                constants.MAP_POSITION[1] - self.image.get_height() // 2,
            ),
        )


class PauseScreen:
    """manages pause screen"""

    def __init__(self):
        original_image = pygame.image.load(constants.PAUSE_IMAGE)
        self.image = pygame.transform.scale(
            original_image, (constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT)
        )

    def draw(self, screen):
        """draws pause screen image"""
        screen.blit(
            self.image,
            (
                constants.PAUSE_POSITION[0] - self.image.get_width() // 2,
                constants.PAUSE_POSITION[1] - self.image.get_height() // 2,
            ),
        )
