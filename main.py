import sys
import pygame
import single_linked_list
import time
pygame.init()
import combobox
import boton

sll = single_linked_list.SingleLinkedList()
from menu import Menu


class Anime:

    def __init__(self):
        self.screen = pygame.display.set_mode((1200, 700))
        pygame.display.set_caption("Anime SLL")
        self.image_selected = None

        # Colores
        self.BLACK = (0, 0, 0)
        self.WHITE = (255, 255, 255)
        self.PINK = (255, 192, 203)
        self.LIGHT_BLUE = (161, 163, 212)
        # Imagenes
        imagen_zero = pygame.image.load("zerotwoicon.jpg").convert_alpha()
        imagen_yuno = pygame.image.load("yuno.jpg").convert_alpha()
        imagen_owari_serapth = pygame.image.load("owari.png").convert_alpha()
        imagen_boton = pygame.image.load("boton.png").convert_alpha()
        imagen_boton_numeros = pygame.image.load("botonnumeros.png").convert_alpha()
        imagen_boton_combo = pygame.image.load("boton.png").convert_alpha()

        # Textos
        self.fuente = pygame.font.SysFont("añadir imagen", 30)
        self.texto = self.fuente.render("Añadir Imagenes A La Lista", True, self.BLACK)
        self.texto_combo = self.fuente.render("Seleccionar Método", True, self.BLACK)
        self.texto_index = self.fuente.render("Posición ", True, self.BLACK)
        self.numeros = self.fuente.render("Seleccionar en teclado ", True, self.BLACK)
        self.lista = self.fuente.render("Lista Actual", True, self.BLACK)

        # Boton menus
        self.main_menu = Menu(self.screen,
                              {"SLL": None, "DLL": None, "Pilas y colas": None, "Árboles": None, "Grafos": None},
                              self.PINK, 75, "Arial", 22, self.BLACK)
        # Botones Imagenes
        self.boton_zerotwo = boton.Button(400, 200, imagen_zero, 1)
        self.boton_yuno_gasai = boton.Button(700, 200, imagen_yuno, 1)
        self.boton_owari = boton.Button(550, 200, imagen_owari_serapth, 1)
        self.boton_combo = boton.Button(350, 329, imagen_boton, 0.3)
        self.boton_numero = boton.Button(750, 329, imagen_boton_numeros, 0.3)
        self.boton_combo_box = boton.Button(360, 320, imagen_boton_combo, 0.3)
        self.combo_box = combobox.combobox(0, 150)

        #Lista de botones
        self.lista_botones = [self.boton_zerotwo, self.boton_owari, self.boton_yuno_gasai]

    def run(self):
        user_number = 0

        while True:
            elpepe=0

            pos = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.unicode.isnumeric():
                        user_number = int(event.unicode)

                        self.numeros = self.fuente.render(str(user_number), False, self.BLACK)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.combo_box.mouseinside(self.screen):
                        imagen_lista=self.boton_zerotwo.image
                        for elemento in self.lista_botones:
                            if elemento.clicked:
                                imagen_lista=elemento.image
                        if self.combo_box.cliks(pos) == 0:
                            sll.create_node_sll_unshift(imagen_lista)
                        if self.combo_box.cliks(pos) == 1:

                            sll.create_node_sll_ends(imagen_lista)
                        if self.combo_box.cliks(pos) == 2:
                            print(user_number)
                            sll.insert_value_at_index(imagen_lista,user_number)
                        if self.combo_box.cliks(pos) == 3:
                            sll.delete_node_sll_pop()
                        if self.combo_box.cliks(pos) == 4:
                            sll.create_node_sll_unshift()
                        if self.combo_box.cliks(pos) == 5:
                            sll.reverse_sll()
                        if self.combo_box.cliks(pos) == 6:
                            sll.remove_all_nodes()
                        if self.combo_box.cliks(pos) == 7:
                            sll.update_node_value(user_number, imagen_lista)
                        if self.combo_box.cliks(pos) == 8:
                            a = self.fuente.render(str(sll.is_sll_empty()), False, (0,0,0))
                            self.screen.blit(a, (500, 500))
                            pygame.display.update()
                            time.sleep(1)





                    if self.boton_zerotwo.click():
                        self.boton_owari.clicked=False
                        self.boton_yuno_gasai.clicked = False
                    if self.boton_owari.click():
                        self.boton_zerotwo.clicked = False
                        self.boton_yuno_gasai.clicked = False
                    if self.boton_yuno_gasai.click():
                        self.boton_owari.clicked = False
                        self.boton_zerotwo.clicked = False

                    if self.boton_combo.mouseinside():
                        self.combo_box.bandera = True
                        print("ELPEPE")


            self.boton_combo.draw(self.screen)
            self.screen.fill(self.WHITE)
            self.combo_box.draw(self.screen)
            if self.main_menu.getSelectedOption() == 0:
                pygame.draw.rect(self.screen, self.WHITE,
                                 (0, 40, self.screen.get_width(), self.screen.get_height() - 40))
                pygame.draw.rect(self.screen, self.WHITE,
                                 (0, 40, self.screen.get_width(), self.screen.get_height() - 40))

                # Dibujar Textos
                self.boton_numero.draw(self.screen)
                self.screen.blit(self.texto, (480, 120))
                self.screen.blit(self.texto_combo, (140, 330))
                self.screen.blit(self.texto_index, (640, 340))
                self.screen.blit(self.numeros, (800, 340))
                self.screen.blit(self.lista, (530, 400))
                # Dibujar Botones
                self.boton_zerotwo.draw(self.screen)
                self.boton_yuno_gasai.draw(self.screen)
                self.boton_owari.draw(self.screen)
                self.boton_combo_box.draw(self.screen)
                for x in sll.show_list():
                    self.draw_singlell(self.screen)
                if self.combo_box.bandera:
                    self.combo_box.draw(self.screen)


            elif (self.main_menu.getSelectedOption() == 1):
                pygame.draw.rect(self.screen, self.WHITE,
                                 (0, 40, self.screen.get_width(), self.screen.get_height() - 40))
            self.main_menu.draw()

            pygame.display.flip()

    def draw_singlell(self, screen):
        x_pos = 510 - (sll.get_list_lenght() * 100 + 15 * (sll.get_list_lenght() - 1)) // 2
        y_pos=450
        for nodo in sll.show_list():
            self.screen.blit(nodo,(x_pos,y_pos))




            x_pos += 140

if __name__ == "__main__":
    a = Anime()
    a.run()
