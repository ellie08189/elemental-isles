"""trying to represent a character in the game."""

import pygame
import constants


class Character:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = 5
        self.vy = 0
        self.on_ground = True
        self.idle_sprite = constants.IDLE
        self.walking_sprites = constants.WALKING
        self.walkback_sprites = constants.WALKBACK
        # self.crouch_sprites = constants.CROUCH
        self.sprites = [self.idle_sprite]
        self.max_index = 0
        self.current_index = 0
        self.width = constants.CHARACTER_WIDTH
        self.height = constants.CHARACTER_HEIGHT

    def handle_input(self, keys):
        """Switch between walking, jumping, and idle sprites based on key press."""
        if keys[pygame.K_RIGHT]:
            self.sprites = self.walking_sprites
            self.max_index = len(self.sprites) - 1
            if self.x != constants.SCREEN_WIDTH // 2:
                self.x += self.speed
            if self.x > constants.SCREEN_WIDTH - self.width:
                self.x = constants.SCREEN_WIDTH - self.width

        elif keys[pygame.K_LEFT]:
            self.sprites = self.walkback_sprites
            self.max_index = len(self.sprites) - 1
            if self.x != constants.SCREEN_WIDTH // 2:
                self.x -= self.speed
            if self.x < 0:
                self.x = 0

        else:
            self.sprites = [self.idle_sprite]
            self.max_index = 0
            self.current_index = 0

        if keys[pygame.K_UP] and self.on_ground:
            self.vy = constants.JUMP_STRENGTH
            self.on_ground = False
            self.max_index = len(self.sprites) - 1
            self.current_index = 0
            if self.y + self.height < 0:
                self.apply_gravity()
            # make the sprite stop jumping if screen top is reached

        # if keys[pygame.K_DOWN]:
        # want sprite to move down by about 10 pixels

    def apply_gravity(self):
        self.vy += constants.GRAVITY
        self.y += self.vy
        if self.y >= constants.GROUND_Y - constants.CHARACTER_HEIGHT:
            self.y = constants.GROUND_Y - constants.CHARACTER_HEIGHT
            self.vy = 0
            self.on_ground = True

    def update(self):
        if self.current_index < self.max_index:
            self.current_index += 1
        else:
            self.current_index = 0

    def draw(self, screen):
        screen.blit(self.sprites[self.current_index], (self.x, self.y))
