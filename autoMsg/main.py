import AppOpener
import pyautogui
import keyboard
try:
    import pywhatkit
except:
    print('internet connection error')
import time
import pygame
from sys import exit

pygame.init()
Clock = pygame.time.Clock()
Screen = pygame.display.set_mode((400,180))
pygame.display.set_caption("AutoMsg")
FONT=pygame.font.SysFont('Comicsans', 20)
Send_button=pygame.Rect(100,Screen.get_height()-50,80,30)
Send_text=FONT.render('Send',True,'black')
Next_button=pygame.Rect(10,Screen.get_height()-50,80,30)
Next_text=FONT.render('Next',True,'black')

Msg_times='Times: '
Next_counter=0
PhoneNumber='+91'
pseudo_message='Message: '
Message='Message: '

Send=False
Message_send=False
Times_send=False
Phone_send=True
def print(Text,x,y):
    temp=FONT.render(Text,True,'green')
    Screen.blit(temp,(x,y))
def logic(PhoneNumber,Message,Times):
    pywhatkit.sendwhatmsg_instantly(PhoneNumber,Message[8:])
    time.sleep(10)
    pyautogui.click(x=692, y=734)
    time.sleep(2)
    keyboard.press_and_release('enter')
    time.sleep(3)
    for i in range(int(Times[7:])):
        
        keyboard.write(Message[8:])
        keyboard.press_and_release('enter')
NEXT_CLICKS=0
        #9470838095-sahil bhaiya +91 6200 035 059-akash
while True:
    for events in pygame.event.get():
        if events.type==pygame.QUIT:
            pygame.quit()
            exit()
        keys=pygame.key.get_pressed()
        mouse_x,mouse_y=pygame.mouse.get_pos()
        if events.type==pygame.KEYDOWN:
            if Phone_send==True:
                if keys[pygame.K_BACKSPACE]:
                    PhoneNumber=PhoneNumber[:-1]
                else:
                    PhoneNumber+=events.unicode
                
            elif Message_send==True:
                if keys[pygame.K_BACKSPACE]:
                    Message=Message[:-1]
                else:
                    Message+=events.unicode
            elif Times_send==True:
                if keys[pygame.K_BACKSPACE]:
                    Msg_times=Msg_times[:-1]
                else:
                    Msg_times+=events.unicode
        if Next_button.x<=mouse_x<=Next_button.x+80 and Next_button.y<=mouse_y<=Next_button.y+20 and events.type==pygame.MOUSEBUTTONDOWN:
            NEXT_CLICKS+=1
            
        if Send_button.x<=mouse_x<=Send_button.x+80 and Send_button.y<=mouse_y<=Send_button.y+20 and events.type==pygame.MOUSEBUTTONDOWN:
            Send=True
    Screen.fill('black')
    print(PhoneNumber,10,20)
    print(pseudo_message,10,50)
    print('Times:',10,85)
    if Message_send==True:
        print(Message,10,50)
    if Times_send==True:
        print(Msg_times,10,85)
    #Rectangles
    pygame.draw.rect(Screen,'green',Send_button,border_radius=20)
    Screen.blit(Send_text,(Send_button.x+15,Send_button.y))
    pygame.draw.rect(Screen,'green',Next_button,border_radius=20)
    Screen.blit(Next_text,(Next_button.x+15,Next_button.y))
    #end
    if NEXT_CLICKS==1:
        Message_send=True
        Phone_send=False
    if NEXT_CLICKS>=2:
        Message_send=False
        print(Message,10,50)
        Times_send=True
    if Send==True:
        logic(PhoneNumber,Message,Msg_times)
        pygame.quit()
        exit()
    pygame.display.update()
    Clock.tick(60)

