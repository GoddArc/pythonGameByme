import pygame
import random
from settings import *
from score import *
pygame.mixer.init()

score_=Score()
ret=retry()
pseudo_score=0
class Tile(pygame.sprite.Sprite):
    def __init__(self,posx):
        super().__init__()
        self.image=random.choice([tile2,tile1,tile3])
        self.rect=self.image.get_rect()
        self.rect.x=posx
        self.rect.y=random.randrange(-Gameheight,-200)
        self.speed=4
        
    def update(self):
        global pseudo_score
        self.rect.y+=self.speed
        if self.rect.y>Gameheight:
            self.rect.y=random.randrange(-Gameheight,-200)
        mos_pos=pygame.mouse.get_pos()
        mouse_click=pygame.mouse.get_pressed()
        if mouse_click[0]:
            if self.rect.collidepoint(mos_pos):
                self.kill()
                tile_group.add(Tile(self.rect.x))
                score_.update()
                pseudo_score+=1
        score_.draw()
        for i in range(1,20):
            if pseudo_score>=i*10 and pseudo_score<(i+1)*10:
                self.speed=i+4
        if pygame.sprite.spritecollide(self,Endline_group,False):
            tile_group.add(Tile(self.rect.x))
            pseudo_score=0
            score_.scorereset()