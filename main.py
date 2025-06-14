import sys
import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField


def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Groups
    asteroids = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    # Add groups to player containers
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)

    # Players
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    # Asteroids
    asteroidfield = AsteroidField()

    # Add to groups
    drawable.add(player)
    updatable.add(player)
    updatable.add(asteroidfield)
    asteroids.add(asteroidfield)

    redraw = True
    while redraw:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0, 0, 0))
        updatable.update(dt)
        for item in drawable:
            item.draw(screen)
        for asteroid in asteroidfield.spawnedList:
            if player.collission(asteroid):
                print("Game Over!")
                sys.exit()
        pygame.display.flip()
        deltaTime = clock.tick(60)  # Pass for 1/60th of a second
        dt = deltaTime / 1000
        # Convert milliseconds to seconds


if __name__ == "__main__":
    main()
