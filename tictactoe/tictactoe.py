import pygame
from sys import exit
pygame.init()

Screen=pygame.display.set_mode((300,300))
pygame.display.set_caption('TicTacToe')
Clock = pygame.time.Clock()
Intro=pygame.image.load('tictactoe/intro.png').convert_alpha()
RealIntro=pygame.transform.scale(Intro,(300,300))
def draw_rect(rect):
    pygame.draw.rect(Screen,'white',rect)

Rect_1=pygame.Rect(0,0,90,90)
Rect_2=pygame.Rect(105,0,90,90)
Rect_3=pygame.Rect(210,0,90,90)

Recm_1=pygame.Rect(0,105,90,90)
Recm_2=pygame.Rect(105,105,90,90)
Recm_3=pygame.Rect(210,105,90,90)

Recl_1=pygame.Rect(0,210,90,90)
Recl_2=pygame.Rect(105,210,90,90)
Recl_3=pygame.Rect(210,210,90,90)

FONT=pygame.font.SysFont('Comicsans',80)
def placement(xoro,pos_x,pos_y,virtual_step):
    if virtual_step%2==0:
        color1='black'
        Text1=FONT.render(xoro,True,color1)
        Screen.blit(Text1,(pos_x,pos_y))
    else:
        color2='black'
        Text2=FONT.render(xoro,True,color2)
        Screen.blit(Text2,(pos_x,pos_y))
    
x1,x2,x3,x4,x5,x6,x7,x8,x9=" "," "," "," "," "," "," "," "," "
x_positions=[]
o_positions=[]
click_count=0
condition=True

def loop(Rectangle):
    pygame.draw.rect(Screen,'red',Rectangle)
    pygame.display.update()
    while True:
        for events in pygame.event.get():
            if events.type==pygame.QUIT:
                pygame.quit()
                exit()
def dialoop(degree):
    surf=pygame.Surface([415,10]).convert_alpha()
    surf.fill('red')
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                exit()
        rotated=pygame.transform.rotate(surf,degree)
        Screen.blit(rotated,(0,0))
        pygame.display.update()
        
def Check_winner(x_pos,o_pos):
    if set([1,2,3]).issubset(x_pos) or set([1,2,3]).issubset(o_pos):
        Rect=pygame.Rect(0,45,300,5)
        loop(Rect)
    if set([4,5,6]).issubset(x_pos) or set([4,5,6]).issubset(o_pos):
        Rect=pygame.Rect(0,45+100,300,5)
        loop(Rect)
    if set([7,8,9]).issubset(x_pos) or set([7,8,9]).issubset(o_pos):
        Rect=pygame.Rect(0,45+200,300,5)
        loop(Rect)
        
    if set([1,5,9]).issubset(x_pos) or set([1,5,9]).issubset(o_pos):
        dialoop(-45)
    if set([3,5,7]).issubset(x_pos) or set([3,5,7]).issubset(o_pos):
        dialoop(45)
    
    if set([1,4,7]).issubset(x_pos) or set([1,4,7]).issubset(o_pos):
        Rect=pygame.Rect(45,0,5,300)
        loop(Rect)
    if set([2,5,8]).issubset(x_pos) or set([2,5,8]).issubset(o_pos):
        Rect=pygame.Rect(45+100,0,5,300)
        loop(Rect)
    if set([3,6,9]).issubset(x_pos) or set([3,6,9]).issubset(o_pos):
        Rect=pygame.Rect(45+200,0,5,300)
        loop(Rect)
intro_check=True
while True:
    while intro_check==True:
        Screen.blit(RealIntro,(0,0))
        pygame.display.update()
        for events in pygame.event.get():
            if events.type==pygame.MOUSEBUTTONDOWN:
                intro_check=False
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            exit()
        mouse_x,mouse_y=pygame.mouse.get_pos()
        if x1==" " and Rect_1.x<=mouse_x<=Rect_1.x+90 and Rect_1.y<=mouse_y<=Rect_1.y+90 and event.type==pygame.MOUSEBUTTONDOWN:
            if click_count%2==0:
                x1="X"
                x_positions.append(1)
            else:
                x1="O"
                o_positions.append(1)
            click_count+=1
        if x2==" " and Rect_2.x<=mouse_x<=Rect_2.x+90 and Rect_2.y<=mouse_y<=Rect_2.y+90 and event.type==pygame.MOUSEBUTTONDOWN:
            if click_count%2==0:
                x2="X"
                x_positions.append(2)
            else:
                x2="O"
            
                o_positions.append(2)
            click_count+=1
        if x3==" " and Rect_3.x<=mouse_x<=Rect_3.x+90 and Rect_3.y<=mouse_y<=Rect_3.y+90 and event.type==pygame.MOUSEBUTTONDOWN:
            if click_count%2==0:
                x3="X"
                
                x_positions.append(3)
            else:
                x3="O"
                
                o_positions.append(3)
            click_count+=1
        if x4==" " and Recm_1.x<=mouse_x<=Recm_1.x+90 and Recm_1.y<=mouse_y<=Recm_1.y+90 and event.type==pygame.MOUSEBUTTONDOWN:
            if click_count%2==0:
                x4="X"
                
                
                x_positions.append(4)
            else:
                x4="O"
                
                o_positions.append(4)
            click_count+=1
        if x5==" " and Recm_2.x<=mouse_x<=Recm_2.x+90 and Recm_2.y<=mouse_y<=Recm_2.y+90 and event.type==pygame.MOUSEBUTTONDOWN:
            if click_count%2==0:
                x5="X"
                
                x_positions.append(5)
            else:
                x5="O"
                
                o_positions.append(5)
            click_count+=1
        if x6==" " and Recm_3.x<=mouse_x<=Recm_3.x+90 and Recm_3.y<=mouse_y<=Recm_3.y+90 and event.type==pygame.MOUSEBUTTONDOWN:
            if click_count%2==0:
                x6="X"
                
                x_positions.append(6)
            else:
                x6="O"
                
                o_positions.append(6)
            click_count+=1
        if x7==" " and Recl_1.x<=mouse_x<=Recl_1.x+90 and Recl_1.y<=mouse_y<=Recl_1.y+90 and event.type==pygame.MOUSEBUTTONDOWN:
            if click_count%2==0:
                x7="X"
                
                x_positions.append(7)
            else:
                x7="O"
                
                o_positions.append(7)
            click_count+=1
        if x8==" " and Recl_2.x<=mouse_x<=Recl_2.x+90 and Recl_2.y<=mouse_y<=Recl_2.y+90 and event.type==pygame.MOUSEBUTTONDOWN:
            if click_count%2==0:
                x8="X"
                
                x_positions.append(8)
            else:
                x8="O"
                
                o_positions.append(8)
            click_count+=1
        if x9==" " and Recl_3.x<=mouse_x<=Recl_3.x+90 and Recl_3.y<=mouse_y<=Recl_3.y+90 and event.type==pygame.MOUSEBUTTONDOWN:
            if click_count%2==0:
                x9="X"
                
                x_positions.append(9)
            else:
                x9="O"
                o_positions.append(9)
            click_count+=1
    Screen.fill('black')
    draw_rect(Rect_1)
    draw_rect(Rect_2)
    draw_rect(Rect_3)
    draw_rect(Recm_1)
    draw_rect(Recm_2)
    draw_rect(Recm_3)
    draw_rect(Recl_1)
    draw_rect(Recl_2)
    draw_rect(Recl_3)
    placement(x1,Rect_1.x+15,Rect_1.y-15,click_count)
    placement(x2,Rect_2.x+15,Rect_2.y-15,click_count)
    placement(x3,Rect_3.x+15,Rect_3.y-15,click_count)
    
    placement(x4,Recm_1.x+15,Recm_1.y-15,click_count)
    placement(x5,Recm_2.x+15,Recm_2.y-15,click_count)
    placement(x6,Recm_3.x+15,Recm_3.y-15,click_count)
    
    placement(x7,Recl_1.x+15,Recl_1.y-15,click_count)
    placement(x8,Recl_2.x+15,Recl_2.y-15,click_count)
    placement(x9,Recl_3.x+15,Recl_3.y-15,click_count)
    Check_winner(x_positions,o_positions)
    if condition==True and click_count==9:
        print(x_positions)
        print(o_positions)
        condition=False
    pygame.display.update()
    Clock.tick(60)