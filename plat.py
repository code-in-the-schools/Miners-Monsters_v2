import pygame
import os

class Platform(object):
  def __init__(self):
    pygame.sprite.Sprite.__init__(self)
    Platform.image = pygame.image.load("player.png")
    self.image = Platform.image
    self.y = 70 
    self.x = 70 
    self.Length = 0
    self.Thickness = 0
    self.hitbox = (self.x,self.y,55,55)

  def draw(self,surface,Length, Thickness):
   surface.blit(self.image, (self.x, self.y))
   self.image = pygame.transform.scale(self.image,(Length,Thickness))
   self.Length = int(Length)
   self.Thickness = int(Thickness)

  def collision(self, obj):
    #print("col " + str(self.Length), str(self.Thickness))
    #print("col" + str(obj.center))
    if obj.center[0] >= self.x and obj.center[0] <= self.x+self.Length:
      if obj.center[1] <= self.y +1 or obj.center[1] >= self.y -1 :
        obj.isOnGround()
        print("HIT")
      else:
        obj.isOffGround()
    else:
      obj.isOffGround()