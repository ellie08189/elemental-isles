"""keys for charcater to collect in the game."""

import pygame
import constants


class Key:
    """key class for character to collect in the game."""

    def __init__(self, x, y):
        self.image = pygame.image.load(constants.KEY_IMAGE)
        self.image = pygame.transform.scale(
            self.image, (constants.KEY_WIDTH, constants.KEY_HEIGHT)
        )
        self.x = x
        self.y = y
        self.amount = 0
        self.collision_detected = False
        self.rect = pygame.Rect(
            self.x, self.y, constants.KEY_WIDTH, constants.KEY_HEIGHT
        )
        self.speed = constants.KEY_SPEED
        self.active = True
        self.sound = pygame.mixer.Sound(constants.COLLECT_KEY_SOUND)

    def update(self, keys, character):
        """updates key position based on character movement"""
        if keys[pygame.K_LEFT] and character.x == constants.SCREEN_WIDTH // 2:
            if self.active:
                self.x -= self.speed
        if keys[pygame.K_RIGHT] and character.x == constants.SCREEN_WIDTH // 2:
            if self.active:
                self.x += self.speed
        self.rect.topleft = (self.x, self.y)

    def collision(self, character, key_score):
        """checks for collision with character"""
        if not self.active:
            return
        char_rect = pygame.Rect(
            character.x, character.y, character.width, character.height
        )
        if self.rect.colliderect(char_rect):
            self.collision_detected = True
            self.active = False
            self.amount = 1
            key_score.add_key(self)
            self.sound.play()

    def draw(self, screen):
        """draws key on the screen"""
        if self.active:
            screen.blit(self.image, (self.x, self.y))


class TotalKeys:
    """tracks total keys collected by character."""

    def __init__(self):
        self.total = 0

    def add_key(self, key):
        """adds key to total collected keys"""
        self.total += key.amount
        print(f"Total keys collected: {self.total}")
        return self.total
