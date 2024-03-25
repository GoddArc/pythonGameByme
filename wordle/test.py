import pygame
import os
import random
pygame.init()
Width=800
Height=600

Screen=pygame.display.set_mode((Width,Height))
Screen_rect=Screen.get_rect()


square_Size=50
No_of_guesses=5
shift=50
row_group1=pygame.sprite.Group()
row_group2=pygame.sprite.Group()
row_group3=pygame.sprite.Group()
row_group4=pygame.sprite.Group()
row_group5=pygame.sprite.Group()
row_group6=pygame.sprite.Group()
gap=5
upper_gap=130
word_group=[]#actually its letter group

FONT=pygame.font.SysFont('font2.fon',35)
logo=pygame.transform.scale_by(pygame.image.load('logo.png').convert_alpha(),0.25)