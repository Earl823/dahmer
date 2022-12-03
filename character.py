import pygame
pygame.init()

bg2 = pygame.image.load('pic/bg-dahmer.png')
bg2 = pygame.transform.scale(bg2, (800, 600))
char = pygame.image.load('pic/dahmer.png')
char1 = pygame.image.load('pic/blue-man.png')
char2 = pygame.image.load('pic/100ga.png')
rect = char.get_rect()
rect1 = char1.get_rect()
rect2 = char2.get_rect()