import pygame
#Clase boton
class Button():
	def __init__(self, x, y, image, scale):
		width = image.get_width()
		height = image.get_height()
		self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
		self.rect = self.image.get_rect()
		self.rect.topleft = (x, y)
		self.clicked = False

	def draw(self, surface):



		#Dibujar el boton en pantalla
		surface.blit(self.image, (self.rect.x, self.rect.y),)
		if self.clicked:
			pygame.draw.rect(surface, (0, 0, 0),(self.rect.x, self.rect.y, self.image.get_width(), self.image.get_height()), 1)



	def click(self):
		action=False
		# Obtener posicion del mouse
		pos = pygame.mouse.get_pos()
		# Revisar mouseover y clicked condiciones
		if self.rect.collidepoint(pos):

			if self.clicked:
				self.clicked=False
				action=False
				return False
			else:
				self.clicked = True
				return True
				action = True



		return action

	def mouseinside(self):
		pos = pygame.mouse.get_pos()
		return self.rect.collidepoint(pos)