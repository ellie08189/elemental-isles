"""all screen classes for different game states"""

import pygame
import constants


class TitleScreen:
    """manages title screen"""

    def __init__(self):
        original_image = pygame.image.load(constants.TITLE_IMAGE)
        self.image = pygame.transform.scale(
            original_image, (original_image.get_width(), constants.SCREEN_HEIGHT)
        )

    def draw(self, screen):
        """draws title screen image"""
        screen.blit(
            self.image,
            (
                constants.TITLE_POSITION[0] - self.image.get_width() // 2,
                constants.TITLE_POSITION[1] - self.image.get_height() // 2,
            ),
        )


class PlayButton:
    """manages play button"""

    def __init__(self):
        original_image = pygame.image.load(constants.PLAY_BUTTON)
        self.image = pygame.transform.scale(original_image, (300, 300))

    def draw(self, screen):
        """draws play button on the screen"""
        screen.blit(
            self.image,
            (
                constants.SCREEN_WIDTH // 2 - self.image.get_width() // 2,
                constants.SCREEN_HEIGHT // 2 - self.image.get_height() // 2,
            ),
        )


class GameOver:
    """manages game over screen"""

    def __init__(self):
        original_image = pygame.image.load(constants.GAME_OVER_IMAGE)
        self.image = pygame.transform.scale(
            original_image, (original_image.get_width(), constants.SCREEN_HEIGHT)
        )

    def draw(self, screen):
        """draws game over screen image"""
        screen.blit(
            self.image,
            (
                constants.GAME_OVER_POSITION[0] - self.image.get_width() // 2,
                constants.GAME_OVER_POSITION[1] - self.image.get_height() // 2,
            ),
        )


class MapScreen:
    """manages map screen"""

    def __init__(self):
        original_image = pygame.image.load(constants.MAP_IMAGE)
        self.image = pygame.transform.scale(
            original_image, (constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT)
        )

    def draw(self, screen):
        """draws map screen image"""
        screen.blit(
            self.image,
            (
                constants.MAP_POSITION[0] - self.image.get_width() // 2,
                constants.MAP_POSITION[1] - self.image.get_height() // 2,
            ),
        )


class PauseScreen:
    """manages pause screen"""

    def __init__(self):
        original_image = pygame.image.load(constants.PAUSE_IMAGE)
        self.image = pygame.transform.scale(
            original_image, (constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT)
        )

    def draw(self, screen):
        """draws pause screen image"""
        screen.blit(
            self.image,
            (
                constants.PAUSE_POSITION[0] - self.image.get_width() // 2,
                constants.PAUSE_POSITION[1] - self.image.get_height() // 2,
            ),
        )


class Score:
    """Shows score on screen"""

    def __init__(self):
        self.score = 0
        self.font = pygame.font.Font(constants.SCORE_FONT, constants.SCORE_FONT_SIZE)

    def increase(self, power, key_score):
        """Increases score by given amount"""
        for power.collision_amount in range(power.collision_amount):
            self.score += 50
            power.collision_amount = 0  # reset after adding to score
        for key_score.total in range(key_score.total):
            self.score += 100
            key_score.total = 0

    def draw(self, screen):
        """Draws score on the screen"""
        score_surface = self.font.render(
            f"Score: {self.score}", True, constants.SCORE_COLOR
        )
        screen.blit(
            score_surface, (constants.SCORE_POSITION[0], constants.SCORE_POSITION[1])
        )


class Buttons:
    """tells user buttons to press"""

    def __init__(self):
        self.font = pygame.font.Font(constants.SCORE_FONT, 20)
        self.speed = -5
        self.x = 300
        self.y = 400

    def update(self, keys, character):
        """updates button instructions position based on character movement"""
        if (
            keys[pygame.K_RIGHT]  # pylint: disable=no-member
            and character.x == constants.SCREEN_WIDTH // 2
        ):
            self.x += self.speed
        if (
            keys[pygame.K_LEFT]  # pylint: disable=no-member
            and character.x == constants.SCREEN_WIDTH // 2
        ):
            self.x -= self.speed

    def draw(self, screen):
        """draws button instructions on screen"""
        instructions = [
            "Press 'Space' to Pause",
            "Press 'A' to View Map",
            "Use Arrow Keys to Move",
            "Press S to Shoot",
        ]
        for i, instruction in enumerate(instructions):
            text_surface = self.font.render(instruction, True, (255, 255, 255))
            screen.blit(text_surface, (self.x, self.y + i * 25))


class Victory:
    """displays victory screen"""

    def __init__(self):
        original_image = pygame.image.load(constants.VICTORY_IMAGE)
        self.image = pygame.transform.scale(
            original_image, (constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT)
        )

    def draw(self, screen):
        """draws victory screen image"""
        screen.blit(
            self.image,
            (
                constants.TITLE_POSITION[0] - self.image.get_width() // 2,
                constants.TITLE_POSITION[1] - self.image.get_height() // 2,
            ),
        )
