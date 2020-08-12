import pygame

class Platform(object):
    def __init__(self, colour, rect):
        self.colour = colour
        self.Rect = rect

    def draw(self, screen):
        pygame.draw.rect(screen, self.colour, self.Rect)
