import pygame
pygame.init()

bg2 = pygame.image.load('pic/bg-dahmer.png')
bg2 = pygame.transform.scale(bg2, (800, 600))
char = pygame.image.load('pic/move-char/front.png')
char1 = pygame.image.load('pic/move-char/front.png')
char2 = [pygame.image.load('pic/move-char/front.png'),
		 pygame.image.load('pic/move-char/side-right.png'), 
		 pygame.image.load('pic/move-char/side-right-walk.png'), 
		 pygame.image.load('pic/move-char/side-right-walk2.png'),
		 pygame.image.load('pic/move-char/side-right.png'), 
		 pygame.image.load('pic/move-char/side-right-walk.png'), 
		 pygame.image.load('pic/move-char/side-right-walk2.png'),
		 pygame.image.load('pic/move-char/side-right.png'), 
		 pygame.image.load('pic/move-char/side-right-walk.png')
		]
char3 = [pygame.image.load('pic/move-char/front.png'),
		 pygame.image.load('pic/move-char/side-right.png'), 
		 pygame.image.load('pic/move-char/side-right-walk.png'), 
		 pygame.image.load('pic/move-char/side-right-walk2.png'),
		 pygame.image.load('pic/move-char/side-right.png'), 
		 pygame.image.load('pic/move-char/side-right-walk.png'), 
		 pygame.image.load('pic/move-char/side-right-walk2.png'),
		 pygame.image.load('pic/move-char/side-right.png'), 
		 pygame.image.load('pic/move-char/side-right-walk.png')
		]
rect = char.get_rect()
rect1 = char1.get_rect()
# rect2 = char2.get_rect()