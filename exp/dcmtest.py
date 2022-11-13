
from turtle import Screen
import pygame, sys
import button
from fighter import Fighter
from pygame import mixer
def End(run_of_end, run_of_pause, totally_quit):
	# screen= pygame.display.set_mode((1000, 600))
	# yes_img = pygame.image.load("images/Button/yes.png").convert_alpha()
	# yes_button  = button.Button(400, 350, yes_img, 0.2)
	# if yes_button.draw(screen):
	# 	game_start = True

	# for event in pygame.event.get():
	# 	if event.type == pygame.QUIT:
	# 		run_of_end[0] = False


	screen= pygame.display.set_mode((1000, 600))
	plagain_img = pygame.image.load('images/Button/playagain.png')
	gameover_img = pygame.image.load('images/Button/gameover.png').convert_alpha()
	scale_plagain_img = pygame.transform.scale(plagain_img, (200,100))
	screen.blit(scale_plagain_img,(380,220))

	scale_gameover_img = pygame.transform.scale(gameover_img, (300,100))
	screen.blit(scale_gameover_img,(335,100))
	
	game_over_img = pygame.image.load("images/Button/gameover.png").convert_alpha()
	yes_img = pygame.image.load("images/Button/yes.png").convert_alpha()
	no_img = pygame.image.load("images/Button/no.png").convert_alpha()

			#create button instances
	yes_button  = button.Button(400, 350, yes_img, 0.2)
	no_button = button.Button(500, 350, no_img, 0.2)
	if yes_button.draw(screen):
		run_of_end[0]= False
	if no_button.draw(screen):
		# game.QUIT
		run_of_end[0]= run_of_pause[0]= False