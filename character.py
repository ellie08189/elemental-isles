"""trying to represent a character in the game."""

import random
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
        self.power_sprites = constants.POWERSPRITE
        # self.crouch_sprites = constants.CROUCH
        self.sprites = [self.idle_sprite]
        self.max_index = 0
        self.current_index = 0
        self.width = constants.CHARACTER_WIDTH
        self.height = constants.CHARACTER_HEIGHT
        self.jump = 2
        self.jump_key_pressed = False

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

        if keys[pygame.K_UP]:
            if not self.jump_key_pressed and self.jump > 0:
                self.vy = constants.JUMP_STRENGTH
                self.on_ground = False
                self.max_index = len(self.sprites) - 1
                self.current_index = 0
                self.jump -= 1
                self.jump_key_pressed = True
                if self.y + self.height < 0:
                    self.apply_gravity()
        else:
            self.jump_key_pressed = False

        if keys[pygame.K_DOWN] and self.on_ground == False:
            self.vy += constants.GRAVITY
            self.y += self.vy
            self.max_index = len(self.sprites) - 1
            self.current_index = 0

        if keys[pygame.K_s]:
            self.sprites = self.power_sprites
            self.max_index = len(self.sprites) - 1
            self.current_index = 0

            # make the sprite stop jumping if screen top is reached

    def apply_gravity(self):
        self.vy += constants.GRAVITY
        self.y += self.vy

        # Prevent character from going above the screen
        if self.y < 0:
            self.y = 0
            self.vy = 0

        if self.y >= constants.GROUND_Y - constants.CHARACTER_HEIGHT:
            self.y = constants.GROUND_Y - constants.CHARACTER_HEIGHT
            self.vy = 0
            self.on_ground = True
            self.jump = 2

    def update(self):
        if self.current_index < self.max_index:
            self.current_index += 1
        else:
            self.current_index = 0

    def draw(self, screen):
        screen.blit(self.sprites[self.current_index], (self.x, self.y))


class Powers:
    # use water arrow
    def __init__(self, x, y):
        self.sprites = constants.POWER
        self.x = x
        self.y = y
        self.speed = constants.POWER_SPEED
        self.current_index = 0
        self.max_index = len(self.sprites) - 1
        self.width = constants.POWER_WIDTH
        self.height = constants.POWER_HEIGHT
        self.active = False
        self.collision_detected = False
        self.collision_amount = 0

    def update(self):
        if self.current_index < self.max_index:
            self.current_index += 1
        else:
            self.current_index = 0

    def power(self, character, keys):
        if keys[pygame.K_s]:  # Activate and position the power
            if not self.active:  # Reset position when first activating
                self.x = character.x
                self.y = character.y + 20
            self.active = True

        if self.active:
            self.x += self.speed
            if self.x > constants.SCREEN_WIDTH:
                self.active = False  # Deactivate if it goes off screen

    def collision(self, fireball):
        if not self.active:
            return

        power_rect = pygame.Rect(self.x, self.y, self.width, self.height)
        fireball_rect = pygame.Rect(
            fireball.x, fireball.y, fireball.width, fireball.height
        )

        if power_rect.colliderect(fireball_rect):
            self.active = False
            fireball.x = constants.SCREEN_WIDTH + random.randint(
                500, 2000
            )  # Move fireball off-screen
            self.collision_detected = True
            self.collision_amount = self.collision_amount + 1

    def draw(self, screen):
        if self.active:
            screen.blit(self.sprites[self.current_index], (self.x, self.y))
