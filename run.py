import pygame, sys
from rocket import  Rocket

class Game(object):

    def __init__(self):
        # Config
        self.max_tps = 100.0
        self.resolution = [1000,600]

        #Init
        pygame.init()
        self.screen = pygame.display.set_mode(self.resolution)
        self.tps_clock = pygame.time.Clock()
        self.tps_delta = 0.0

        self.player = Rocket(self)

        while True:
            # Events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit(0)
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    sys.exit(0)

            # Ticking
            self.tps_delta += self.tps_clock.tick() / 1000.0
            while self.tps_delta > 1 / self.max_tps:
                self.tick()
                self.tps_delta -= 1 / self.max_tps

            # Rendering
            self.screen.fill((0, 0, 0))
            self.draw()
            pygame.display.flip()


    def tick(self):
        self.player.tick()

    def draw(self):
        self.player.draw()

if __name__ == "__main__":
    Game()






