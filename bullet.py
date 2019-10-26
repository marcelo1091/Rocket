import pygame
from pygame.math import Vector2

class Bullet(object):
    def __init__(self, game):
        self.game = game
        self.player = game.player
        self.createBullet = False
        self.bullets = []
        self.size = self.game.screen.get_size()

    def tick(self):
        #Set bullet Speed
        for b in range(len(self.bullets)):
            self.bullets[b][0] += -self.bullets[b][2].y * 2
            self.bullets[b][1] += self.bullets[b][2].x * 2

        #Remove bullet
        for bullet in self.bullets[:]:
            if bullet[0] < 0 or \
               bullet[0] > self.size[0] or \
               bullet[1] < 0 or \
               bullet[1] > self.size[1]:
                self.bullets.remove(bullet)

    def draw(self):
        for bullet in self.bullets:
            pygame.draw.rect(self.game.screen,(255,0,0), pygame.Rect(bullet[0], bullet[1], 0, 0))