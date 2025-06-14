import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS, ASTEROID_MAX_RADIUS


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(
            screen, (255, 255, 255), self.position, self.radius, self.radius * 2
        )

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        angle = random.uniform(20, 50)
        velocity1 = self.velocity.rotate(-angle)
        velocity2 = self.velocity.rotate(angle)
        radius = self.radius - ASTEROID_MIN_RADIUS
        a1 = Asteroid(self.position.x, self.position.y, radius)
        a1.velocity = velocity1 * 1.2
        a2 = Asteroid(self.position.x, self.position.y, radius)
        a2.velocity = velocity2 * 1.2
        self.containers[0].add(a1)
        self.containers[0].add(a2)
