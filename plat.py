import pygame
import os

img_path = os.path.join("Player.png")

class Platform(pygame.Rect):
    def __init__(self):
      pygame.sprite.Sprite.__init__(self)
      Platform.image = pygame.image.load("Player.png")
      self.image = Platform.image
      self.y = 70 
      self.x = 70 
      self.Length = 0
      self.Thickness = 0
      self.rect = pygame.rect(self.x,self.y,self.Length, self.Thickness)

    def draw(self,surface,Length, Thickness, colour, screen):
     self.image = pygame.transform.scale(self.image,(Length,Thickness))
     self.Length = int(Length)
     self.Thickness = int(Thickness)
     self.rect = pygame.Rect(self.x,self.y,self.Length, self.Thickness)
     self.colour = colour
     pygame.draw.rect(screen, self.colour, self.rect)