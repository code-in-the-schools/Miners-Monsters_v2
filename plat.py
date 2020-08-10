import pygame
import os

class Platform(object):
  def __init__(self):
    pygame.sprite.Sprite.__init__(self)
    Platform.image = pygame.image.load("player.png")
    self.image = Platform.image
    self.image = pygame.transform.scale(self.image,(150,70))
    self.y = 70 
    self.x = 70 
    self.hitbox = (self.x,self.y,55,55)

  def draw(self,surface):
   surface.blit(self.image, (self.x, self.y))