import pygame

from plasmoid import Plasmoid
from setting import WIDTH, HEIGHT

class Player(pygame.sprite.Sprite):
	#движение игрока
	speed = 10

	#паузы между стрельбой
	shooting_cooldown = 150

	#наследоание от pygame sprite позволяет взаимодействовать объекту с другими объектами и с полем
	def __init__(self, clock, plasmoids):
		super(Player, self).__init__()

		self.clock = clock
		self.plasmoids = plasmoids

		self.image = pygame.image.load('image/player1.png') 
		#размеры игрока
		self.rect = self.image.get_rect()

		#зададим координаты через его позицию
		#отцентрируем относительно экрана
		self.rect.centerx = WIDTH / 2
		self.rect.bottom = HEIGHT - 10

		#перемещение по экрану
		self.current_speed_x = 0
		self.current_speed_y = 0

		#текущий выстрел
		self.current_shooting_cooldown = 0 
 
	def update(self):
		#обработка нажатых клавиш
		keys = pygame.key.get_pressed()

		if keys[pygame.K_a]:
			if self.rect.centerx > 0:
				self.current_speed_x = -self.speed
				self.current_speed_y = 0
			else:
				self.current_speed_x = 0
		elif keys[pygame.K_d]:
			if self.rect.centerx < WIDTH:
				self.current_speed_x = self.speed
				self.current_speed_y = 0
			else:
				self.current_speed_x = 0
		elif keys[pygame.K_w]:
			if self.rect.bottom > 100:
				self.current_speed_y = -self.speed
				self.current_speed_x = 0
			else:
				self.current_speed_y = 0
		elif keys[pygame.K_s]:
			if self.rect.bottom < HEIGHT - 10:
				self.current_speed_y = self.speed
				self.current_speed_x = 0
			else:
				self.current_speed_y = 0
		else:
			self.current_speed_x = 0
			self.current_speed_y = 0

		#двигать игрока 
		self.rect.move_ip((self.current_speed_x, self.current_speed_y))

		#стрельба
		self.shooting()

	def  shooting(self):
		keys = pygame.key.get_pressed()

		if keys[pygame.K_SPACE] and self.current_shooting_cooldown <= 0:
			self.plasmoids.add(Plasmoid(self.rect.midtop))
			#ограничим количество выстрел за определенный промеуток времени
			self.current_shooting_cooldown = self.shooting_cooldown
		else:
			self.current_shooting_cooldown -= self.clock.get_time() 

		#удалить после того, как снаряд улетает за экран
		for plasmoid in list(self.plasmoids):
			if plasmoid.rect.bottom < 0:
				self.plasmoids.remove(plasmoid)

