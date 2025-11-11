import pygame
import constants


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
