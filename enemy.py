import pygame, random
from pygame.math import Vector2

class Enemy(object):
    def __init__(self, game):
        self.game = game
        self.bullet = game.bullet
        self.enemies = []

    def spawn_enemy(self):
        self.enemies.append([random.randint(10,self.game.screen_size[0] - 10), random.randint(1,self.game.screen_size[1] - 10), random.uniform(1.8,2.4)])

    def remove_enemy(self):
        for e in range(len(self.enemies)):
            for b in range(len(self.bullet.bullets)):
                if self.enemies[e].rect.colliderect(self.bullet.bullets[b].rect):
               # if self.bullet.bullets[b][0] - self.bullet.bullet_radius < self.enemies[e][0] + 20 and \
                #        self.bullet.bullets[b][0] + self.bullet.bullet_radius > self.enemies[e][0]:
                 #   if self.bullet.bullets[b][1] + self.bullet.bullet_radius > self.enemies[e][1] and \
                  #          self.bullet.bullets[b][1] - self.bullet.bullet_radius < self.enemies[e][1] + 20:
                        self.enemies.remove(self.enemies[e])
                        self.bullet.remove_bullet(self.bullet.bullets[b])
                        break

    def update(self):
        self.remove_enemy()

        if len(self.enemies) < 6:
            self.spawn_enemy()

        for e in range(len(self.enemies)):
            self.enemies[e][2] -= 0.01
            if self.enemies[e][2] <= 0:
                rel_x = self.game.player.pos.x - self.enemies[e][0]
                rel_y = self.game.player.pos.y - self.enemies[e][1]
                self.game.enemy_bullet.bullets.append([self.enemies[e][0], self.enemies[e][1], Vector2(rel_x, rel_y)])
                self.enemies[e][2] = random.uniform(1.8, 2.4)

    def draw(self):
        for enemy in self.enemies:
            pygame.draw.rect(self.game.screen, (255, 0, 0), pygame.Rect(enemy[0], enemy[1], 20, 20))
