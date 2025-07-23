# env/sensors.py

import pygame
import math
from config import BLACK

class Sensor:
    def __init__(self, car, angles_deg):
        self.car = car
        self.angles = angles_deg
        self.readings = [0 for _ in angles_deg]

    def update(self, track):
        self.readings = []
        for angle in self.angles:
            dist = self.cast_ray(angle, track)  # ✅ Pass track here
            self.readings.append(dist)

    def cast_ray(self, angle, track):  # ✅ Accept track here
        rad = math.radians(angle + self.car.angle)
        for dist in range(1, 150):
            test_x = self.car.x + dist * math.cos(rad)
            test_y = self.car.y - dist * math.sin(rad)
            if track.is_colliding(test_x, test_y):  # ✅ Call correctly
                return dist
        return 150  # max sensor range

    def draw(self, surface):
        for i, angle in enumerate(self.angles):
            rad = math.radians(angle + self.car.angle)
            end_x = self.car.x + self.readings[i] * math.cos(rad)
            end_y = self.car.y - self.readings[i] * math.sin(rad)
            pygame.draw.line(surface, BLACK, (self.car.x, self.car.y), (end_x, end_y), 1)
            pygame.draw.circle(surface, BLACK, (int(end_x), int(end_y)), 3)
