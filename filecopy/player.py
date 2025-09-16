import pygame
import constants

class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.radius = constants.PLAYER_RADIUS
        self.color = constants.PLAYER_COLOR
        self.speed = constants.PLAYER_SPEED
        self.vy = 0
        self.on_ground = True

    def handle_input(self, keys):
        if keys[pygame.K_LEFT] and self.x - self.radius > 0:
            self.x -= self.speed
        if keys[pygame.K_RIGHT] and self.x + self.radius < constants.SCREEN_WIDTH:
            self.x += self.speed
        if keys[pygame.K_UP] and self.on_ground:
            self.vy = constants.JUMP_STRENGTH
            self.on_ground = False

    def apply_gravity(self):
        self.vy += constants.GRAVITY
        self.y += self.vy
        if self.y >= constants.GROUND_Y - self.radius:
            self.y = constants.GROUND_Y - self.radius
            self.vy = 0
            self.on_ground = True

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)
