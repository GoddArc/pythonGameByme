from test import *
import testmain
row_width=square_Size*(len(testmain.Word))+gap*(len(testmain.Word)-1)
class Rowr(pygame.sprite.Sprite):
    def __init__(self,y):
        super().__init__()
        pygame.init()
        self.image=pygame.Surface((row_width,square_Size))
        self.rect=self.image.get_rect()
        if len(testmain.Word)%2==0:
            self.rect.x=Width//2-(gap/2+(int(len(testmain.Word)/2)*square_Size)+((len(testmain.Word)/2)-1)*gap)
        else:
            self.rect.x=Width//2-((square_Size//2)+(int(len(testmain.Word)/2)*(square_Size+gap)))
        self.rect.y=y
        self.sq_group=[]
        self.pos_letter=[]
        self.color=['grey']*len(testmain.Word)
        self.image.fill((43, 45, 48))
        self.FONT=pygame.font.SysFont('font.fon',square_Size)
    def update(self,word,Color):
        self.word=word.upper()
        self.squares(Color)
        self.text()
    def squares(self,Color):
        self.pos=self.rect.x
        for i in range (len(testmain.Word)):
            Rect=pygame.Rect(self.pos,self.rect.y,square_Size,square_Size)
            self.sq_group.append(Rect)
            if Color[i]=='#787C7E':
                pygame.draw.rect(Screen,Color[i],Rect,border_radius=5,width=2)
            else:
                pygame.draw.rect(Screen,Color[i],Rect,border_radius=5)
            self.pos+=square_Size+gap
    def text(self):
            for index,i in enumerate(self.word):
                ord=self.FONT.render(i,True,'#FDFDFD')
                rect=ord.get_rect()
                rect.center=self.sq_group[index].center
                Screen.blit(ord,rect)
            