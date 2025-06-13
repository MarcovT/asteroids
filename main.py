import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from player import Player


def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Players
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    # Groups
    updatable = pygame.sprite.Group()
    updatable.add(player)
    drawable = pygame.sprite.Group()
    drawable.add(player)

    # Add groups to player containers
    Player.containers = (updatable, drawable)

    redraw = True
    while redraw:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0, 0, 0))
        updatable.update(dt)
        for item in drawable:
            item.draw(screen)
        pygame.display.flip()
        deltaTime = clock.tick(60)  # Pass for 1/60th of a second
        dt = deltaTime / 1000
        # Convert milliseconds to seconds


if __name__ == "__main__":
    main()
