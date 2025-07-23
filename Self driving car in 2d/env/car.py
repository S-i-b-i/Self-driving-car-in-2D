# env/car.py

import pygame
import math
from env.sensors import Sensor
from config import CAR_WIDTH, CAR_HEIGHT, TURN_ANGLE, ACCELERATION, FRICTION

class Car:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.angle = 0
        self.speed = 0
        self.sensor = Sensor(self, angles_deg=[-60, -30, 0, 30, 60])
        self.image = pygame.image.load("assets/car.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (CAR_WIDTH, CAR_HEIGHT))

    def draw(self, surface):
        rotated = pygame.transform.rotate(self.image, self.angle)
        rect = rotated.get_rect(center=(self.x, self.y))
        surface.blit(rotated, rect.topleft)
        self.sensor.draw(surface)

    def update_rl(self, action, track):
        if action['acc']:
            self.speed += ACCELERATION
        else:
            self.speed *= FRICTION

        self.angle += TURN_ANGLE * action['turn']
        rad = math.radians(self.angle)
        self.x += self.speed * math.cos(rad)
        self.y -= self.speed * math.sin(rad)

        self.sensor.update(track)

