# env/track.py

import pygame

class Track:
    def __init__(self):
        self.image = pygame.image.load("assets/track.jpg").convert()
        self.mask = pygame.mask.from_threshold(self.image, (0, 0, 0), (60, 60, 60))  # Detects black pixels
        self.rect = self.image.get_rect()

    def draw(self, screen):
        screen.blit(self.image, self.rect.topleft)

    def is_colliding(self, x, y):
        try:
            return self.mask.get_at((int(x), int(y))) == 1  # 1 = collision
        except IndexError:
            return True  # Out of bounds = crash
