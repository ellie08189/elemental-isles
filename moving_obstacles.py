"""for obstacles that move independently to the character"""

import pygame
import constants


class Fireball:
    """a fireball that moves across the screen"""

    def __init__(self, x, y):
        self.image = constants.FIREBALL_IMAGE
        self.x = x
        self.y = y
        self.width = constants.FIREBALL_WIDTH
        self.height = constants.FIREBALL_HEIGHT
        self.speed = constants.FIREBALL_SPEED
        self.active = True
        self.collision_detected = False
        self.current_index = 0
        self.max_index = 0

    def update(self, background):
        # could make it so always aims for character by using character.x for location when spawning - spawn certain amount of times?
        # need fireball to move faster when background movingleft and slower when moving right
        """move the fireball across the screen"""
        if self.active:
            if background.speed < 0:
                self.x += self.speed + background.speed
            elif background.speed > 0:
                self.x += self.speed - background.speed
            else:
                self.x += self.speed
            self.max_index = len(self.image) - 1
            if self.current_index < self.max_index:
                self.current_index += 1
            else:
                self.current_index = 0
            self.active = True
            if self.x < -100:
                self.active = False

    def collision(self, character):
        """check for collision with the character"""
        # Get character and obstacle rectangles
        char_rect = pygame.Rect(
            character.x, character.y, character.width, character.height
        )
        fireball_rect = pygame.Rect(self.x, self.y, self.width, self.height)
        if char_rect.colliderect(fireball_rect):
            # Determine collision side
            if (
                character.vy > 0
                and character.y + character.height - character.vy <= self.y
            ):
                # Landing on top
                character.y = self.y - character.height
                character.vy = 0

            elif character.vy < 0 and character.y >= self.y + self.height:
                # Hitting bottom of bush
                character.y = self.y + self.height
                character.vy = 0
            elif character.x + character.width - character.speed <= self.x:
                # Hitting left side
                character.x = self.x - character.width
                # self.active = False
            elif character.x >= self.x + self.width - character.speed:
                # Hitting right side
                character.x = self.x + self.width
                # self.active = False
            self.collision_detected = True

    def draw(self, screen):
        screen.blit(self.image[self.current_index], (self.x, self.y))


class Log:
    def __init__(self, x, y):
        self.image = constants.LOG_IMAGE
        self.x = x
        self.y = y
        self.current_index = 0
        self.max_index = 0
        self.width = constants.LOG_WIDTH
        self.height = constants.LOG_HEIGHT
        self.speed = constants.LOG_SPEED
        self.active = True

    def move(self):
        if self.active:
            self.max_index = len(self.image) - 1
            self.x += self.speed

    def update(self):
        if self.current_index < self.max_index:
            self.current_index += 1
        else:
            self.current_index = 0

    def draw(self, screen):
        screen.blit(self.image[self.current_index], (self.x, self.y))
