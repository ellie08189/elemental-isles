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
