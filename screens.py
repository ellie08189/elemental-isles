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
                constants.SCREEN_HEIGHT // 2 - self.image.get_height() // 2 + 50,
            ),
        )


class Name:
    """displays name on title screen"""

    def __init__(self):
        self.font1 = pygame.font.Font(constants.VICTORY_FONT, 75)
        self.font2 = pygame.font.Font(constants.VICTORY_FONT, 150)

    def draw(self, screen):
        """draws name on title screen"""
        name_surface = self.font1.render(
            "Legends of the", True, constants.NAME_FONT_COLOUR
        )
        name_surface2 = self.font2.render(
            "Elemental Isles", True, constants.NAME_FONT_COLOUR
        )
        screen.blit(
            name_surface,
            (
                constants.SCREEN_WIDTH // 2 - name_surface.get_width() // 2,
                40,
            ),
        )
        screen.blit(
            name_surface2,
            (
                constants.SCREEN_WIDTH // 2 - name_surface2.get_width() // 2,
                100,
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
        self.x = 600
        self.y = 200

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
            original_image, (original_image.get_width(), constants.SCREEN_HEIGHT)
        )
        self.font = pygame.font.Font(
            constants.VICTORY_FONT, constants.VICTORY_FONT_SIZE
        )
        self.score_display = None
        self.score_display2 = None

    def score(self):
        """displays final score on victory screen"""
        self.score_display = pygame.font.Font(
            constants.SCORE_FONT, constants.SCORE_FONT_SIZE
        ).render("Final Score:", True, constants.SCORE_COLOR)
        x_pos = constants.SCREEN_WIDTH // 2 - self.score_display.get_width() // 2
        self.image.blit(
            self.score_display,
            (x_pos, 375),
        )

    def score2(self, score):
        """displays final score on victory screen"""
        self.score_display2 = pygame.font.Font(
            constants.SCORE_FONT, constants.SCORE_FONT_SIZE2
        ).render(f"{score.score}", True, constants.SCORE_COLOR)
        self.image.blit(
            self.score_display2,
            (constants.SCREEN_WIDTH // 2 - self.score_display2.get_width() // 2, 450),
        )

    def victory(self):
        """displays victory message on victory screen"""
        victory_surface = self.font.render(
            "Victory!", True, constants.VICTORY_FONT_COLOR
        )
        self.image.blit(
            victory_surface,
            (constants.SCREEN_WIDTH // 2 - victory_surface.get_width() // 2, 65),
        )

    def keys_collected(self, cumulative_total):
        """displays keys collected on victory screen"""
        keys_collected_display = pygame.font.Font(
            constants.SCORE_FONT, constants.SCORE_FONT_SIZE
        ).render(f"Keys Collected: {cumulative_total}", True, constants.SCORE_COLOR)
        x_pos = constants.SCREEN_WIDTH // 2 - keys_collected_display.get_width() // 2
        self.image.blit(
            keys_collected_display,
            (x_pos, 325),
        )

    def draw(self, screen):
        """draws victory screen image"""
        screen.blit(
            self.image,
            (0, 0),
        )
