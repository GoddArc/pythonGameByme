import pygame,sys
from settings import *
from row import Row
from endScreen import EndScreen
from endScreen import Logo
pygame.init()
stroke=pygame.mixer.Sound('audio/stroke.mp3')
win=pygame.mixer.Sound('audio/win.mp3')
row_group1.add(Row(upper_gap))
row_group2.add(Row(upper_gap+square_Size+gap))
row_group3.add(Row(upper_gap+2*(square_Size+gap)))
row_group4.add(Row(upper_gap+3*(square_Size+gap)))
row_group5.add(Row(upper_gap+4*(square_Size+gap)))
row_group6.add(Row(upper_gap+5*(square_Size+gap)))
chekc=True
word_guessed=''
word_guessed2=''
word_guessed3=''
word_guessed4=''
word_guessed5=''
word_guessed6=''
control=1
default1,default2,default3,default4,default5,default6=['#787C7E']*len(Word),['#787C7E']*len(Word),['#787C7E']*len(Word),['#787C7E']*len(Word),['#787C7E']*len(Word),['#787C7E']*len(Word)
def Color(takes):
    word=takes.upper()
    color=['#787C7E']*len(Word)
    for index,i in enumerate(word):
            if i==Word[index]:
                color.pop(index)
                color.insert(index,'#6BA964')
            elif set([i]).issubset(word_group):
                color.pop(index)
                color.insert(index,'#CAB457')
                
    return color

def check_color(grp):
    token=0
    for elements in grp:
        if elements=='#6BA964':
            token+=1
    if token==len(Word):
        return True
    else:
        return False
Gameplay=True
end=EndScreen()
log=Logo()
while True:
    for events in pygame.event.get():
        if events.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
        if Gameplay==True:
            if events.type==pygame.KEYDOWN and chekc==True:
                stroke.play()
                key=pygame.key.get_pressed()
                if key[pygame.K_RETURN]:
                    if control>=1:
                        default1=Color(word_guessed)
                    if control>=2:
                        default2=Color(word_guessed2)
                    if control>=3:
                        default3=Color(word_guessed3)
                    if control>=4:
                        default4=Color(word_guessed4)
                    if control>=5:
                        default5=Color(word_guessed5)
                    if control>=6:
                        default6=Color(word_guessed6)
                    print(control)
                    control+=1
                elif key[pygame.K_BACKSPACE]:
                    if control==1:
                        word_guessed=word_guessed[0:-1]
                    elif control==2:
                        word_guessed2=word_guessed2[0:-1]
                    elif control==3:
                        word_guessed3=word_guessed3[0:-1]
                    elif control==4:
                        word_guessed4=word_guessed4[0:-1]
                    elif control==5:
                        word_guessed5=word_guessed5[0:-1]
                    elif control==6:
                        word_guessed6=word_guessed6[0:-1]
                else:
                    if control==1:
                        if len(word_guessed)<len(Word):
                            word_guessed+=events.unicode
                    elif control==2:
                        if len(word_guessed2)<len(Word):
                            word_guessed2+=events.unicode
                    elif control==3:
                        if len(word_guessed3)<len(Word):
                            word_guessed3+=events.unicode
                    elif control==4:
                        if len(word_guessed4)<len(Word):
                            word_guessed4+=events.unicode
                    elif control==5:
                        if len(word_guessed5)<len(Word):
                            word_guessed5+=events.unicode
                    elif control==6:
                        if len(word_guessed6)<len(Word):
                            word_guessed6+=events.unicode
            if events.type==pygame.KEYUP:
                chekc=True
                
    Screen.fill((43, 45, 48))
    log.draw()
    row_group1.draw(Screen)
    row_group2.draw(Screen)
    row_group3.draw(Screen)
    row_group4.draw(Screen)
    row_group5.draw(Screen)
    row_group6.draw(Screen)
    row_group1.update(word_guessed,default1)
    row_group2.update(word_guessed2,default2)
    row_group3.update(word_guessed3,default3)
    row_group4.update(word_guessed4,default4)
    row_group5.update(word_guessed5,default5)
    row_group6.update(word_guessed6,default6)
    if check_color(default1)==True or check_color(default2)==True or check_color(default3)==True or check_color(default4)==True or check_color(default5)==True or check_color(default6)==True:
        end.draw('You','WON')
        if Gameplay==True:
            win.play()
        Gameplay=False
    elif control>6:
        end.draw('The word is',Word)
        Gameplay=False
    pygame.display.update()