"""lives the character has left"""

import pygame
import constants


class Lives:
    """manages lives character has left"""

    def __init__(self):
        self.lives = 3
        self.heart = pygame.image.load("assets/heart.png")
        self.heart = pygame.transform.scale(
            self.heart, (constants.HEART_WIDTH, constants.HEART_HEIGHT)
        )
        self.lost_life_sound = pygame.mixer.Sound(constants.LOST_LIFE_SOUND)
        self.lost_life_sound.set_volume(0.1)

    def lose_life(self, character=None):
        """reduces lives by 1 and plays sound when collision occurs"""
        self.lives -= 1
        self.lost_life_sound.play()
        if character:
            character.start_invincibility(120)  # 2 seconds of invincibility

    def draw(self, screen):
        """draws hearts on the screen representing lives left"""
        for i in range(self.lives):
            screen.blit(self.heart, (10 + i * (constants.HEART_WIDTH + 10), 10))
