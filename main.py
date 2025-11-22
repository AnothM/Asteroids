# This allows us to use code from the open-source
# pygame library throughout this file
import sys
from logger import log_state
import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
from logger import log_event


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    print("Starting Asteroids")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    # setup player start position
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    
    # setup sprite groups
    asteroids = pygame.sprite.Group()
    updatable = pygame.sprite.Group() 
    drawable = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    # add classes to sprite groups
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    Shot.containers = (shots, updatable, drawable)

    
    # create objects
    asteroid_field = AsteroidField()
    player_instance = Player(x, y)
    
    #Game loop
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
        screen.fill("black")
        updatable.update(dt)
        for i in asteroids:
            if player_instance.collides_with(i):
                log_event("player_hit")
                print("Game over!")
                sys.exit() 
        for j in asteroids:
            for i in shots:
                if i.collides_with(j):
                    j.split()
                    i.kill()
                    log_event("asteroid_shot")
        for obj in drawable:
            obj.draw(screen)
        pygame.display.flip()
        #delta time
        dt = clock.tick(60) / 1000.0





if __name__ == "__main__":
    main()
