"""trying to represent a character in the game."""

import pygame


class Character:
    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y
        self.sprites = [pygame.image.load("assets/idle1.png")]
        self.max_index = len(self.sprites) - 1
        self.current_index = self.max_index

    def walk(self, keys):
        """Load walking sprites into a list"""
        if keys[pygame.K_RIGHT]:
            self.sprites = [
                pygame.image.load("assets/walk1.png"),
                pygame.image.load("assets/walk1.png"),
                pygame.image.load("assets/walk1.png"),
                pygame.image.load("assets/walk1.png"),
                pygame.image.load("assets/walk2.png"),
                pygame.image.load("assets/walk2.png"),
                pygame.image.load("assets/walk2.png"),
                pygame.image.load("assets/walk2.png"),
                pygame.image.load("assets/walk3.png"),
                pygame.image.load("assets/walk3.png"),
                pygame.image.load("assets/walk3.png"),
                pygame.image.load("assets/walk3.png"),
                pygame.image.load("assets/walk4.png"),
                pygame.image.load("assets/walk4.png"),
                pygame.image.load("assets/walk4.png"),
                pygame.image.load("assets/walk4.png"),
                pygame.image.load("assets/walk5.png"),
                pygame.image.load("assets/walk5.png"),
                pygame.image.load("assets/walk5.png"),
                pygame.image.load("assets/walk5.png"),
                pygame.image.load("assets/walk6.png"),
                pygame.image.load("assets/walk6.png"),
                pygame.image.load("assets/walk6.png"),
                pygame.image.load("assets/walk6.png"),
                pygame.image.load("assets/walk7.png"),
                pygame.image.load("assets/walk7.png"),
                pygame.image.load("assets/walk7.png"),
                pygame.image.load("assets/walk7.png"),
                pygame.image.load("assets/walk8.png"),
                pygame.image.load("assets/walk8.png"),
                pygame.image.load("assets/walk8.png"),
                pygame.image.load("assets/walk8.png"),
            ]
            self.max_index = len(self.sprites) - 1
            self.current_index = self.max_index

    def update(self):
        """Increment index by 1 and reset if index is larger than max index"""
        if self.current_index < self.max_index:
            self.current_index += 1
        else:
            self.current_index = 0
        # One liner
        # self.current_index += 1 if self.current_index < self.max_index else -self.max_index

    def draw(self, screen):
        screen.blit(self.sprites[self.current_index], (self.x, self.y))


pygame.init()
pygame.display.set_caption("Character Animation Test")
character = Character(100, 100)
background = pygame.display.set_mode((400, 300))
background.fill((255, 255, 255))
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break  # Exit the event loop immediately to prevent further processing
    keys = pygame.key.get_pressed()
    character.walk(keys)
    character.update()
    background.fill((255, 255, 255))
    character.draw(background)
    clock.tick(60)
    pygame.display.update()

pygame.quit()
