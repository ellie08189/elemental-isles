import pygame
import constants


class Cloud:
    def __init__(self):
        self.x = constants.CLOUD_RESET_X
        self.y = constants.CLOUD_Y
        self.speed = constants.CLOUD_SPEED
        self.image = pygame.image.load(constants.CLOUD_IMAGE)

    def update(self):
        self.x += self.speed
        if self.x + self.image.get_width() < constants.CLOUD_OFFSCREEN_X:
            self.x = constants.CLOUD_RESET_X

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))
