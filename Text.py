import pygame
pygame.init()
#Classes
class textbox():
    def __init__(self,window,name,text,text_color,box_color,box_x,box_y,width,height,name_x,name_y,text_x,text_y):
        #Variables
        self.window=window
        ##Name,Text, and Text_color
        self.name,self.text,self.text_color=name,text,text_color
        ##Textbox's x, y, and color
        self.box_x,self.box_y,self.box_color=box_x,box_y,box_color
        ##Textbox's width and height
        self.width,self.height=width,height
        ##Name's x and y
        self.name_x,self.name_y=name_x,name_y
        ##Text's x and y
        self.text_x,self.text_y=text_x,text_y
    def draw(self):
        #Speaker's name info
        Namefont=pygame.font.SysFont('timesnewroman',25);Namerender=Namefont.render(self.name,False,self.text_color)
        #Text info
        Textfont=pygame.font.SysFont('timesnewroman',25);Textrender=Textfont.render(self.text,False,self.text_color)
        #Backgroundbox info and display it
        Backgroundbox=pygame.Rect((self.box_x,self.box_y),(self.width,self.height));Backgroundbox_display=pygame.draw.rect(self.window,(self.box_color),Backgroundbox)
        #Display Name and Text
        Name_display,Text_display=self.window.blit(Namerender,(self.name_x,self.name_y)),self.window.blit(Textrender,(self.text_x,self.text_y))
    def update_textbox(self,message='',new_name=''):
        #Changing text and name variables
        self.text,self.name=message,new_name
    def delete_textbox(self):
        #Empties text
        self.update_textbox()
        self.x,self.y=Display_W+1,Display_H+1
        self.width,self.height=0,0
class button():
    def __init__ (self,window,box_color,x,y,width,height):
        #Variables
        self.window=window
        ##Button info
        self.x,self.y,self.box_color,self.width,self.height=x,y,box_color,width,height
        self.clicked=False
    def draw(self):
        #Variables
        act=False
        ##Button info
        Box=pygame.Rect((self.x,self.y),(self.width,self.height))
        ##Button display
        Box_display=pygame.draw.rect(self.window,(self.box_color),Box)
        #Mouse detection
        if Box_display.collidepoint(pygame.mouse.get_pos()):
            if pygame.mouse.get_pressed()[0]==1 and self.clicked==False:self.clicked=True;act=True
        if pygame.mouse.get_pressed()[0]==0:self.clicked=False
        return act
    def delete_button(self):
        #Move and shrink button and moves it elsewhere
        self.x,self.y,self.width,self.height=Display_W+1,Display_H+1,0,0
class option():
    def __init__(self,window,optiontext,text_color,x,y):
        #Variables
        self.window=window
        ##Option Info
        self.optiontext,self.text_color,self.x,self.y=optiontext,text_color,x,y
        ##Option button
        self.option_button=button(self.window,White,150,40,200,50)
    def draw_text(self):
        #Text option info
        Optionfont=pygame.font.SysFont('timesnewroman',25);Optionrender=Optionfont.render(self.optiontext,True,self.text_color)
        #Text option display
        Option_display=self.window.blit(Optionrender,(self.x,self.y))
    def update_option(self,new_option=''):
        #Change option text
        self.optiontext=new_option
    def delete_option(self):
        #Empties text and use button.delete_button()
        self.update_option();self.option_button.delete_button()
