import pygame
import constants
import math

class Obstacle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.radius = constants.OBSTACLE_RADIUS
        self.color = constants.OBSTACLE_COLOR
        self.speed = constants.OBSTACLE_SPEED
        self.active = True

    def update(self):
        if self.active:
            self.x += self.speed
            if self.x + self.radius < 0:  # respawn on right
                self.x = constants.SCREEN_WIDTH
                self.active = True

    def check_collision(self, player):
        dx = self.x - player.x
        dy = self.y - player.y
        distance = math.sqrt(dx*dx + dy*dy)
        if distance <= self.radius + player.radius:
            self.active = False

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)
