import pygame
import character
import charCollision

pygame.init()

screen_length = 800
screen_heigth = 600

win = pygame.display.set_mode([screen_length, screen_heigth])

pygame.display.set_caption('DAHMER')

class Player():
	def __init__(self, left_edge, top_edge, x, y, width, height):
		self.left_edge = left_edge
		self.top_edge = top_edge
		self.width = width
		self.height = height
		self.x = x
		self.y = y
		self.vel = 2
		self.speed = 2

	def movement(self, r, l, u, d):
		controls = pygame.key.get_pressed()

		if controls[r]:
			self.left_edge -= self.vel
		else: 0
		
		if controls[l]: 
			self.left_edge += self.vel 
		else: 0

		if controls[u]: 
			self.top_edge -= self.speed 
		else: 0
		if controls[d]: 
			self.top_edge += self.speed 
	
	def render(self, char):
		man = win.blit(char, [self.left_edge, self.top_edge, self.x, self.y])
		# pygame.draw.rect(win, char, [self.left_edge, self.top_edge, self.width, self.height])

		if man.right >= screen_length or man.left <= 0:
			self.vel *= -1

		if man.bottom >= screen_heigth or man.top <= 0:
			self.speed *= -1

		# collide = man.colliderect(man)
		# if collide:
		# 	print('collide')
		#   	# self.vel *= -1
		#   	# self.speed *= -1

def bg(pic):
	win.blit(pic, (0,0))
		
		
player1 = Player(100, 0, 0, 0, 80, 80)
player2 = Player(500, 0, 0, 400, 64, 64)


run = True
while run:
	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False
	
	win.fill((0, 0, 0))
	bg(character.bg2)
	player1.render(character.char)
	player2.render(character.char1)
	player1.movement(pygame.K_a, pygame.K_d, pygame.K_w, pygame.K_s)
	player2.movement(pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN)
	# charCollision.collision(win)
	pygame.display.update()

pygame.quit()
