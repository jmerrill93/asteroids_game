import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    pygame.init()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    #screen setup
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Asteroids: A Project by BootDev")
    
    #time clock
    clock = pygame.time.Clock()
    dt = 0

    #groups
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    astroids = pygame.sprite.Group()

    #add player to groups
    Player.containers = (updateable, drawable)
    Asteroid.containers = (updateable, drawable, astroids)
    AsteroidField.containers = (updateable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroidfield = AsteroidField()

    #main loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        

        updateable.update(dt)

        screen.fill("black")
        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()

        #limit to 60 FPS
        dt = clock.tick(60) / 1000.0

if __name__ == "__main__":
    main()