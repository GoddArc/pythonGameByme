import pygame
Gamewidth=340
Gameheight=600
Screen=pygame.display.set_mode((Gamewidth,Gameheight))
clock=pygame.time.Clock()
FPS=60
Tile_width=100
tile_group=pygame.sprite.Group()
Endline_group=pygame.sprite.Group()
#images
tile1=pygame.transform.scale(pygame.image.load('resources/tile1.png'),(Tile_width,150))
tile2=pygame.transform.scale(pygame.image.load('resources/tile2.png'),(Tile_width,150))
tile3=pygame.transform.scale(pygame.image.load('resources/tile3.png'),(Tile_width,150))
bg=pygame.transform.scale(pygame.image.load('resources/Bg.png'),(400,600))
cursor=pygame.image.load('resources/aim.png')