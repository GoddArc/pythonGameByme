import pygame
import sys
from settings import *
from backdrop import *
from character import Show_character
from obstacles import Obstacles
from score import *
pygame.init()
from pygame import mixer
#sounds
mixer.init()

bG_music=mixer.music.load('endlessRun/sounds/bg sound.mp3')

mixer.music.set_volume(0.1)
mixer.music.play(-1)
Death_music=False
go=False
temp=10
Velo=temp
waiter=0
worldShift_speed=5
Gamplay=0
#groups
for i in range(3):
    cloud_group1.add(Cloud1())
for i in range(3):
    cloud_group2.add(Cloud2())
for i in range(3):
    cloud_group1.add(Cloud3())
for i in range(3):
    cloud_group2.add(Cloud4())
    
for i in range (28):
    platform_group.add(Platform(i*50))
    #1400->28
for i in range (5):
    Tree_group.add(Tree())
    
Character_group.add(Show_character())
for i in range (3):
    Obstacle_group.add(Obstacles())
    
Show_score=Score(0)
retry=Retry()
    
    
Mountain_group.add(Mountain())
Mountain_group.add(Mountain())
Mountain_group.add(Mountain())

sun_group.add(Sun())
while True:
    for events in pygame.event.get():
        if events.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
        key1=pygame.key.get_pressed()
        if key1[pygame.K_LCTRL]:
            Swush=mixer.Sound('endlessRun/sounds/swush sound.mp3')
            Swush.play()
            go=True
        #if key1[pygame.K_SPACE]:
            #huh=mixer.Sound('endlessRun/sounds/jump sound.mp3')
            #huh.play()
    #backdrop
    Screen.blit(Backdrop,(0,0))
    #key_presses
    key=pygame.key.get_pressed()
    #if key[pygame.K_LSHIFT]:
    #    go=True
    if go==True:
        worldShift_speed+=Velo
        Velo-=1
        if Velo<5:
            worldShift_speed=5
            Velo=temp
            go=False
    #Sprites
    sun_group.draw(Screen)
    cloud_group1.draw(Screen)
    Mountain_group.draw(Screen)
    cloud_group2.draw(Screen)
    platform_group.draw(Screen)
    Tree_group.draw(Screen)
    Character_group.draw(Screen)
    
    #update
    if Gamplay==0:
        
        sun_group.update()
        Mountain_group.update()
        cloud_group1.update(worldShift_speed)
        cloud_group2.update(worldShift_speed)
        platform_group.update(worldShift_speed)
        Tree_group.update(worldShift_speed)
        Character_group.update()
        Obstacle_group.update(worldShift_speed)
        Show_score.update()
        Obstacle_group.draw(Screen)
        Show_score.draw()
    elif Gamplay==-1:
        if Death_music==False:
            mixer.music.stop()
            Death_music=mixer.Sound('endlessRun/sounds/death sound.wav')
            Death_music.play()
            Death_music=True
        key0=pygame.key.get_pressed()
        retry.Draw()
        Show_score=Score(0)
        Gamplay=retry.update()
        if key0[pygame.K_LSHIFT]:
            Gamplay=0
        if Gamplay==0:
            mixer.music.play()
        
    if pygame.sprite.groupcollide(Character_group,Obstacle_group,False,True):
        Obstacle_group.add(Obstacles())
        Death_music=False
        Gamplay=-1
    pygame.display.update()
    Clock.tick(FPS)