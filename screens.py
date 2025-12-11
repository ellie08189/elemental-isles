import pygame
import constants


class TitleScreen:
    def __init__(self):
        original_image = pygame.image.load(constants.TITLE_IMAGE)
        self.image = pygame.transform.scale(
            original_image, (original_image.get_width(), constants.SCREEN_HEIGHT)
        )

    def draw(self, screen):
        screen.blit(
            self.image,
            (
                constants.TITLE_POSITION[0] - self.image.get_width() // 2,
                constants.TITLE_POSITION[1] - self.image.get_height() // 2,
            ),
        )

    def mouse_click(self):
        # Placeholder for handling mouse click events on the title screen
        pass


class PlayButton:
    def __init__(self):
        original_image = pygame.image.load(constants.PLAY_BUTTON)
        self.image = pygame.transform.scale(original_image, (300, 300))

    def draw(self, screen):
        screen.blit(
            self.image,
            (
                constants.SCREEN_WIDTH // 2 - self.image.get_width() // 2,
                constants.SCREEN_HEIGHT // 2 - self.image.get_height() // 2,
            ),
        )


class GameOver:
    def __init__(self):
        original_image = pygame.image.load(constants.GAME_OVER_IMAGE)
        self.image = pygame.transform.scale(
            original_image, (original_image.get_width(), constants.SCREEN_HEIGHT)
        )

    def draw(self, screen):
        screen.blit(
            self.image,
            (
                constants.GAME_OVER_POSITION[0] - self.image.get_width() // 2,
                constants.GAME_OVER_POSITION[1] - self.image.get_height() // 2,
            ),
        )


class MapScreen:
    def __init__(self):
        original_image = pygame.image.load(constants.MAP_IMAGE)
        self.image = pygame.transform.scale(
            original_image, (constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT)
        )

    def draw(self, screen):
        screen.blit(
            self.image,
            (
                constants.MAP_POSITION[0] - self.image.get_width() // 2,
                constants.MAP_POSITION[1] - self.image.get_height() // 2,
            ),
        )
