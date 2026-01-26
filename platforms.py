"""platforms"""

import random
import pygame
import constants


class Platform:
    """platform for the character to jump on"""

    def __init__(self, x, y, width=None, height=None):
        image_path = random.choice(constants.PLATFORM_IMAGES)
        original_image = pygame.image.load(image_path)
        self.width = width if width is not None else constants.PLATFORM_WIDTH
        self.height = height if height is not None else constants.PLATFORM_HEIGHT
        self.image = pygame.transform.scale(original_image, (self.width, self.height))
        self.x = x
        self.y = y
        self.active = True
        self.speed = constants.PILLAR_SPEED
        self.collision_detected = False

    def __repr__(self):
        return f"Platform(x={self.x}, y={self.y}, width={self.width}, height={self.height}, active={self.active})"

    def update(self, keys, character):
        if keys[pygame.K_RIGHT] and character.x == constants.SCREEN_WIDTH // 2:
            if self.active:
                self.x += self.speed
        if keys[pygame.K_LEFT] and character.x == constants.SCREEN_WIDTH // 2:
            if self.active:
                self.x -= self.speed

    def collision(self, character):
        char_rect = pygame.Rect(
            character.x, character.y, character.width, character.height
        )
        platform_rect = pygame.Rect(self.x, self.y, self.width, self.height)

        if char_rect.colliderect(platform_rect):
            if (
                character.vy > 0
                and character.y + character.height - character.vy <= self.y
            ):  # landing on top
                character.y = self.y - character.height
                character.vy = 0
                character.on_ground = True
                character.jump = 2
            elif character.y <= self.y + self.height:  # hitting from below
                character.y = self.y + self.height
                character.vy += constants.GRAVITY
                character.on_ground = False
                self.collision_detected = True
            elif (
                character.x + character.width - character.speed <= self.x
            ):  # hitting from left
                character.x = self.x - character.width
                self.active = False
                self.collision_detected = True
            elif (
                character.x >= self.x + self.width - character.speed
            ):  # hitting from right
                character.x = self.x + self.width
                self.active = False
                self.collision_detected = True

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))


class PlatformManager:
    """Manages all platforms and handles spawning, updating, and drawing."""

    def __init__(self):
        self.platforms = []
        self.furthest_platform_x = 2000
        # Spawn the initial platform
        initial_platform = Platform(self.furthest_platform_x, 550)
        self.platforms.append(initial_platform)
        self.furthest_platform_x = initial_platform.x + initial_platform.width

    def spawn_platform(self):
        # Only spawn if the furthest platform is within the screen
        if self.furthest_platform_x < constants.SCREEN_WIDTH + 400:
            num = random.randint(3, 6)
            gap = random.randint(150, 300)
            width = num * 31
            height = num * 11
            y = random.randint(300, 575)
            new_x = self.furthest_platform_x + gap
            new_platform = Platform(new_x, y, width, height)
            self.platforms.append(new_platform)
            self.furthest_platform_x = new_x + width

    def update(self, keys, character):
        for platform in self.platforms:
            platform.update(keys, character)
        # Do not remove platforms that have moved off screen, so the player can walk back
        # Update furthest_platform_x
        if self.platforms:
            self.furthest_platform_x = max(p.x + p.width for p in self.platforms)
        else:
            self.furthest_platform_x = 0
        self.spawn_platform()

    def collision(self, character):
        for platform in self.platforms:
            platform.collision(character)

    def draw(self, screen):
        for platform in self.platforms:
            platform.draw(screen)
