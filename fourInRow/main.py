import pygame
from sys import exit

blocks=[]
y=5
#5,5+20+5,5+20+5+20+5
#5,
for i in range (10):
    x=5
    for j in range (10):
        blocks.append(pygame.Rect(x,y,50,50))
        x+=55
    y+=55
red_=[]
blue_=[]
Truth=False
def rituals(text,text_color,Screen):
    pygame.draw.rect(Screen,'black',(20,195,515,110),border_radius=50)
    pygame.draw.rect(Screen,'#fbd7bf',(25,200,505,100),border_radius=50)
    FONT=pygame.font.SysFont('Comicsans',50,bold=True)
    Text=FONT.render(f'{text} wins',True,text_color)
    Screen.blit(Text,(160,210))
    pygame.display.update()
def logic(color,text,Screen,text_color):
    for i in range (97):
        if set([i+1,i+2,i+3,i+4]).issubset(color):
            while True:
                for events in pygame.event.get():
                    if events.type==pygame.QUIT:
                        pygame.quit()
                        exit()
                rituals(text,text_color,Screen)
        if set([i+10,i+20,i+30,i+40]).issubset(color):
            while True:
                for events in pygame.event.get():
                    if events.type==pygame.QUIT:
                        pygame.quit()
                        exit()
                rituals(text,text_color,Screen)
class player1:
    def __init__(self,Screen):
        self.data=[]
        self.blocks=blocks
        self.Screen=Screen
        self.blue=blue_
    def draw(self):
        for data in self.data:
            pygame.draw.rect(self.Screen,'#ee316b',data,border_radius=30)
            
        pygame.display.update()
    def append_data(self,data):
        self.blue.append((self.blocks.index(data))+1)
        self.data.append(data)
class player2:
    def __init__(self,Screen):
        self.data=[]
        self.Screen=Screen
        self.red=red_
        self.blocks=blocks
    def draw(self):
        for data in self.data:
            pygame.draw.rect(self.Screen,'#842d72',data,border_radius=30)
            
    def append_data(self,data):
        self.red.append((self.blocks.index(data))+1)
        self.data.append(data)
HEIGHT=555
WIDTH=555
class Main:
    def __init__(self):
        pygame.init()
        self.Screen=pygame.display.set_mode((HEIGHT,WIDTH))
        pygame.display.set_caption('4inRow')
        self.Rectangles=blocks
        self.mouse_count=1
        self.player1=player1(self.Screen)
        self.player2=player2(self.Screen)
        self.red=red_
        self.blue=blue_
        self.check=Truth
    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                mos=pygame.mouse.get_pos()
                for rects in self.Rectangles:
                    if rects.collidepoint(mos):
                        if event.type==pygame.MOUSEBUTTONDOWN :
                            if self.mouse_count == 1:
                                self.player1.append_data(rects)
                                
                            elif self.mouse_count == -1:
                                self.player2.append_data(rects)
                                
                            self.mouse_count*=-1
            self.Screen.fill('black')
            for rects in blocks:
                pygame.draw.rect(self.Screen,'#ffb037',rects,border_radius=30)
            self.player2.draw()
            self.player1.draw()
            logic(red_,'purple',self.Screen,'#842d72')
            logic(blue_,'pink',self.Screen,'#ee316b')
            pygame.display.update()

if __name__ == "__main__":
    main=Main()
    main.run()