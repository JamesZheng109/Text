#Imports
import pygame,sys
from Scripts.Audio import play_sfx
pygame.init()
class button():
    def __init__ (self,window,x:int,y:int,width:int,height:int,box_color=None,text:str=None,text_color='black',image=None,audio=None,alpha=255,hover=None):
        '''Make a button using Rect
window=pass variable used to make pygame window
x=x location the button will be placed
y=y location the button will be placed
width=How wide the texbox will be
height=How high the texbox will be
box_color=color the button will be
text=Words to display on button
text_color=color text will be
image=display image on surface
hover=If mouse hover, draw rect
-format:(color,thickness)'''
        #Variables
        self.window=window
        self.audio=audio
        ##Button info
        self.x=x
        self.y=y
        self.box_color=box_color
        self.width=width
        self.height=height
        self.clicked=False
        self.text=text
        self.text_color=text_color
        self.textfont=pygame.font.SysFont('timesnewroman',50)
        self.textrender=self.textfont.render(self.text,False,self.text_color)
        if image!=None:
            self.image=pygame.transform.scale(image,(self.width,self.height))
        elif image==None:
            self.image=None
        #Surface
        self.surface=pygame.Surface((self.width,self.height),pygame.SRCALPHA)
        self.surface.set_alpha(alpha)
        self.Box=pygame.Rect(0,0,self.width,self.height)
        self.hover=hover
    def draw(self,act=None):
        '''Draws button instance onto window'''
        self.window.blit(self.surface,(self.x,self.y))
        ##Button info
        if self.box_color!=None:
            ##Button display
            pygame.draw.rect(self.surface,(self.box_color),self.Box)
        elif self.image!=None:
            self.surface.blit(self.image,(0,0))
        ##Display Text
        if self.text!=None:
            self.surface.blit(self.textrender,(int(self.width/2)-int(self.textrender.get_width()/2),int(self.height/2)-int(self.textrender.get_height()/2)))
        #Mouse detection
        if self.Box.collidepoint((pygame.mouse.get_pos()[0]-self.x,pygame.mouse.get_pos()[1]-self.y)):
            if self.hover!=None:
                pygame.draw.rect(self.window,self.hover[0],(self.x,self.y,self.Box.width,self.Box.height),self.hover[1])
            if pygame.mouse.get_pressed()[0]==1 and self.clicked==False:
                self.clicked=True
                if self.audio!=None:
                    play_sfx(self.audio)
                if act!=None:
                    pygame.event.clear()
                    act()
            else:
                self.clicked=False
    def delete_button(self,Display_W,Display_H):
        '''Move and shrink button and moves it elsewhere'''
        self.x=Display_W+1
        self.y=Display_H+1
        self.width=0
        self.height=0
