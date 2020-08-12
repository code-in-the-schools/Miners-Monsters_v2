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
    self.rect = pygame.Rect(self.x,self.y,self.Length, self.Thickness)
   
    self.colour = (0,0,0)

  def draw(self,screen,colour,Length, Thickness):
    self.image = pygame.transform.scale(self.image,(Length, Thickness))
    self.Length = int(Length)
    self.Thickness = int(Thickness)
    self.rect = pygame.Rect(self.x,self.y,self.Length, self.Thickness)
    self.colour = colour
    pygame.draw.Rect(screen, self.colour, self.rect)


 # def collision(self, obj):
    #print("col " + str(self.Length), str(self.Thickness))
    #print("col" + str(obj.center))
  #  if obj.center[0] >= self.x and obj.center[0] <= self.x+self.Length:
   #   if obj.center[1] <= self.y +1 or obj.center[1] >= self.y -1 :
    #    return True
     # else:
      #  return False
    #else:
     # return False
  