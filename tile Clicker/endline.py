import pygame
from settings import *
class Endline(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=pygame.Surface((Gamewidth,5))
        self.image.fill('red')
        self.rect=self.image.get_rect()
        self.rect.x=0
        self.rect.y=Gameheight-5