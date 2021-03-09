import pygame
import os
import sys


class GetImage:
    def __init__(self, name, size=None, colorkey=None):
        self.name = name
        self.colorkey = colorkey
        self.size = size

    def load_image(self):
        fullname = os.path.join('Resources', self.name)
        if not os.path.isfile(fullname):
            print(f"Файл с изображением '{fullname}' не найден")
            sys.exit()
        image = pygame.image.load(fullname)
        if self.size:
            image = pygame.transform.scale(image, self.size)
        return image
