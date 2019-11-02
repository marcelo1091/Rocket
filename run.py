import pygame, sys
from rocket import Rocket
from bullet import Bullet
from  enemy import Enemy
from enemy_bullet import Enemy_bullets

class Game(object):

    def __init__(self):
        # Config
        self.max_fps = 100.0
        self.resolution = [800,600]

        #Init
        pygame.init()
        self.screen = pygame.display.set_mode(self.resolution)
        self.screen_size = self.screen.get_size()
        self.fps_clock = pygame.time.Clock()
        self.fps_delta = 0.0

        self.player = Rocket(self)
        self.bullet = Bullet(self)
        self.enemy = Enemy(self)
        self.enemy_bullet = Enemy_bullets(self)

        while True:
            # Events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit(0)
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    sys.exit(0)
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    self.bullet.bullets.append([self.player.pos.x - (self.player.direction.y * 17), 
                    self.player.pos.y + (self.player.direction.x * 17), 
                    self.player.direction])
            # Set Max Fps
            self.fps_delta += self.fps_clock.tick() / 1000.0
            while self.fps_delta > 1 / self.max_fps:
                self.update()
                self.fps_delta -= 1 / self.max_fps

            # Rendering
            self.screen.fill((0, 0, 0))
            self.draw()
            pygame.display.flip()

    def update(self):
        self.player.update()
        self.bullet.update()
        self.enemy.update()
        self.enemy_bullet.tick()

    def draw(self):
        self.player.draw()
        self.bullet.draw()
        self.enemy.draw()
        self.enemy_bullet.draw()

if __name__ == "__main__":
    Game()






