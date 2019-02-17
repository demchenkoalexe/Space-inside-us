import pygame
import random

from setting import WIDTH, HEIGHT

class Meteorite(pygame.sprite.Sprite):
	#время появления метеорита
	cooldawn = 500
	current_cooldawn = 0
	speed = 10

	def __init__(self):
		super(Meteorite, self).__init__()
		
		#Рандомный выбор из 10 картинок метеоритов
		image_name = 'image/meteorite{}.png'.format(random.randint(1, 9))
		self.image = pygame.image.load(image_name)
		self.rect = self.image.get_rect()

		#рандомное расположение на игровом пространстве
		self.rect.midbottom = (random.randint(0, WIDTH), 0)
		
	def update(self):
		self.rect.move_ip((0, self.speed))

	#метод для появления метеоритов, сделаем статическим для обащения к cooldawn и current_cooldawn
	@staticmethod
	def process_meteors(clock, meteorites):
		if Meteorite.current_cooldawn <= 0:
			meteorites.add((Meteorite()))
			Meteorite.current_cooldawn = Meteorite.cooldawn
		else:
			Meteorite.current_cooldawn -= clock.get_time()

		#удаление меторитов за пределами экрана
		for m in list(meteorites):
			if (m.rect.right < 0 or m.rect.left > WIDTH or m.rect.top > HEIGHT):
				meteorites.remove(m)

