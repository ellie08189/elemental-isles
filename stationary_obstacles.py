"""stationary obstacles"""

import random
import pygame
import constants


class Pillar:
    """manages pillar obstacle"""

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
        self.collision_detected = False

    def update(self, keys, character):
        """updates pillar position based on character movement"""
        if (
            keys[pygame.K_RIGHT]  # pylint: disable=no-member
            and character.x == constants.SCREEN_WIDTH // 2
        ):
            if self.active:
                self.x += self.speed
        if (
            keys[pygame.K_LEFT]  # pylint: disable=no-member
            and character.x == constants.SCREEN_WIDTH // 2
        ):
            if self.active:
                self.x -= self.speed

    def collision(self, character):
        """checks for collision between pillar and character"""
        # Get character and pillar rectangles
        char_rect = pygame.Rect(
            character.x, character.y, character.width, character.height
        )
        pillar_rect = pygame.Rect(self.x, self.y, self.width, self.height)
        if character.immune is True:
            return
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
                character.jump = 2
            elif character.vy < 0 and character.y >= self.y + self.height:
                # Hitting bottom of pillar
                character.y = self.y + self.height
                character.vy = 0
            elif character.x + character.width - character.speed <= self.x:
                # Hitting left side
                character.x = self.x - character.width
                self.collision_detected = True
            elif character.x >= self.x + self.width - character.speed:
                # Hitting right side
                character.x = self.x + self.width
                self.collision_detected = True

    def draw(self, screen):
        """draws pillar on screen"""
        screen.blit(self.image, (self.x, self.y))


class Bush1:
    """manages bush obstacle"""

    def __init__(self, x, y):
        image_path = random.choice(constants.BUSH_IMAGES)
        original_image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(
            original_image, (constants.BUSH1_WIDTH, constants.BUSH1_HEIGHT)
        )
        self.x = x
        self.y = y
        self.width = constants.BUSH1_WIDTH
        self.height = constants.BUSH1_HEIGHT
        self.active = True
        self.speed = constants.BUSH1_SPEED
        self.collision_detected = False

    def update(self, keys, character):
        """updates bush position based on character movement"""
        if (
            keys[pygame.K_RIGHT]  # pylint: disable=no-member
            and character.x == constants.SCREEN_WIDTH // 2
        ):
            if self.active:
                self.x += self.speed
                # if self.x + self.width < 0:  # respawn on right
                #     self.x = constants.SCREEN_WIDTH
                #     self.active = True
        if (
            keys[pygame.K_LEFT]  # pylint: disable=no-member
            and character.x == constants.SCREEN_WIDTH // 2
        ):
            if self.active:
                self.x -= self.speed

    def collision(self, character):
        """checks for collision between bush and character"""
        # Get character and obstacle rectangles
        char_rect = pygame.Rect(
            character.x, character.y, character.width, character.height
        )
        bush1_rect = pygame.Rect(self.x, self.y, self.width, self.height)
        if character.immune is True:
            return
        if char_rect.colliderect(bush1_rect):
            # Determine collision side
            if (
                character.vy > 0
                and character.y + character.height - character.vy <= self.y
            ):
                # Landing on top
                character.y = self.y - character.height
                character.vy = 0
                character.on_ground = True
                character.jump = 2

            elif character.vy < 0 and character.y >= self.y + self.height:
                # Hitting bottom of bush
                character.y = self.y + self.height
                character.vy = 0
            elif character.x + character.width - character.speed <= self.x:
                # Hitting left side
                character.x = self.x - character.width
            elif character.x >= self.x + self.width - character.speed:
                # Hitting right side
                character.x = self.x + self.width
            self.collision_detected = True

    def draw(self, screen):
        """draws bush on screen"""
        screen.blit(self.image, (self.x, self.y))
