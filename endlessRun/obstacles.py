import pygame
import random
from settings import *
class Obstacles(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=Stone
        self.rect=self.image.get_rect()
        self.rect.bottom=GameHeight-50
        self.rect.x=random.randint(GameWidth,GameWidth*2)
        self.Gameplay=0
    def update(self,worldShift_speed):
        if self.Gameplay==0:
            self.rect.x-=worldShift_speed
            if self.rect.x<-50:
                self.rect.x=random.randint(GameWidth,GameWidth*2)