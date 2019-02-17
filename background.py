import pygame
from setting import WIDTH, HEIGHT

class Background(pygame.sprite.Sprite):
	count = 0

	def __init__(self):
		super(Background, self).__init__()

		self.image = pygame.image.load('image/background.jpg')

		self.rect = self.image.get_rect()

		self.rect.bottom = HEIGHT

	#иллюзия движения игрока вперед, на самом деле двигается фон
	def update(self):
		self.rect.bottom += 5

		#сбрасывать позицию фона, если он закончился
		if self.rect.bottom >= self.rect.height and self.count < 6:
			self.rect.bottom = HEIGHT
			self.rect.right -= WIDTH
			self.count += 1
		elif self.rect.bottom >= self.rect.height and self.count == 6:
			self.rect.bottom = HEIGHT
			self.rect.right += WIDTH * 6
			self.count = 0