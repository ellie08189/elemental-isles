"""display map"""

import pygame
import constants


class MapScreen:
    def __init__(self):
        original_image = pygame.image.load(constants.MAP_IMAGE)
        self.image = pygame.transform.scale(
            original_image, (original_image.get_width(), constants.SCREEN_HEIGHT)
        )

    def draw(self, screen):
        screen.blit(
            self.image,
            (
                constants.MAP_POSITION[0] - self.image.get_width() // 2,
                constants.MAP_POSITION[1] - self.image.get_height() // 2,
            ),
        )


# if m is pressed in game screen, go to map screen
