# import pygame
# import button
# from fighter import Fighter
# from pygame import mixer
# from fighting import Fighting
# import end
# import pause


# #-------------------------------------------------------------------------
# pygame.init()
# # create game window (tạo khung cho game)
# SCREEN_WIDTH= 1000
# SCREEN_HEIGHT= 600

# screen= pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
# pygame.display.set_caption('game base')

# #set framerate (vi fps qua cao, no di chuyen nhanh va muot, nen theo li ma noi, ta lai phari giam FPS xuong, dm di nguoc lai voi tu nhien :v)
# clock= pygame.time.Clock()
# FPS= 60

# #define color
# RED= (255, 0, 0)
# YELLOW= (255, 255, 0) 
# WHITE= (255, 255, 255)


# pause_img = pygame.image.load("images/Button/pause.png").convert_alpha()
# pause_button = button.Button(950, 550, pause_img, 0.15)


# # condition to out each of frames

# totally_quit= [10]
# run_of_main= [10]
# run_of_fighting= [10]
# run_of_pause= [10]
# run_of_end= [10]


# run_of_fighting[0]= True
# # run_of_end[0]= True	
# # run_of_main[0]= True


# while run_of_fighting[0]:
# 	screen.fill((52, 78, 91))
# 	clock.tick(FPS)
# 	totally_quit [0]= 0
# 	if pause_button.draw(screen): 


# 		run_of_pause[0]= True

# 		while run_of_pause[0]:
			
# 			pause.Pause(totally_quit, run_of_pause, run_of_fighting, run_of_main, screen)

# 			for event in pygame.event.get():
# 				if event.type == pygame.QUIT:
# 					run_of_end = False

# 			pygame.display.update()

# 	# if run_of_end[0]= 1 and totally_quit[0]= 1: run_of_pause[0]= False

# 	for event in pygame.event.get():
# 		if event.type == pygame.QUIT:
# 			run_of_pause = False		
# 	pygame.display.update()

# pygame.quit()
mai=[""]
mai[0]="1"
if mai[0]=="1": print("Yes")
else: print("No")