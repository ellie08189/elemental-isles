"""lives the character has left"""

import pygame
import constants


class Lives:
    def __init__(self):
        self.lives = 3
        self.heart = pygame.image.load("assets/heart.png")
        self.heart = pygame.transform.scale(
            self.heart, (constants.HEART_WIDTH, constants.HEART_HEIGHT)
        )
        self.lost_life_sound = pygame.mixer.Sound(constants.LOST_LIFE_SOUND)
        self.lost_life_sound.set_volume(0.1)

    def lose_life(self):
        self.lives -= 1
        self.lost_life_sound.play()

    def draw(self, screen):
        for i in range(self.lives):
            screen.blit(self.heart, (10 + i * (constants.HEART_WIDTH + 10), 10))
