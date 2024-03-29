import pygame
import os

pygame.init()

bg2 = pygame.image.load('pic/tiles2.0.png')
speed = pygame.image.load('pic/speed.png')
debuff = pygame.image.load('pic/debuff.png')
bg2 = pygame.transform.scale(bg2, (800, 600))
char = pygame.image.load(os.path.join('pic/move-char', 'front2.0.png'))
oponent = pygame.image.load(os.path.join('pic/move-char', 'oponent-front.png'))
orange_button = pygame.image.load(os.path.join('pic/', 'play-game.png'))
player1_wins = pygame.image.load(os.path.join('pic/', 'player1_wins.png'))
player2_wins = pygame.image.load(os.path.join('pic/', 'player2_wins.png'))

left = [
		pygame.image.load(os.path.join('pic/move-char', 'side-right2.0.png')), 
		pygame.image.load(os.path.join('pic/move-char', 'side-right-walk2.0.png')), 
		pygame.image.load(os.path.join('pic/move-char', 'side-right-walk22.0.png')),
		pygame.image.load(os.path.join('pic/move-char', 'side-right2.0.png')), 
		pygame.image.load(os.path.join('pic/move-char', 'side-right-walk2.0.png')), 
		pygame.image.load(os.path.join('pic/move-char', 'side-right-walk22.0.png')),
		pygame.image.load(os.path.join('pic/move-char', 'side-right2.0.png')), 
		pygame.image.load(os.path.join('pic/move-char', 'side-right-walk2.0.png')),
		pygame.image.load(os.path.join('pic/move-char', 'side-right-walk22.0.png'))
]

right = [
		pygame.image.load(os.path.join('pic/move-char', 'side-left2.0.png')), 
		pygame.image.load(os.path.join('pic/move-char', 'side-left-walk2.0.png')), 
		pygame.image.load(os.path.join('pic/move-char', 'side-left-walk22.0.png')),
		pygame.image.load(os.path.join('pic/move-char', 'side-left2.0.png')), 
		pygame.image.load(os.path.join('pic/move-char', 'side-left-walk2.0.png')), 
		pygame.image.load(os.path.join('pic/move-char', 'side-left-walk22.0.png')),
		pygame.image.load(os.path.join('pic/move-char', 'side-left2.0.png')), 
		pygame.image.load(os.path.join('pic/move-char', 'side-left-walk2.0.png')),
		pygame.image.load(os.path.join('pic/move-char', 'side-left-walk22.0.png'))
]

front = [
		pygame.image.load(os.path.join('pic/move-char', 'front-right2.0.png')), 
		pygame.image.load(os.path.join('pic/move-char', 'front-left2.0.png')),
		pygame.image.load(os.path.join('pic/move-char', 'front-right2.0.png')), 
		pygame.image.load(os.path.join('pic/move-char', 'front-left2.0.png')),
		pygame.image.load(os.path.join('pic/move-char', 'front-right2.0.png')), 
		pygame.image.load(os.path.join('pic/move-char', 'front-left2.0.png')),
		pygame.image.load(os.path.join('pic/move-char', 'front-right2.0.png')), 
		pygame.image.load(os.path.join('pic/move-char', 'front-left2.0.png')),
		pygame.image.load(os.path.join('pic/move-char', 'front-right2.0.png'))		
]

back = [
	   pygame.image.load(os.path.join('pic/move-char', 'back-right2.0.png')),
	   pygame.image.load(os.path.join('pic/move-char', 'back-left2.0.png')),
	   pygame.image.load(os.path.join('pic/move-char', 'back-right2.0.png')),
	   pygame.image.load(os.path.join('pic/move-char', 'back-left2.0.png')), 
	   pygame.image.load(os.path.join('pic/move-char', 'back-right2.0.png')),
	   pygame.image.load(os.path.join('pic/move-char', 'back-left2.0.png')), 
	   pygame.image.load(os.path.join('pic/move-char', 'back-right2.0.png')),
	   pygame.image.load(os.path.join('pic/move-char', 'back-left2.0.png')), 
	   pygame.image.load(os.path.join('pic/move-char', 'back-right2.0.png'))
]

oponent_left = [
	   pygame.image.load(os.path.join('pic/move-char', 'oponent-side-left2.png')),
	   pygame.image.load(os.path.join('pic/move-char', 'oponent-side-left-walk.png')),
	   pygame.image.load(os.path.join('pic/move-char', 'oponent-side-left-walk2.png')),
	   pygame.image.load(os.path.join('pic/move-char', 'oponent-side-left2.png')),
	   pygame.image.load(os.path.join('pic/move-char', 'oponent-side-left-walk.png')),
	   pygame.image.load(os.path.join('pic/move-char', 'oponent-side-left-walk2.png')),
	   pygame.image.load(os.path.join('pic/move-char', 'oponent-side-left2.png')),
	   pygame.image.load(os.path.join('pic/move-char', 'oponent-side-left-walk.png')),
	   pygame.image.load(os.path.join('pic/move-char', 'oponent-side-left-walk2.png'))
]

oponent_right = [
	   pygame.image.load(os.path.join('pic/move-char', 'oponent-side-right.png')),
	   pygame.image.load(os.path.join('pic/move-char', 'oponent-side-right-walk.png')),
	   pygame.image.load(os.path.join('pic/move-char', 'oponent-side-right-walk2.png')),
	   pygame.image.load(os.path.join('pic/move-char', 'oponent-side-right.png')),
	   pygame.image.load(os.path.join('pic/move-char', 'oponent-side-right-walk.png')),
	   pygame.image.load(os.path.join('pic/move-char', 'oponent-side-right-walk2.png')),
	   pygame.image.load(os.path.join('pic/move-char', 'oponent-side-right.png')),
	   pygame.image.load(os.path.join('pic/move-char', 'oponent-side-right-walk.png')),
	   pygame.image.load(os.path.join('pic/move-char', 'oponent-side-right-walk2.png'))
]

oponent_front = [
	   pygame.image.load(os.path.join('pic/move-char', 'oponent-front-left.png')),
	   pygame.image.load(os.path.join('pic/move-char', 'oponent-front-right.png')),
	   pygame.image.load(os.path.join('pic/move-char', 'oponent-front-left.png')),
	   pygame.image.load(os.path.join('pic/move-char', 'oponent-front-right.png')),
	   pygame.image.load(os.path.join('pic/move-char', 'oponent-front-left.png')),
	   pygame.image.load(os.path.join('pic/move-char', 'oponent-front-right.png')),
	   pygame.image.load(os.path.join('pic/move-char', 'oponent-front-left.png')),
	   pygame.image.load(os.path.join('pic/move-char', 'oponent-front-right.png')),
	   pygame.image.load(os.path.join('pic/move-char', 'oponent-front-left.png'))  
]

oponent_back = [
	   pygame.image.load(os.path.join('pic/move-char', 'oponent-back-left.png')),
	   pygame.image.load(os.path.join('pic/move-char', 'oponent-back-right.png')),
	   pygame.image.load(os.path.join('pic/move-char', 'oponent-back-left.png')),
	   pygame.image.load(os.path.join('pic/move-char', 'oponent-back-right.png')),
	   pygame.image.load(os.path.join('pic/move-char', 'oponent-back-left.png')),
	   pygame.image.load(os.path.join('pic/move-char', 'oponent-back-right.png')),
	   pygame.image.load(os.path.join('pic/move-char', 'oponent-back-left.png')),
	   pygame.image.load(os.path.join('pic/move-char', 'oponent-back-right.png')),
	   pygame.image.load(os.path.join('pic/move-char', 'oponent-back-left.png'))
]

# rect = char.get_rect()
# rect1 = char1.get_rect()
# # rect2 = char2.get_rect()