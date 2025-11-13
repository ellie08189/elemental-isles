import pygame
import constants


class Background:
    def __init__(self):
        original_image = pygame.image.load(constants.BACKGROUND_IMAGE)
        # Scale the image to match the screen height
        self.image = pygame.transform.scale(
            original_image, (original_image.get_width(), constants.SCREEN_HEIGHT)
        )
        self.x1 = 0
        self.x2 = self.image.get_width()
        self.y = 0
        self.speed = constants.BACKGROUND_SPEED

    def update(self, keys, player):
        if keys[pygame.K_LEFT] and player.x == constants.SCREEN_WIDTH // 2:
            self.scroll_left()

        if keys[pygame.K_RIGHT] and player.x == constants.SCREEN_WIDTH // 2:
            self.scroll_right()

        # If an image goes off screen, reset its position to the right of the other image
        if self.x1 + self.image.get_width() < 0:
            self.x1 = self.x2 + self.image.get_width()
        elif self.x1 > constants.SCREEN_WIDTH:
            self.x1 = self.x2 - self.image.get_width()

        if self.x2 + self.image.get_width() < 0:
            self.x2 = self.x1 + self.image.get_width()
        elif self.x2 > constants.SCREEN_WIDTH:
            self.x2 = self.x1 - self.image.get_width()

    def scroll_left(self):
        self.x1 += self.speed
        self.x2 += self.speed

    def scroll_right(self):
        self.x1 -= self.speed
        self.x2 -= self.speed

    def draw(self, screen):
        screen.blit(self.image, (self.x1, self.y))
        screen.blit(self.image, (self.x2, self.y))
