import pygame
from settings import *
import sys
from tile import Tile
from score import *
from endline import Endline
Gameplay=0
ret=retry()
#Groups
for i in range (3):
    tile_group.add(Tile(Tile_width*i+20*i))
Endline_group.add(Endline())

click=pygame.mixer.Sound('resources/click2.wav')
    
def collision():
    global Gameplay
    if pygame.sprite.groupcollide(tile_group,Endline_group,False,False):
        Gameplay=ret.draw(Gameplay)
        pygame.mixer.music.play(-1)
#music
pygame.mixer.init()
pygame.mixer.music.load('resources/bg music.mp3')
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.2)
pygame.mouse.set_visible(False)
#gameloop
while True:
    for events in pygame.event.get():
        if events.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
    mouse_click=pygame.mouse.get_pressed()
    #if mouse_click[0]:
    #    continue
        #click.play()
    Screen.blit(bg,(0,0))
    if Gameplay==0:
        tile_group.update()
    tile_group.draw(Screen)
    Endline_group.draw(Screen)
    mos_pos=pygame.mouse.get_pos()
    rect=cursor.get_rect()
    rect.center=mos_pos
    Screen.blit(cursor,rect)
    if Gameplay==1:
        pygame.mixer.music.stop()
        collision()
    if pygame.sprite.groupcollide(tile_group,Endline_group,False,False):
        Gameplay=1
    pygame.display.update()
    clock.tick(FPS)