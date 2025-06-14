import pygame

from circleshape import CircleShape

from constants import PLAYER_SHOOT_SPEED


class Shot(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.rotation = 0

    def draw(self, screen):
        pygame.draw.circle(
            screen, (255, 255, 255), self.position, self.radius, self.radius * 2
        )

    def update(self, dt):
        self.position += self.velocity * dt
