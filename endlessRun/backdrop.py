import pygame
from settings import *
import random
from character import Show_character
        

class Cloud1(pygame.sprite.Sprite):
    def __init__(self,):
        super().__init__()
        self.image=cloud1
        self.rect=self.image.get_rect()
        self.rect.x=(random.randint(GameWidth,GameWidth*2))
        self.rect.y=random.randint(0,cloud_portion)
    def update(self,worldShift_speed):
        self.rect.x-=worldShift_speed-2
        if self.rect.x<-300:
            self.rect.x=(random.randint(GameWidth,GameWidth*2))
            self.rect.y=random.randint(0,cloud_portion)
            
class Cloud2(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=cloud2
        self.rect=self.image.get_rect()
        self.rect.x=(random.randint(GameWidth,GameWidth*2))
        self.rect.y=random.randint(0,cloud_portion)
        
    def update(self,worldShift_speed):
        self.rect.x-=worldShift_speed-2
        if self.rect.x<-400:
            self.rect.x=(random.randint(GameWidth,GameWidth*2))
            self.rect.y=random.randint(0,cloud_portion)
            
class Cloud3(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=cloud3
        self.rect=self.image.get_rect()
        self.rect.x=(random.randint(GameWidth,GameWidth*2))
        self.rect.y=random.randint(0,cloud_portion)
    def update(self,worldShift_speed):
        self.rect.x-=worldShift_speed-2
        if self.rect.x<-200:
            self.rect.x=(random.randint(GameWidth,GameWidth*2))
            self.rect.y=random.randint(0,cloud_portion)
            
class Cloud4(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=cloud4
        self.rect=self.image.get_rect()
        self.rect.x=(random.randint(GameWidth,GameWidth*2))
        self.rect.y=random.randint(0,cloud_portion)
    def update(self,worldShift_speed):
        self.rect.x-=worldShift_speed-2
        if self.rect.x<-500:
            self.rect.x=(random.randint(GameWidth,GameWidth*2))
            self.rect.y=random.randint(0,cloud_portion)
            
class Platform(pygame.sprite.Sprite):
    def __init__(self,x):
        super().__init__()
        self.image=platform
        self.rect=self.image.get_rect()
        self.rect.bottom=GameHeight
        self.rect.x=x
    def update(self,worldShift_speed):
        self.rect.x-=worldShift_speed
        if self.rect.x<-50:
            self.rect.x=GameWidth*2-(45+worldShift_speed)
            

class Tree(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.size=random.randint(150,250)
        self.sizey=random.randint(200,400)
        self.image=pygame.transform.scale(tree,(self.size,self.sizey))
        self.rect=self.image.get_rect()
        self.rect.bottom=GameHeight-50
        self.rect.x=random.randint(GameWidth,GameWidth*2)
    
    def update(self,worldShift_speed):
        self.rect.x-=worldShift_speed
        if self.rect.x<(-1)*(self.size):
            self.size=random.randint(150,250)
            self.sizey=random.randint(200,400)
            self.rect.x=random.randint(GameWidth,GameWidth*2)
    
class Mountain(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=mountain
        self.rect=self.image.get_rect()
        self.rect.bottom=GameHeight-50
        self.rect.x=random.randint(GameWidth,GameWidth*2)
    def update(self):
        self.rect.x-=1
        if self.rect.x<GameWidth*-1:
            self.rect.x=random.randint(GameWidth,GameWidth*2)

class Sun(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=sun
        self.rect=self.image.get_rect()
        self.rect.bottom=100
        self.rect.x=random.randint(GameWidth,GameWidth+100)
        self.doop=0
    def update(self):
        self.doop+=0.2
        if self.doop==1:
            self.rect.x-=1
            self.doop=0
        if self.rect.x<GameWidth*-1:
            self.rect.x=random.randint(GameWidth,GameWidth+100)
