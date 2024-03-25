import pygame
from settings import *
pygame.init()
Font=pygame.font.SysFont('Comicsans',30)

class Score:
    def __init__(self,number):
        self.text=number
    def draw(self):
        self.ShowText=Font.render(f'{int(self.text)}m',True,'black')
        self.Rect=self.ShowText.get_rect()
        self.Rect.x=10
        self.Rect.y=10
        Screen.blit(self.ShowText,self.Rect)
    def update(self):
        self.text+=0.01

class Retry:
    def __init__(self):
        self.Rect_retry=pygame.Rect(200,100,130,50)
        self.ScreenRect=Screen.get_rect()
        self.Rect_retry.center=self.ScreenRect.center
        self.label=Font.render('Retry',False,'black')
        self.label_rect=self.label.get_rect()
        self.label_rect.center=self.Rect_retry.center
    def Draw(self):
        pygame.draw.rect(Screen,'green',self.Rect_retry,border_radius=20)
        Screen.blit(self.label,self.label_rect)
    
    def update(self):
        var=-1
        mos_pos=pygame.mouse.get_pos()
        mos_pressed=pygame.mouse.get_pressed()
        if self.Rect_retry.collidepoint(mos_pos):
            if mos_pressed[0]==True:
                var=0
                
            else:
                var=-1
        return var