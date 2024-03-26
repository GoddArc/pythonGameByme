from settings import *
import pygame
import os

file=open('highscore.txt','r')
high=file.read()
highscore=int(high)

pygame.init()

class Score():
    def __init__(self):
        self.Font=pygame.font.Font(None,100)
        self.Font2=pygame.font.Font(None,50)
        self.counter=0
        self.text=f'{highscore}'
    def draw(self):
        
        self.Text=self.Font.render(f'{self.counter}',True,'blue')
        self.Rect=self.Text.get_rect()
        self.Rect.center=(Gamewidth//2,Gameheight//2)
        self.Text2=self.Font2.render(f'{self.text}',True,'skyblue')
        self.Rect2=self.Text.get_rect()
        self.Rect2.center=(Gamewidth//2,Gameheight-10)
        
        Screen.blit(self.Text,self.Rect)
        Screen.blit(self.Text2,self.Rect2)
    
    def update(self):
        self.counter+=1
        if self.counter>highscore:
            score__=str(self.counter)
            change=open('highscore.txt','w')
            change.write(score__)
            self.text=str(self.counter)
        else:
            self.text=f'{highscore}'
        high=file.read()
    def scorereset(self):
        global highscore
        self.counter=0
        file=open('highscore.txt','r')
        high=file.read()
        highscore=int(high)


class retry():
    def __init__(self):
        self.Font=pygame.font.Font(None,50)
        self.Text=self.Font.render('Try again ?',False,'black')
        self.Rect=self.Text.get_rect()
        self.Rect.center=(Gamewidth//2,Gameheight//2)
        
    def draw(self,Gameplay):
        Screen.blit(self.Text,self.Rect)
        mos_pos=pygame.mouse.get_pos()
        mouse=pygame.mouse.get_pressed()
        if self.Rect.collidepoint(mos_pos) and Gameplay==1:
            if mouse[0]:
                pygame.sprite.groupcollide(tile_group,Endline_group,True,False)
                return 0
