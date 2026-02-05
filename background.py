"""background of the game"""

import pygame
import constants


class Background:
    """manages background"""

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
        self.sound = pygame.mixer.Sound(constants.MAIN_THEME_MUSIC)
        self.scroll = None

    def update(self, keys, character):
        """updates background position based on character movement"""
        if (
            keys[pygame.K_LEFT]  # pylint: disable=no-member
            and character.x == constants.SCREEN_WIDTH // 2
        ):
            self.scroll_left()

        if (
            keys[pygame.K_RIGHT]  # pylint: disable=no-member
            and character.x == constants.SCREEN_WIDTH // 2
        ):
            self.scroll_right()

        if not (
            keys[pygame.K_LEFT] or keys[pygame.K_RIGHT]  # pylint: disable=no-member
        ):
            self.scroll_stop()

        # If an image goes off screen, reset its position to the right of the other image
        if self.x1 + self.image.get_width() < 0:
            self.x1 = self.x2 + self.image.get_width()
        elif self.x1 > constants.SCREEN_WIDTH:
            self.x1 = self.x2 - self.image.get_width()
        if self.x2 + self.image.get_width() < 0:
            self.x2 = self.x1 + self.image.get_width()
        elif self.x2 > constants.SCREEN_WIDTH:
            self.x2 = self.x1 - self.image.get_width()

    def approach_door(self, door):
        """door appears in screen"""
        if door.x + door.width <= constants.SCREEN_WIDTH:
            self.scroll = None
            self.speed = 0

    def scroll_left(self):
        """makes background move right"""
        self.x1 += self.speed
        self.x2 += self.speed
        self.scroll = "left"

    def scroll_right(self):
        """makes background move left"""
        self.x1 -= self.speed
        self.x2 -= self.speed
        self.scroll = "right"

    def scroll_stop(self):
        """stops background movement"""
        self.x1 = self.x1
        self.x2 = self.x2
        self.scroll = None

    def sound_play(self):
        """plays background music"""
        self.sound.set_volume(0.5)
        self.sound.play(loops=-1)

    def draw(self, screen):
        """draws background to screen"""
        screen.blit(self.image, (self.x1, self.y))
        screen.blit(self.image, (self.x2, self.y))
