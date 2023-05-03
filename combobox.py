import pygame

import boton


# Clase boton
class combobox():
    def __init__(self, x, y ):
        self.fuente = pygame.font.SysFont("Helvetica", 30)
        self.lista_render=[]
        self.x = x
        self.y = y
        self.height = 0
        self.width=0
        self.x_inicio=0
        self.bandera=False
        lista_acciones=["Ingresar Al Inicio", "Ingresar Al Final" , "Insertar Nodo En posicion", "Eliminar Ultimo Nodo", "Eliminar Primer Nodo", "Invertir Lista", "Eliminar todos los elementos", "Agregar Elemento en posición", "Comprobar lista vacia"]
        for accion in  lista_acciones:
            self.lista_render.append(self.fuente.render(accion,True,(0,0,0)))
        for render in self.lista_render:
            if  render.get_width() > self.width:
                self.width = render.get_width()
            self.height += render.get_height()+10
        self.width+=10

    def draw(self, screen):
        pygame.draw.rect(screen,(255, 192, 203),pygame.Rect(self.x,self.y,self.width,self.height) )
        self.y_render=self.y
        for render in self.lista_render:
            screen.blit(render,(self.x,self.y_render))
            pygame.draw.line(screen,(0,0,0),(self.x,self.y_render),(self.x+self.width,self.y_render))
            self.y_render+=render.get_height()+10
    def cliks(self, mousepos):
        self.bandera= False
        contador=0

        pos_actual=self.y
        for render in self.lista_render:
            if  mousepos[1] > pos_actual and mousepos[1] < pos_actual + 45 and mousepos[0] > self.x and mousepos[0] < self.x + self.width:
                return contador
            contador+=1
            pos_actual+=45

    def mouseinside(self,screen):
        self.rectangulo=pygame.Rect(self.x, self.y, self.width, self.height)
        pos = pygame.mouse.get_pos()
        return self.rectangulo.collidepoint(pos)










