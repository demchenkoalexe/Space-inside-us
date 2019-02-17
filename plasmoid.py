import pygame
from setting import HEIGHT, WIDTH

class Plasmoid(pygame.sprite.Sprite):
	speed = -15

	def __init__(self, position):
		super(Plasmoid, self).__init__()

		self.image = pygame.image.load('image/plasmoid1.png')
		self.rect = self.image.get_rect()

		self.rect.midbottom = position
		self.rect.y += 40

	def update(self):
		self.rect.move_ip((0, self.speed))