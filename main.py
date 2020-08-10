import pygame
import os
import plat

img_path = os.path.join("player.png")

 #movement
class Player(object):
  def __init__(self):
    #load sprite
    pygame.sprite.Sprite.__init__(self)
    Player.image = pygame.image.load("player.png")
    self.image = Player.image
    self.image = pygame.transform.scale(self.image,(50, 50))
    self.x = 50 
    self.y = 50

  def draw(self, surface):
    surface.blit(self.image, (self.x, self.y))

  def movement(self):
    key = pygame.key.get_pressed()
    if key[pygame.K_DOWN]:
      self.y += 1
    if key[pygame.K_UP]:
      self.y -= 2
    if key[pygame.K_LEFT]:
      self.x -= 1
    if key[pygame.K_RIGHT]:
      self.x += 1

  def gravity(self, height):
    if self.y < height - 50 and pygame.key.get_focused:
      self.y += 1


pygame.init()
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((int(screen_width),int(screen_height)))

p = Player()
pf = plat.Platform()

running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      running = False
  
  screen.fill((255, 255, 255))
  p.draw(screen)
  p.movement()
  p.gravity(screen_height)
  pf.draw(screen)
  pygame.display.update()