import sys 
import pygame
import pyganim

from game_object import Player
from background import Background
from meteorite import Meteorite
from plasmoid import Plasmoid
from setting import SIZE, WHITE

pygame.init()

pygame.display.set_caption("Space inside us")
screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()

#создадим анимацию взрыва
explosion_animation = pyganim.PygAnimation([('image/explosion/{}.png'.format(i), 100) for i in range(3)], loop=False)

#фоновый звук
music = pygame.mixer.Sound('tracks/1.wav')
music.play(-1) #-1 музыка играет всё время
 
#отдельная группа для плазмоидов
plasmoids = pygame.sprite.Group()
#отдельная группа метеоритов
meteorites = pygame.sprite.Group()
#группа всех объектов для групповых операций над ними в общем цикле
all_objects = pygame.sprite.Group()

explosions = [] #массив взрывов

#создание игрока
player = Player(clock, plasmoids)

#создадим игровые объекты и добавляем их в группу
all_objects.add(Background())
all_objects.add(player)


while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit(0)

	Meteorite.process_meteors(clock, meteorites)

	#перед тем, как отобразить объекты, проведем все изменения над ними
	all_objects.update()
	plasmoids.update()
	meteorites.update()

	#уничтожение плазмоида и метеорита после сталкновения
	meteorites_and_plasmoids_collide = pygame.sprite.groupcollide(meteorites, plasmoids, True, True)
	for collided in meteorites_and_plasmoids_collide:
		explosion = explosion_animation.getCopy()
		explosion.play()
		explosions.append((explosion, (collided.rect.center)))

	#столкновение игрока и метеорита
	players_and_meteors_collide = pygame.sprite.spritecollide(player, meteorites, False)
	if players_and_meteors_collide:
		all_objects.remove(player)

	#отображение игрока
	all_objects.draw(screen)
	plasmoids.draw(screen)
	meteorites.draw(screen)

	#рисование анимации взрыва
	for explosion, position in explosions.copy():
		#проверим, не закончилась ли ещё анимация
		if explosion.isFinished():
			explosions.remove((explosion, position))
		else:
			x, y = position
			explosion.blit(screen, (x - 300, y - 300))

	pygame.display.flip()

	clock.tick(30)

