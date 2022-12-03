import pygame
import character

pygame.init()

def collision(screen):
	# if character.rect.colliderect(character.rect1):
	# 		# pygame.draw.rect(screen, (255, 0, 0), character.rect, 3)
	# 		print('player 1 win')
	collide = character.rect.colliderect(character.rect1)
	if collide:
		print('collide')


		# if collide:
		#   self.vel *= -1
		#   self.speed *= -1
