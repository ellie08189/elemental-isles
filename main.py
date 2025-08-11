"""Main game loop."""

import pygame
from constants import width, height, white, black

pygame.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Elemental Isles")
clock = pygame.time.Clock()


def main():
    """Run the game."""
    running = True
