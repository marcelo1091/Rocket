import pygame, math
from pygame.math import Vector2

class Enemy_bullets(object):
    def __init__(self, game):
        self.game = game
        self.player = game.player
        self.bullets = []
        self.size = self.game.screen.get_size()
        self.bullet_radius = 2

    def remove_bullet_on_borders(self):
        for bullet in self.bullets[:]:
            if bullet[0] < 0 or \
               bullet[0] > self.size[0] or \
               bullet[1] < 0 or \
               bullet[1] > self.size[1]:
                self.bullets.remove(bullet)

    def tick(self):




        # Set bullet Speed
        for b in range(len(self.bullets)):
            #angle = math.atan2(self.bullets[b][2].x, self.bullets[b][2].y)
            angle = (180 / math.pi) * -math.atan2(self.bullets[b][2].x, self.bullets[b][2].y)
            self.direction = Vector2(1, 0).rotate(angle)
            self.bullets[b][0] += -self.direction.y * 2
            self.bullets[b][1] += self.direction.x * 2

        # Remove bullet
        self.remove_bullet_on_borders()

    def draw(self):
        for bullet in self.bullets:
            pygame.draw.circle(self.game.screen, (255, 0, 0), (int(bullet[0]), int(bullet[1])), 3)