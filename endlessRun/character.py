import pygame
from settings import *
class Show_character(pygame.sprite.Sprite):
    
    def __init__(self):
        super().__init__()
        self.image=Character_frame_list[0]
        self.rect=self.image.get_rect()
        self.rect.bottom=GameHeight-50
        self.rect.x=100
        self.index=1
        self.delay=0
        self.jumpHeight=12
        self.velo=-self.jumpHeight
        self.pressed=False
        self.dash=False
        self.Gameplay=0
    def update(self):
        if self.Gameplay==0:
            key_pressed=pygame.key.get_pressed()
            if key_pressed[pygame.K_SPACE]:
                self.pressed=True
            if key_pressed[pygame.K_LCTRL]:
                self.dash=True
            if self.pressed==True:
                self.rect.y+=self.velo
                self.velo+=1
                if self.velo<0:
                    self.image=jump_up
                if self.velo>0:
                    self.image=jump_fall
                if self.velo>self.jumpHeight:
                    self.velo=-self.jumpHeight
                    self.pressed=False
            elif self.pressed==False:
                self.image=Character_frame_list[self.index]
                if self.delay==1:
                    self.index+=1
                    self.delay=0
                self.delay+=0.25
                if self.index>3:
                    self.index=0
            if self.dash==True:
                self.image=slide
                self.dash=False
    