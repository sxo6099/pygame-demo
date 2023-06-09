# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import pygame
import Player

RESOURCE_PATH = './resources/'

class projectile(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.movex = 0  # move along X
        self.movey = 0  # move along Y
        self.frame = 0  # count frames
        self.images = []
        img = pygame.image.load(RESOURCE_PATH + 'blob.png')
        self.images.append(img)
        self.image = self.images[0]
        self.rect = self.image.get_rect()
    def control(self, x, y):
        """
        control player movement
        """
        self.movex = x
        self.movey = y
    def update(self):
        """
        Update sprite position
        """
        self.rect.x = self.movex
        self.movex = 0;
        self.rect.y = self.movey
        self.movey = 0;
