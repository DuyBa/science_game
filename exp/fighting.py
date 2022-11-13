import pygame
from fighter import Fighter
from pygame import mixer
import button
import p_e

class Fighting():

	def __init__(self, hero1, hero2, take_bg, take_music):
		self.size_data_hero1= hero1[0]
		self.scale_data_hero1= hero1[1]
		self.offset_data_hero1= hero1[2]
		self.step_data_hero1= hero1[3]
		self.hero1_address= hero1[4]
		
		self.size_data_hero2= hero2[0]
		self.scale_data_hero2= hero2[1]
		self.offset_data_hero2= hero2[2]
		self.step_data_hero2= hero2[3]
		self.hero2_address= hero2[4]
		
		self.take_bg= take_bg
		self.take_music= take_music
	game_stop=False
	def play_immediately(self, totally_quit, run_of_pause, run_of_fighting, run_of_main, run_of_end,game_start,menu_state):

		pygame.init()

		# create game window (tạo khung cho game)
		SCREEN_WIDTH= 1000
		SCREEN_HEIGHT= 600

		screen= pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
		pygame.display.set_caption("countervailing game")

		#set framerate (vi fps qua cao, no di chuyen nhanh va muot, nen theo li ma noi, ta lai phari giam FPS xuong, dm di nguoc lai voi tu nhien :v)
		clock= pygame.time.Clock()
		FPS= 60

		#define color
		RED= (255, 0, 0)
		YELLOW= (255, 255, 0) 
		WHITE= (255, 255, 255)

		#define game variables
		intro_count= 0
		last_count_update= pygame.time.get_ticks()
		score= [0, 0] #player score [p1, p2]
		round_over= False
		ROUND_OVER_COOLDOWN= 2000

		#define fighter variables
		# WARRIOR_SIZE= [162, 162] #old
		# WIZARD_SIZE= [250, 250]  #old

		# WARRIOR_SIZE= [64, 44]  #new
		# WIZARD_SIZE= [231, 190]	  #new

		#take data from self: a list include 2 int agr
		WARRIOR_SIZE= self.size_data_hero1
		WIZARD_SIZE= self.size_data_hero2

		# WARRIOR_SCALE= 4 old
		# WIZARD_SCALE= 3 old
		# WARRIOR_SCALE= 4.9 new
		# WIZARD_SCALE= 2.3 new
		#take data from self, a double or int agr
		WARRIOR_SCALE= self.scale_data_hero1
		WIZARD_SCALE= self.scale_data_hero2

		# WARRIOR_OFFSET= [72, 56] old
		# WIZARD_OFFSET= [112, 107]
		# WARRIOR_OFFSET= [15, 7] new
		# WIZARD_OFFSET= [112, 63]
		#take data form self, a list include 2 int agr
		WARRIOR_OFFSET= self.offset_data_hero1
		WIZARD_OFFSET= self.offset_data_hero2

		WARRIOR_DATA= [WARRIOR_SIZE, WARRIOR_SCALE, WARRIOR_OFFSET]
		WIZARD_DATA= [WIZARD_SIZE, WIZARD_SCALE, WIZARD_OFFSET]

		#load music and sound
		#take music form self: a string
		# pygame.mixer.music.load("assets/audio/lop13.mp3") old
		pygame.mixer.music.load(self.take_music)
		pygame.mixer.music.set_volume(0) #20
		pygame.mixer.music.play(-1, 0.0, 5000)
		sword_fx= pygame.mixer.Sound("assets/muontam/audio/sword.wav")
		sword_fx.set_volume(0.5)
		magic_fx= pygame.mixer.Sound("assets/muontam/audio/magic.wav")
		magic_fx.set_volume(0.75)



		#load background image (chay phong nen)
		#bg_image= pygame.image.load("assets/Flat Night 2 BG/Flat Night 2 BG.png").convert_alpha() old
		#bg_image= pygame.image.load("assets/Background/Demo.png").convert_alpha() 
		#take background from data: a string
		bg_image= pygame.image.load(self.take_bg).convert_alpha()

		#load spritesheets
		# warrior_sheet= pygame.image.load("assets/muontam/images/warrior/Sprites/warrior.png").convert_alpha() old
		# wizard_sheet= pygame.image.load("assets/muontam/images/wizard/Sprites/wizard.png").convert_alpha() old
		# warrior_sheet= pygame.image.load("assets/Warrior-V1.3/aaa.png").convert_alpha() 
		# wizard_sheet= pygame.image.load("assets/Wizard Pack/aa.png").convert_alpha() 
		#take address from data: a string
		warrior_sheet= pygame.image.load(self.hero1_address).convert_alpha() 
		wizard_sheet= pygame.image.load(self.hero2_address).convert_alpha() 

		#load victory image
		victory_img= pygame.image.load("assets/muontam/images/icons/victory.png").convert_alpha()

		#define number of steps in each animations
		# WARRIOR_ANIMATION_STEPS= [10, 8, 1, 7 ,7, 3, 7] old
		# WIZARD_ANIMATION_STEPS= [8, 8, 1, 8, 8, 3, 7]	old
		# WARRIOR_ANIMATION_STEPS= [6, 8, 3, 12 ,10, 4, 10] new
		# WIZARD_ANIMATION_STEPS= [6, 8, 2, 8, 8, 4, 7]	
		#take data from self, a list
		WARRIOR_ANIMATION_STEPS= self.step_data_hero1
		WIZARD_ANIMATION_STEPS= self.step_data_hero2

		#define font
		count_font= pygame.font.Font("assets/muontam/fonts/turok.ttf", 80)
		score_font= pygame.font.Font("assets/muontam/fonts/turok.ttf", 30)

		#funtion for drawing tect
		def draw_text(text, font, text_col, x, y):
			img= font.render(text, True, text_col)
			screen.blit(img, (x, y))


		#function for drawing background (thang bg_img chi la 1 bien khoi tao, chung ta phai tao ham de goi no, xong no se luu vao bo nho memory va ta se cho chay trong vong lap)
		def draw_bg():
			#vi bg cua chung ta ko fit size nen chung ta se resize lai, ok
			scaled_bg= pygame.transform.scale(bg_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
			screen.blit(scaled_bg, (0, 0))

		#function for drawing fight health bars
		def draw_health_bar(health, x, y):
			ratio= health/  100
			pygame.draw.rect(screen, RED, (x, y, 400, 30))
			pygame.draw.rect(screen, YELLOW, (x, y, 400* ratio, 30))


		#create 2 instance of fighters (chac chan se co 2 thang tren man hinh, nen ta tao 2 tk)
		fighter_1 = Fighter(1, 200, 340, False, WARRIOR_DATA,warrior_sheet, WARRIOR_ANIMATION_STEPS, sword_fx)
		fighter_2 = Fighter(2, 700, 340, True, WIZARD_DATA,wizard_sheet, WIZARD_ANIMATION_STEPS, magic_fx)

		# pause 
		pause_img = pygame.image.load("images/Button/pause.png").convert_alpha()
		pause_button = button.Button(950, 550, pause_img, 0.15)


		#game loop (tao vong lap cho game, tat ca moi thu se dien ra tai day)
		# run= True
		# while run:

		# 	clock.tick(FPS)

		# 	#draw beackground (ve nen trong nay)
		# 	draw_bg()

			

		# 	#show health bars
		# 	draw_health_bar(fighter_1.health, 20, 20)
		# 	draw_health_bar(fighter_2.health, 580, 20)
		# 	draw_text("P1: "+ str(score[0]), score_font, RED, 20, 60)
		# 	draw_text("P2: "+ str(score[1]), score_font, RED, 580, 60)

		# 	#update countdown
		# 	if intro_count<= 0:
		# 		#move fighters (goi thang nay ra de di chuyen)
		# 		fighter_1.move(SCREEN_WIDTH, SCREEN_HEIGHT, screen, fighter_2, round_over)
		# 		fighter_2.move(SCREEN_WIDTH, SCREEN_HEIGHT, screen, fighter_1, round_over)
		# 	else:
		# 		#display count timer
		# 		draw_text(str(intro_count), count_font, RED, SCREEN_WIDTH/ 2- 30, SCREEN_HEIGHT/ 2)
		# 		#update count timer
		# 		if(pygame.time.get_ticks()- last_count_update) >= 1000:
		# 			intro_count-= 1
		# 			last_count_update= pygame.time.get_ticks()
		# 			#print(intro_count)



		# 	#update fighters
		# 	fighter_1.update()
		# 	fighter_2.update()

		# 	#draw fighters (ve 2 thang o day)
		# 	fighter_1.draw(screen)
		# 	fighter_2.draw(screen)


		# 	#check for player defeated
		# 	if round_over== False:
		# 		if fighter_1.alive== False:
		# 			score[1]+= 1
		# 			round_over= True
		# 			round_over_time= pygame.time.get_ticks()
		# 		elif fighter_2.alive== False:
		# 			score[0]+= 1
		# 			round_over= True
		# 			round_over_time= pygame.time.get_ticks()
		# 	else:
		# 		#display victory img
		# 		screen.blit(victory_img, (360, 150))
		# 		if pygame.time.get_ticks()- round_over_time> ROUND_OVER_COOLDOWN:
		# 			round_over= False
		# 			intro_count= 3
		# 			#create 2 instance of fighters (chac chan se co 2 thang tren man hinh, nen ta tao 2 tk)
		# 			fighter_1 = Fighter(1, 200, 340, False, WARRIOR_DATA,warrior_sheet, WARRIOR_ANIMATION_STEPS, sword_fx)
		# 			fighter_2 = Fighter(2, 700, 340, True, WIZARD_DATA,wizard_sheet, WIZARD_ANIMATION_STEPS, magic_fx)
		# 	if score[0]	==2 or score[1]==2:
		# 		game_stop=True
		# 		#end.End(game_stop)

		# 	run_of_end= True
		# 	totally_quit= 0
			
		# 	if pause_button.draw(screen):
		# 		while run_of_end:
		# 			# end.End()

		# 			# if yes_button.draw(screen):
		# 			# 	game_start = True
		# 			# if no_button.draw(screen):
		# 			# 	runn= False

		# 			# screen= pygame.display.set_mode((1000, 600))
		# 			plagain_img = pygame.image.load('images/Button/playagain.png')
		# 			gameover_img = pygame.image.load('images/Button/gameover.png').convert_alpha()
		# 			scale_plagain_img = pygame.transform.scale(plagain_img, (200,100))
		# 			screen.blit(scale_plagain_img,(380,220))

		# 			scale_gameover_img = pygame.transform.scale(gameover_img, (300,100))
		# 			screen.blit(scale_gameover_img,(335,100))
					
		# 			game_over_img = pygame.image.load("images/Button/gameover.png").convert_alpha()
		# 			yes_img = pygame.image.load("images/Button/yes.png").convert_alpha()
		# 			no_img = pygame.image.load("images/Button/no.png").convert_alpha()

		# 					#create button instances
		# 			yes_button  = button.Button(400, 350, yes_img, 0.2)
		# 			no_button = button.Button(500, 350, no_img, 0.2)
		# 			if yes_button.draw(screen):
		# 				pause_button.clicked = False
		# 				run_of_end= False
		# 			if no_button.draw(screen):
		# 				# game.QUIT
		# 				totally_quit= 1
		# 				run_of_end= False




		# 			for event in pygame.event.get():
		# 				if event.type == pygame.QUIT:
		# 					run_of_end = False	
					
		# 			pygame.display.update()

		# 	if run_of_end== False and totally_quit== 1: run= False

		# 	#event handler (xu li de thoat game, ko de cho vong lap vo tan)
		# 	for event in pygame.event.get():
		# 		if event.type== pygame.QUIT:
		# 			run= False

		# 	#update display(nom na la trong vong loop co rat nhieu thay doi, sau moi vong lap, ta phai cap nhat nen lai ngay lap tuc)
		# 	pygame.display.update()


		# new update 11:20 05/11/2022
		
		while run_of_fighting[0]:

			clock.tick(FPS)

			#draw beackground (ve nen trong nay)
			draw_bg()

			

			#show health bars
			draw_health_bar(fighter_1.health, 20, 20)
			draw_health_bar(fighter_2.health, 580, 20)
			draw_text("P1: "+ str(score[0]), score_font, RED, 20, 60)
			draw_text("P2: "+ str(score[1]), score_font, RED, 580, 60)

			#update countdown
			if intro_count<= 0:
				#move fighters (goi thang nay ra de di chuyen)
				fighter_1.move(SCREEN_WIDTH, SCREEN_HEIGHT, screen, fighter_2, round_over)
				fighter_2.move(SCREEN_WIDTH, SCREEN_HEIGHT, screen, fighter_1, round_over)
			else:
				#display count timer
				draw_text(str(intro_count), count_font, RED, SCREEN_WIDTH/ 2- 30, SCREEN_HEIGHT/ 2)
				#update count timer
				if(pygame.time.get_ticks()- last_count_update) >= 1000:
					intro_count-= 1
					last_count_update= pygame.time.get_ticks()
					#print(intro_count)



			#update fighters
			fighter_1.update()
			fighter_2.update()

			#draw fighters (ve 2 thang o day)
			fighter_1.draw(screen)
			fighter_2.draw(screen)


			#check for player defeated
			if round_over== False:
				if fighter_1.alive== False:
					score[1]+= 1
					round_over= True
					round_over_time= pygame.time.get_ticks()
				elif fighter_2.alive== False:
					score[0]+= 1
					round_over= True
					round_over_time= pygame.time.get_ticks()
			else:
				#display victory img
				screen.blit(victory_img, (360, 150))
				if pygame.time.get_ticks()- round_over_time> ROUND_OVER_COOLDOWN:
					round_over= False
					intro_count= 3
					#create 2 instance of fighters (chac chan se co 2 thang tren man hinh, nen ta tao 2 tk)
					fighter_1 = Fighter(1, 200, 340, False, WARRIOR_DATA,warrior_sheet, WARRIOR_ANIMATION_STEPS, sword_fx)
					fighter_2 = Fighter(2, 700, 340, True, WIZARD_DATA,wizard_sheet, WIZARD_ANIMATION_STEPS, magic_fx)

			run_of_end[0]= True
			if score[0]	==2 or score[1]==2:
				while run_of_end[0]:
				
					p_e.End(totally_quit, run_of_pause, run_of_fighting, run_of_main,run_of_end,game_start,menu_state, screen)

					for event in pygame.event.get():
						if event.type == pygame.QUIT:
							run_of_pause[0] = False

					pygame.display.update()

			if pause_button.draw(screen): 
				run_of_pause[0]= True
				while run_of_pause[0]:
					p_e.Pause(totally_quit, run_of_pause, run_of_fighting, run_of_main,game_start, menu_state, screen)

					for event in pygame.event.get():
						if event.type == pygame.QUIT:
							run_of_pause[0] = False

					pygame.display.update()
					

			#event handler (xu li de thoat game, ko de cho vong lap vo tan)
			for event in pygame.event.get():
				if event.type== pygame.QUIT:
					run_of_main[0]= run_of_fighting[0]= False

			#update display(nom na la trong vong loop co rat nhieu thay doi, sau moi vong lap, ta phai cap nhat nen lai ngay lap tuc)
			pygame.display.update()


		#exit pygame (thoat khoi tat ca)
		# pygame.quit()
































# import pygame
# from fighter import Fighter
# from pygame import mixer

# pygame.init()

# # create game window (tạo khung cho game)
# SCREEN_WIDTH= 1000
# SCREEN_HEIGHT= 600

# screen= pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
# pygame.display.set_caption("countervailing game")

# #set framerate (vi fps qua cao, no di chuyen nhanh va muot, nen theo li ma noi, ta lai phari giam FPS xuong, dm di nguoc lai voi tu nhien :v)
# clock= pygame.time.Clock()
# FPS= 60

# #define color
# RED= (255, 0, 0)
# YELLOW= (255, 255, 0) 
# WHITE= (255, 255, 255)

# #define game variables
# intro_count= 0
# last_count_update= pygame.time.get_ticks()
# score= [0, 0] #player score [p1, p2]
# round_over= False
# ROUND_OVER_COOLDOWN= 2000

# #define fighter variables
# # WARRIOR_SIZE= [162, 162] #old
# # WIZARD_SIZE= [250, 250]  #old

# WARRIOR_SIZE= [64, 44]  #new
# WIZARD_SIZE= [231, 190]	  #new

# # WARRIOR_SCALE= 4
# # WIZARD_SCALE= 3
# WARRIOR_SCALE= 4.9
# WIZARD_SCALE= 2.3

# # WARRIOR_OFFSET= [72, 56]
# # WIZARD_OFFSET= [112, 107]
# WARRIOR_OFFSET= [15, 7]
# WIZARD_OFFSET= [112, 63]

# WARRIOR_DATA= [WARRIOR_SIZE, WARRIOR_SCALE, WARRIOR_OFFSET]
# WIZARD_DATA= [WIZARD_SIZE, WIZARD_SCALE, WIZARD_OFFSET]

# #load music and sound
# pygame.mixer.music.load("assets/audio/lop13.mp3")
# pygame.mixer.music.set_volume(0) #20
# pygame.mixer.music.play(-1, 0.0, 5000)
# sword_fx= pygame.mixer.Sound("assets/muontam/audio/sword.wav")
# sword_fx.set_volume(0.5)
# magic_fx= pygame.mixer.Sound("assets/muontam/audio/magic.wav")
# magic_fx.set_volume(0.75)



# #load background image (chay phong nen)
# #bg_image= pygame.image.load("assets/Flat Night 2 BG/Flat Night 2 BG.png").convert_alpha() old
# bg_image= pygame.image.load("assets/Background/Demo.png").convert_alpha()

# #load spritesheets
# # warrior_sheet= pygame.image.load("assets/muontam/images/warrior/Sprites/warrior.png").convert_alpha() old
# # wizard_sheet= pygame.image.load("assets/muontam/images/wizard/Sprites/wizard.png").convert_alpha() old
# warrior_sheet= pygame.image.load("assets/Warrior-V1.3/aaa.png").convert_alpha() 
# wizard_sheet= pygame.image.load("assets/Wizard Pack/aa.png").convert_alpha() 

# #load victory image
# victory_img= pygame.image.load("assets/muontam/images/icons/victory.png").convert_alpha()

# #define number of steps in each animations
# # WARRIOR_ANIMATION_STEPS= [10, 8, 1, 7 ,7, 3, 7] old
# # WIZARD_ANIMATION_STEPS= [8, 8, 1, 8, 8, 3, 7]	old
# WARRIOR_ANIMATION_STEPS= [6, 8, 3, 12 ,10, 4, 10]
# WIZARD_ANIMATION_STEPS= [6, 8, 2, 8, 8, 4, 7]	

# #define font
# count_font= pygame.font.Font("assets/muontam/fonts/turok.ttf", 80)
# score_font= pygame.font.Font("assets/muontam/fonts/turok.ttf", 30)

# #funtion for drawing tect
# def draw_text(text, font, text_col, x, y):
# 	img= font.render(text, True, text_col)
# 	screen.blit(img, (x, y))


# #function for drawing background (thang bg_img chi la 1 bien khoi tao, chung ta phai tao ham de goi no, xong no se luu vao bo nho memory va ta se cho chay trong vong lap)
# def draw_bg():
# 	#vi bg cua chung ta ko fit size nen chung ta se resize lai, ok
# 	scaled_bg= pygame.transform.scale(bg_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
# 	screen.blit(scaled_bg, (0, 0))

# #function for drawing fight health bars
# def draw_health_bar(health, x, y):
# 	ratio= health/  100
# 	pygame.draw.rect(screen, RED, (x, y, 400, 30))
# 	pygame.draw.rect(screen, YELLOW, (x, y, 400* ratio, 30))


# #create 2 instance of fighters (chac chan se co 2 thang tren man hinh, nen ta tao 2 tk)
# fighter_1 = Fighter(1, 200, 340, False, WARRIOR_DATA,warrior_sheet, WARRIOR_ANIMATION_STEPS, sword_fx)
# fighter_2 = Fighter(2, 700, 340, True, WIZARD_DATA,wizard_sheet, WIZARD_ANIMATION_STEPS, magic_fx)


# #game loop (tao vong lap cho game, tat ca moi thu se dien ra tai day)
# run= True
# while run:

# 	clock.tick(FPS)

# 	#draw beackground (ve nen trong nay)
# 	draw_bg()

# 	#show health bars
# 	draw_health_bar(fighter_1.health, 20, 20)
# 	draw_health_bar(fighter_2.health, 580, 20)
# 	draw_text("P1: "+ str(score[0]), score_font, RED, 20, 60)
# 	draw_text("P2: "+ str(score[1]), score_font, RED, 580, 60)

# 	#update countdown
# 	if intro_count<= 0:
# 		#move fighters (goi thang nay ra de di chuyen)
# 		fighter_1.move(SCREEN_WIDTH, SCREEN_HEIGHT, screen, fighter_2, round_over)
# 		fighter_2.move(SCREEN_WIDTH, SCREEN_HEIGHT, screen, fighter_1, round_over)
# 	else:
# 		#display count timer
# 		draw_text(str(intro_count), count_font, RED, SCREEN_WIDTH/ 2- 30, SCREEN_HEIGHT/ 2)
# 		#update count timer
# 		if(pygame.time.get_ticks()- last_count_update) >= 1000:
# 			intro_count-= 1
# 			last_count_update= pygame.time.get_ticks()
# 			#print(intro_count)



# 	#update fighters
# 	fighter_1.update()
# 	fighter_2.update()

# 	#draw fighters (ve 2 thang o day)
# 	fighter_1.draw(screen)
# 	fighter_2.draw(screen)


# 	#check for player defeated
# 	if round_over== False:
# 		if fighter_1.alive== False:
# 			score[1]+= 1
# 			round_over= True
# 			round_over_time= pygame.time.get_ticks()
# 		elif fighter_2.alive== False:
# 			score[0]+= 1
# 			round_over= True
# 			round_over_time= pygame.time.get_ticks()
# 	else:
# 		#display victory img
# 		screen.blit(victory_img, (360, 150))
# 		if pygame.time.get_ticks()- round_over_time> ROUND_OVER_COOLDOWN:
# 			round_over= False
# 			intro_count= 3
# 			#create 2 instance of fighters (chac chan se co 2 thang tren man hinh, nen ta tao 2 tk)
# 			fighter_1 = Fighter(1, 200, 340, False, WARRIOR_DATA,warrior_sheet, WARRIOR_ANIMATION_STEPS, sword_fx)
# 			fighter_2 = Fighter(2, 700, 340, True, WIZARD_DATA,wizard_sheet, WIZARD_ANIMATION_STEPS, magic_fx)

# 	#event handler (xu li de thoat game, ko de cho vong lap vo tan)
# 	for event in pygame.event.get():
# 		if event.type== pygame.QUIT:
# 			run= False

# 	#update display(nom na la trong vong loop co rat nhieu thay doi, sau moi vong lap, ta phai cap nhat nen lai ngay lap tuc)
# 	pygame.display.update()


# #exit pygame (thoat khoi tat ca)
# pygame.quit()