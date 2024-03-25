import pygame
GameHeight=500
GameWidth=700
FPS=24
#worldShift_speed=5
#playerDash

cloud_portion=100
Screen=pygame.display.set_mode((GameWidth,GameHeight))
Clock=pygame.time.Clock()
Character_frame_list=[]
#groups
cloud_group1=pygame.sprite.Group()
cloud_group2=pygame.sprite.Group()
platform_group=pygame.sprite.Group()
Tree_group=pygame.sprite.Group()
Character_group=pygame.sprite.Group()
Obstacle_group=pygame.sprite.Group()
Mountain_group=pygame.sprite.Group()
sun_group=pygame.sprite.Group()
#images
Backdrop=pygame.transform.scale(pygame.image.load('endlessRun/Export/background.png').convert(),(GameWidth,GameHeight))
cloud1=pygame.transform.scale(pygame.image.load('endlessRun/Export/cloud1.png'),(300,300))
cloud2=pygame.transform.scale(pygame.image.load('endlessRun/Export/cloud2.png'),(400,400))
cloud3=pygame.transform.scale(pygame.image.load('endlessRun/Export/cloud3.png'),(200,200))
cloud4=pygame.transform.scale(pygame.image.load('endlessRun/Export/cloud4.png'),(500,500))
platform=pygame.transform.scale(pygame.image.load('endlessRun/Export/tile.png'),(50,50))
tree=pygame.image.load('endlessRun/Export/tree.png')

for i in range (1,5):
    Character=pygame.transform.scale(pygame.image.load(f'endlessRun/Character/run/frame-{i}.png'),(50,80))
    Character_frame_list.append(Character)
jump_up=pygame.transform.scale(pygame.image.load('endlessRun/Character/jump up/frame.png'),(50,80))
jump_fall=pygame.transform.scale(pygame.image.load('endlessRun/Character/jump fall/frame.png'),(50,80))
slide=pygame.transform.scale(pygame.image.load('endlessRun/Character/sliding/frame.png'),(80,50))
Stone=pygame.transform.scale(pygame.image.load('endlessRun/obstacle/1.png'),(40,40))
mountain=pygame.transform.scale(pygame.image.load('endlessRun/Export/mountain.png'),(GameWidth,GameHeight))
sun=pygame.transform.scale(pygame.image.load('endlessRun/Export/sun.png'),(50,50))