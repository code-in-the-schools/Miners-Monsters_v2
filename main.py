import pygame
import os
import plat

img_path = os.path.join("Player.png")

 #movement
class Player(object):
  def __init__(self):
    #load sprite
    pygame.sprite.Sprite.__init__(self)
    Player.image = pygame.image.load("Player.png")
    self.image = Player.image
    self.image = pygame.transform.scale(self.image,(50, 50))
    self.x = 50 
    self.y = 50
    self.dy = 0
    self.rect = pygame.Rect(self.x,self.y,50,50)

    self.center = (25+self.x,50+self.y)
    self.isGrounded = False

  def draw(self, surface):
    surface.blit(self.image, (self.x, self.y))

  def movement(self):
    self.center = (25+self.x,50+self.y)
    key = pygame.key.get_pressed()
    if key[pygame.K_DOWN]:
      self.y += 1
    if key[pygame.K_UP]:
      self.y -= 2
    if key[pygame.K_LEFT]:
      self.x -= 1
    if key[pygame.K_RIGHT]:
      self.x += 1

  def isStanding(self, platform):
    return (pygame.Rect(self.rect.x, self.rect.y + self.dy+1,50, 50).collidelist(platform)) 

  def dogravity(self, height, platforms):
    print("Grav " + str(self.isGrounded))
    if self.y < height - 50 and pygame.key.get_focused:
      for platform in platforms:
        print(self.isStanding(platform))
        if self.isStanding(platform) >= 0:
          self.isGrounded = True
          #break;
        else:
          self.isGrounded = False

    if self.isGrounded == False:
      self.y +=1
        
      

  





pygame.init()
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((int(screen_width),int(screen_height)))

p = Player()
platform1 = plat.Platform((0, 255, 255), 40, 100, 100, 10)
platform2 = plat.Platform((0, 255, 255), 150, 150, 100, 10)
platforms = [platform1.Rect, platform2.Rect]
running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      running = False
  
  screen.fill((255, 255, 255))
  p.draw(screen)
  p.movement()
  print(str(p.isStanding(platforms))+ " <<<<<")
  p.dogravity(screen_height, platforms)
  platform1.draw(screen)
  platform2.draw(screen)
  print(p.center)
  pygame.display.update()