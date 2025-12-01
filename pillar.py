"""pillar obstacle"""

import pygame
import character
import constants
import math


class Pillar:
    def __init__(self, x, y):
        original_image = pygame.image.load(constants.PILLAR_IMAGE)
        self.image = pygame.transform.scale(
            original_image, (constants.PILLAR_WIDTH, constants.PILLAR_HEIGHT)
        )
        self.x = x
        self.y = y
        self.width = constants.PILLAR_WIDTH
        self.height = constants.PILLAR_HEIGHT
        self.active = True
        self.speed = constants.PILLAR_SPEED

    def update(self, keys, character):
        if keys[pygame.K_RIGHT] and character.x == constants.SCREEN_WIDTH // 2:
            if self.active:
                self.x += self.speed
                if self.x + self.width < 0:  # respawn on right
                    self.x = constants.SCREEN_WIDTH
                    self.active = True
        if keys[pygame.K_LEFT] and character.x == constants.SCREEN_WIDTH // 2:
            if self.active:
                self.x -= self.speed
                if self.x > constants.SCREEN_WIDTH:  # respawn on left
                    self.x = -self.width
                    self.active = True

    def collision(self, character):
        # Get character and pillar rectangles
        char_rect = pygame.Rect(
            character.x, character.y, character.width, character.height
        )
        pillar_rect = pygame.Rect(self.x, self.y, self.width, self.height)

        if char_rect.colliderect(pillar_rect):
            # Determine collision side
            if (
                character.vy > 0
                and character.y + character.height - character.vy <= self.y
            ):
                # Landing on top
                character.y = self.y - character.height
                character.vy = 0
                character.on_ground = True
            elif character.vy < 0 and character.y >= self.y + self.height:
                # Hitting bottom of pillar
                character.y = self.y + self.height
                character.vy = 0
            elif character.x + character.width - character.speed <= self.x:
                # Hitting left side
                character.x = self.x - character.width
                self.active = False
            elif character.x >= self.x + self.width - character.speed:
                # Hitting right side
                character.x = self.x + self.width
                self.active = False

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))
