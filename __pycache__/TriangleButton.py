import pygame
class TriangleButton:
    def __init__(self, x, y,foto):
        self.x = x
        self.y = y
        self.hovered = False
        self.border = 3
        self.width = 65
        self.height =65
        self.selected = False
        self.image= pygame.image.load("foto")

    def draw(self, screen, mouse_position):

        self.checkHover(mouse_position)
        if self.selected:
            self.border = 0
        else:
            self.border = 3
        pygame.draw.rect(screen,(255,0,0), pygame.Rect(self.x , self.y, self.width, self.height), self.border)
        pygame.draw.polygon(screen, (255, 0, 0), ((self.x+10,self.y+self.height-10),(self.x+10+((self.width-20)/2),self.y+10),(self.x-10+self.width,self.y+self.height-10)),3)
        
    def checkHover(self, mouse_position):
        if (mouse_position[0] > self.x  and mouse_position[1] > self.y  and mouse_position[0] < self.x +  self.width  and mouse_position[1] < self.y + self.height ):
            return True
        else:
            return False
    
    def setClick(self):
        if self.selected:
            self.selected = False
        else:
            self.selected = True    

    def setFalse(self):
        self.selected = False