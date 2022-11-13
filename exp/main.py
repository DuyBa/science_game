import pygame
import button
from fighter import Fighter
from pygame import mixer
from fighting import Fighting



#-------------------------------------------------------------------------
pygame.init()
# create game window (tạo khung cho game)
SCREEN_WIDTH= 1000
SCREEN_HEIGHT= 600

screen= pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('game base')

#set framerate (vi fps qua cao, no di chuyen nhanh va muot, nen theo li ma noi, ta lai phari giam FPS xuong, dm di nguoc lai voi tu nhien :v)
clock= pygame.time.Clock()
FPS= 60

#define color
RED= (255, 0, 0)
YELLOW= (255, 255, 0) 
WHITE= (255, 255, 255)

font = pygame.font.SysFont(None, 20)

font = pygame.font.SysFont("Segoe Script", 40)

#---------------------------------------------------------------------------
def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)
 




#---------------------bload button images-------------------------
start_img = pygame.image.load("images/Button/start.png").convert_alpha()
quit_img = pygame.image.load("images/Button/exit.png").convert_alpha()
game_over_img = pygame.image.load("images/Button/gameover.png").convert_alpha()
yes_img = pygame.image.load("images/Button/yes.png").convert_alpha()
no_img = pygame.image.load("images/Button/no.png").convert_alpha()
fight_img = pygame.image.load("images/Button/fight.png").convert_alpha()
next_img = pygame.image.load("images/Button/next.png").convert_alpha()

hero1_img = pygame.image.load("images/character/1.png").convert_alpha()
hero2_img = pygame.image.load("images/character/2.png").convert_alpha()
hero3_img = pygame.image.load("images/character/3.png").convert_alpha()
hero4_img = pygame.image.load("images/character/4.png").convert_alpha()

music1_img = pygame.image.load("images/music/flo.jpg").convert_alpha()
music2_img = pygame.image.load("images/music/lop13.jpg").convert_alpha()

bg1_img = pygame.image.load("images/background/Demo.png").convert_alpha()
bg2_img = pygame.image.load("images/background/Flat Night 2 BG.png").convert_alpha()
#---------------------------------------------------------------------------

#-----------------------create button instances-----------------------------
start_button = button.Button(180, 270, start_img, 0.8)
quit_button = button.Button(582, 270, quit_img, 0.8)
yes_button  = button.Button(400, 350, yes_img, 0.2)
no_button = button.Button(500, 350, no_img, 0.2)
fight_button = button.Button(500,300,fight_img,0.8)
next_button = button.Button(850, 250, next_img, 0.2)

hero1_1_button= button.Button(120, 120, hero1_img, 1.5)
hero2_1_button= button.Button(320, 155, hero2_img, 2.2)
hero3_1_button= button.Button(520, 160, hero3_img, 3)
hero4_1_button= button.Button(670, 85, hero4_img, 1.8)

hero1_2_button= button.Button(120, 385, hero1_img, 1.5)
hero2_2_button= button.Button(320, 420, hero2_img, 2.2)
hero3_2_button= button.Button(520, 425, hero3_img, 3)
hero4_2_button= button.Button(670, 350, hero4_img, 1.8)

music1_button = button.Button(120, 120, music1_img, 0.4)
music2_button = button.Button(520, 120, music2_img, 0.95)

bg1_button = button.Button(120, 380, bg1_img, 0.65)
bg2_button = button.Button(520, 380, bg2_img, 0.18)

fight_game = button.Button(800, 500, fight_img, 0.5)
#---------------------------------------------------------------------------

#--------------------------hero-------------------------------------
hero1= [[231, 190], 2.3, [112, 63], [6, 8, 2, 8, 8, 4, 7], "assets/Wizard Pack/aa.png"]
hero2= [[162, 162], 4, [72, 56], [10, 8, 1, 7, 7, 3, 7], "assets/muontam/images/warrior/Sprites/warrior.png"]
hero3= [[64, 44], 4.9, [15, 7], [6, 8, 3, 12, 10, 4, 10], "assets/Warrior-V1.3/aaa.png"]
hero4= [[250, 250], 3, [112, 107], [8, 8, 1, 8, 8, 3, 7], "assets/muontam/images/wizard/Sprites/wizard.png"]
#---------------------------------------------------------------------------
#menu_state = "main"

game_stop = False
run= True



# 05/11/2022 11:13 new update
totally_quit= [10]
run_of_main= [10]
run_of_fighting= [10]
run_of_pause= [10]
run_of_end= [10]
game_start = [10]
menu_state=[""]



run_of_main[0]= True
totally_quit[0]= 0
game_start[0] = False
menu_state[0] = "main"


main_bg= pygame.image.load("images/background/main_background.gif").convert_alpha()
select_bg= pygame.image.load("images/background/select.jpg").convert_alpha()

def draw_bg(your_bg):
	#vi bg cua chung ta ko fit size nen chung ta se resize lai, ok
	scaled_bg= pygame.transform.scale(your_bg, (SCREEN_WIDTH, SCREEN_HEIGHT))
	screen.blit(scaled_bg, (0, 0))

while run_of_main[0]:


	

	# screen.fill((52, 78, 91))
	clock.tick(FPS)
	
	#check if game is paused
	if game_start[0] == False:

	#check menu state
		if menu_state[0]=="main":
			draw_bg(main_bg)
			draw_text('Main Menu', font, (255, 255, 255), screen, 20, 20)
			draw_text('play for a while?', font, RED, screen, 325, 150)
			if start_button.draw(screen):
				menu_state[0]="hero"
			if quit_button.draw(screen):
				run_of_main[0] = False
		if menu_state[0]=="hero":
			# screen.fill((52, 78, 91))
			draw_bg(select_bg)

			draw_text("SELECT HERO1", font, RED,screen, 40, 50)
			if hero1_1_button.draw(screen):
				h1=hero1
			if hero2_1_button.draw(screen):
				h1=hero2
			if hero3_1_button.draw(screen):
				h1=hero3
			if hero4_1_button.draw(screen):
				h1=hero4

			draw_text("SELECT HERO2", font, RED,screen, 40, 300)
			if hero1_2_button.draw(screen):
				h2=hero1
			if hero2_2_button.draw(screen):
				h2=hero2
			if hero3_2_button.draw(screen):
				h2=hero3
			if hero4_2_button.draw(screen):
				h2=hero4

			if next_button.draw(screen):
				menu_state[0]="music_bg"

		if menu_state[0] =="music_bg":
			# screen.fill((52, 78, 91))
			draw_bg(select_bg)
			draw_text("MUSIC", font, RED,screen, 40, 50)
			if music1_button.draw(screen):
				take_music="assets/audio/flo.mp3"
			if music2_button.draw(screen):
				take_music="assets/audio/lop13.mp3" 

			draw_text("MAP", font, RED,screen, 40, 300)
			if bg1_button.draw(screen):
				take_bg="assets/Background/Demo.png"
			if bg2_button.draw(screen):
				take_bg="assets/Flat Night 2 BG/Flat Night 2 BG.png"
			if fight_game.draw(screen):
				game_start[0]=True

	#check if the options menu is open
	else:
		#khoi tao class
		dau_vao= Fighting(h1, h2, take_bg, take_music)
		#choi game
		run_of_fighting[0]= True
		dau_vao.play_immediately(totally_quit, run_of_pause, run_of_fighting, run_of_main, run_of_end, game_start, menu_state)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run_of_main[0] = False
			
			
	pygame.display.update()

pygame.quit()