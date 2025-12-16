"""platforms"""

import pygame
import constants
import random


class Platform:
    """A platform that the player can stand on."""

    def __init__(self, x, y):
        original_image = pygame.image.load(constants.PLATFORM_IMAGE)
        self.image = pygame.transform.scale(
            original_image, (constants.PLATFORM_WIDTH, constants.PLATFORM_HEIGHT)
        )
        self.x = x
        self.y = y
        self.width = constants.PLATFORM_WIDTH
        self.height = constants.PLATFORM_HEIGHT
        # to randomly generate - pick number between e.g. 1-10 and time the width by 31 and height by 11 for that number
        self.active = True
        self.speed = constants.PILLAR_SPEED
        self.collison_detected = False

    def spawn_platform(self):
        num = random.randint(1, 10)
        self.width = num * 31
        self.height = num * 11

    def update(self, keys, character):

        if keys[pygame.K_RIGHT] and character.x == constants.SCREEN_WIDTH // 2:
            if self.active:
                self.x += self.speed
        if keys[pygame.K_LEFT] and character.x == constants.SCREEN_WIDTH // 2:
            if self.active:
                self.x -= self.speed

    def collision(self, character):
        # Get character and platform rectangles
        char_rect = pygame.Rect(
            character.x, character.y, character.width, character.height
        )
        platform_rect = pygame.Rect(self.x, self.y, self.width, self.height)

        if char_rect.colliderect(platform_rect):
            # Determine collision side
            if (
                character.vy > 0
                and character.y + character.height - character.vy <= self.y
            ):
                # Landing on top
                character.y = self.y - character.height
                character.vy = 0
                character.on_ground = True
            elif character.y <= self.y + self.height:
                # Hitting bottom of platform
                character.y = self.y + self.height
                character.vy += constants.GRAVITY
                character.on_ground = False
                self.collison_detected = True
            elif character.x + character.width - character.speed <= self.x:
                # Hitting left side
                character.x = self.x - character.width
                self.active = False
                self.collison_detected = True
            elif character.x >= self.x + self.width - character.speed:
                # Hitting right side
                character.x = self.x + self.width
                self.active = False
                self.collison_detected = True

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))
