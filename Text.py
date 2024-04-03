import pygame
pygame.init()
#Classes
class textbox():
    def __init__(self,window,name:str,text:str,text_color:str,box_color:str,box_x:int,box_y:int,width:int,height:int,name_x:int,name_y:int,text_x:int,text_y:int):
        '''Make a textbox using Rect and Sysfont
window=pass varibale used to make pygame window
name=Name of the person who is speaking
text=text for the texbox
text_color=color the text variable will display as
box_color=color the texbox will be
box_x=x location the textbox will be placed
box_y=y location the textbox will be placed
width=How wide the texbox will be
height=How high the texbox will be
name_x=x location the name variable will be placed
name_y=y location the name variable will be placed
text_x=x location the text variable will be placed
text_y=y location the text variable will be placed'''
        #Variables
        self.window=window
        ##Name,Text, and Text_color
        self.name=name
        self.text=text
        self.text_color=text_color
        ##Textbox's x, y, and color
        self.box_x=box_x
        self.box_y=box_y
        self.box_color=box_color
        ##Textbox's width and height
        self.width=width
        self.height=height
        ##Name's x and y
        self.name_x=name_x
        self.name_y=name_y
        ##Text's x and y
        self.text_x=text_x
        self.text_y=text_y
        self.surface=pygame.Surface((self.width,self.height),pygame.SRCALPHA)
def draw(self,namefontsize:int,textfontsize:int):
        '''Draws textbox instance onto window
namefontsize=font size of the name
textfontsize=font size of the text'''
        #Speaker's name info
        Namefont=pygame.font.SysFont('timesnewroman',namefontsize)
        Namerender=Namefont.render(self.name,False,self.text_color)
        #Text info
        Textfont=pygame.font.SysFont('timesnewroman',textfontsize)
        Textrender=Textfont.render(self.text,False,self.text_color)
        #Backgroundbox info and display it
        Backgroundbox=pygame.Rect((0,0),(self.width,self.height))
        self.window.blit(self.surface,(self.box_x,self.box_y))
        Backgroundbox_display=pygame.draw.rect(self.surface,(self.box_color),Backgroundbox)
        #Display Name and Text
        Name_display=self.surface.blit(Namerender,(self.name_x,self.name_y))
        Text_display=self.surface.blit(Textrender,(self.text_x,self.text_y))
