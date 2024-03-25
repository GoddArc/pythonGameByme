from settings import *
import pygame
class EndScreen:
    def __init__(self):
        pygame.init()
        self.Rect=pygame.Rect(100,100,200,100)
        self.Rect.center=Screen_rect.center
        self.Rect2=pygame.Rect(100,100,205,105)
        self.Rect2.center=Screen_rect.center
    def draw(self,word1,word2):
        pygame.draw.rect(Screen,'grey',self.Rect2,border_radius=30)
        pygame.draw.rect(Screen,(43, 45, 48),self.Rect,border_radius=30)
        self.text(word1,word2)
    def text(self,word1,word2):
        Text=FONT.render(word1,True,'white')
        Text_rect=Text.get_rect()
        Text_rect.center=self.Rect.center
        Text2=FONT.render(word2,True,'white')
        Text_rect2=Text2.get_rect()
        Text_rect2.center=self.Rect.center
        Screen.blit(Text,(Text_rect.x,Text_rect.y-15))
        Screen.blit(Text2,(Text_rect2.x,Text_rect2.y+15))
class Logo:
    def __init__(self):
        self.image=logo
        self.Rect=self.image.get_rect()
        self.Rect.center=Screen_rect.center
        
    def draw(self):
        Screen.blit(self.image,(self.Rect.x,self.Rect.y-230))