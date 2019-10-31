import pygame
from pygame.math import Vector2

class Rocket(object):

    def __init__(self, game):
        self.game = game
        self.airResistance = 0.9
        self.speed = 0.1
        self.gravity = 0.0

        self.pos = Vector2(self.size[0]/2,self.size[1]/2)
        self.vel = Vector2(0,0)
        self.acc = Vector2(0,0)
        self.angle = Vector2(0,0)
        self.direction = Vector2(1,0)

    def add_force(self, force):
        self.acc += force

    def border_collision(self):
        if self.pos.x+20 >= self.game.screen_size[0] or \
          self.pos.x-20 <= 0 or \
          self.pos.y+20 >= self.game.screen_size[1] or \
          self.pos.y-20 <= 0:
            self.pos = Vector2(self.game.screen_size[0]/2,self.game.screen_size[1]/2)

    def physic(self):
        self.vel *= self.airResistance
        self.vel -= Vector2(0, -self.gravity)

        self.vel += self.acc
        self.pos += self.vel
        self.acc *= 0

    def input(self):
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_w]:
            self.add_force(Vector2(0,-self.speed))
        if pressed[pygame.K_s]:
            self.add_force(Vector2(0,self.speed))
        if pressed[pygame.K_a]:
            self.add_force(Vector2(-self.speed,0))
        if pressed[pygame.K_d]:
            self.add_force(Vector2(self.speed,0))


    def updte(self):
        # Input
        self.input()

        # Physics
        self.physic()

        # Get directiion
        self.direction = Vector2(1,0).rotate(-self.angle)

        #Check border collision
        self.border_collision()

    def draw(self):
        # Base triangle
        points = [Vector2(0,-10), Vector2(5,5), Vector2(-5,5)]

        # Rotate points
        self.angle = self.vel.angle_to(Vector2(0,1))
        points = [p.rotate(self.angle) for p in points]

        #Fix y axis
        points = [Vector2(p.x,p.y*-1) for p in points]

        # Add current position
        self.points = [Vector2(self.pos+p*2) for p in points]

        #Draw triangle
        pygame.draw.polygon(self.game.screen, (0,100,255), self.points)


