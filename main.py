import pygame
import draw
import button
import pause_end
import Frame1


pygame.init()



#-------------const_data----------------

SCREEN_WIDTH= 1000
SCREEN_HEIGHT= 600

BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED   = (255,   0,   0)

rectangle = pygame.rect.Rect(176, 134, 17, 17)
rectangle_draging = False

clock = pygame.time.Clock()
FPS= 1000





screen= pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('science game')

# font
font= pygame.font.SysFont("Wesminster", 40)

# button
pause_img= pygame.image.load("icon/x.png").convert_alpha()
pause_button= button.Button(910, 5, pause_img, 0.8)


# buttons for select_bg
button1_img= pygame.image.load("buttons/green1.png").convert_alpha()
button2_img= pygame.image.load("buttons/blue2.png").convert_alpha()
button3_img= pygame.image.load("buttons/purple3.png").convert_alpha()
button4_img= pygame.image.load("buttons/red4.png").convert_alpha()
button5_img= pygame.image.load("buttons/orange5.png").convert_alpha()
button6_img= pygame.image.load("buttons/yellow6.png").convert_alpha()
button7_img= pygame.image.load("buttons/green7.png").convert_alpha()
button8_img= pygame.image.load("buttons/blue8.png").convert_alpha()
button9_img= pygame.image.load("buttons/purple9.png").convert_alpha()
button10_img= pygame.image.load("buttons/red10.png").convert_alpha()
button11_img= pygame.image.load("buttons/orange11.png").convert_alpha()
button12_img= pygame.image.load("buttons/yellow12.png").convert_alpha()
button13_img= pygame.image.load("buttons/green13.png").convert_alpha()
button14_img= pygame.image.load("buttons/blue14.png").convert_alpha()
button15_img= pygame.image.load("buttons/purple15.png").convert_alpha()
button16_img= pygame.image.load("buttons/red16.png").convert_alpha()
button17_img= pygame.image.load("buttons/orange17.png").convert_alpha()
button18_img= pygame.image.load("buttons/yellow18.png").convert_alpha()

x= 30
button1_button= button.Button(200, 180+ x, button1_img, 0.65)
button2_button= button.Button(304, 180+ x, button2_img, 0.65)
button3_button= button.Button(408, 180+ x, button3_img, 0.65)
button4_button= button.Button(512, 180+ x, button4_img, 0.65)
button5_button= button.Button(616, 180+ x, button5_img, 0.65)
button6_button= button.Button(720, 180+ x, button6_img, 0.65)
button7_button= button.Button(200, 284+ x, button7_img, 0.65)
button8_button= button.Button(304, 284+ x, button8_img, 0.65)
button9_button= button.Button(408, 284+ x, button9_img, 0.65)
button10_button= button.Button(512, 284+ x, button10_img, 0.65)
button11_button= button.Button(616, 284+ x, button11_img, 0.65)
button12_button= button.Button(720, 284+ x, button12_img, 0.65)
button13_button= button.Button(200, 392+ x, button13_img, 0.65)
button14_button= button.Button(304, 392+ x, button14_img, 0.65)
button15_button= button.Button(408, 392+ x, button15_img, 0.65)
button16_button= button.Button(512, 392+ x, button16_img, 0.65)
button17_button= button.Button(616, 392+ x, button17_img, 0.65)
button18_button= button.Button(720, 392+ x, button18_img, 0.65)

# play button in main bg
play_img= pygame.image.load("icon/play.png").convert_alpha()
play_button= button.Button(460, 410, play_img, 0.8)

# bacground
main_bg= pygame.image.load("images/background/main.jpg").convert_alpha()

# img
brain_img= pygame.image.load("icon/logo2.png").convert_alpha()
select_img= pygame.image.load("images/background/select.png")

# runnnn
run_of_main= [10]
run_of_main[0]= True

run_of_pause= [10]


supertotal= [10]
supertotal[0]= True

select_frame= [10]
select_frame[0]= True

run_of_manf= []
run_of_manf.append(1)
run_of_manf.append(True)


status= 'man1'

xuong= [10]

while supertotal[0]:

	# -----------frame 1--------------
	if status== 'frame1':
		
		draw.draw_bg(main_bg, screen, 1000, 600)
		draw.draw_text('main menu', font, (0,0,0), screen, 20, 20)
		draw.draw_normally(brain_img, screen, 400, 400, 300, 60)

		if play_button.draw(screen):
			status= 'frame2'


		if pause_button.draw(screen):
			run_of_pause[0]= True
			while run_of_pause[0]:
				pause_end.Pause(supertotal,run_of_pause, run_of_main, screen)
					
				for event in pygame.event.get():
					if event.type == pygame.QUIT:
						run_of_pause[0] = supertotal[0]= False

				pygame.display.update()




		# for event in pygame.event.get():
		# 	if event.type== pygame.QUIT:
		# 		run_of_main[0]= supertotal[0]= False

		# pygame.display.update()


	if status== 'frame2':
		draw.draw_bg(select_img, screen, 1000, 600)
		draw.draw_text('select now, bro', font, (0,0,0), screen, 400, 150)
		if button1_button.draw(screen):
			status= 'man1'
		if button2_button.draw(screen):
			status= 'man2'
		if button3_button.draw(screen):
			status= 'man3'
		if button4_button.draw(screen):
			status= 'man4'
		if button5_button.draw(screen):
			status= 'man5'
		if button6_button.draw(screen):
			status= 'man6'
		if button7_button.draw(screen):
			status= 'man7'
		if button8_button.draw(screen):
			status= 'man8'
		if button9_button.draw(screen):
			status= 'man9'
		if button10_button.draw(screen):
			status= 'man10'
		if button11_button.draw(screen):
			status= 'man11'
		if button12_button.draw(screen):
			status= 'man12'
		if button13_button.draw(screen):
			status= 'man13'
		if button14_button.draw(screen):
			status= 'man14'
		if button15_button.draw(screen):
			status= 'man15'
		if button16_button.draw(screen):
			status= 'man16'
		if button17_button.draw(screen):
			status= 'man17'
		if button18_button.draw(screen):
			status= 'man18'

		if pause_button.draw(screen):
			run_of_pause[0]= True
			while run_of_pause[0]:
				pause_end.Pause(supertotal,run_of_pause, run_of_main, screen)
					
				for event in pygame.event.get():
					if event.type == pygame.QUIT:
						run_of_pause[0] = supertotal[0]= False

				pygame.display.update()

	if status== 'man1':

		run_of_manf[1]= True
		Frame1.runtest(run_of_manf, supertotal)

	if status== 'man2':
		pass
	if status== 'man3':
		pass
	if status== 'man4':
		pass
	if status== 'man5':
		pass
	if status== 'man6':
		pass
	if status== 'man7':
		pass
	if status== 'man8':
		pass
	if status== 'man9':
		pass
	if status== 'man10':
		pass
	if status== 'man11':
		pass
	if status== 'man12':
		pass
	if status== 'man13':
		pass
	if status== 'man14':
		pass
	if status== 'man15':
		pass
	if status== 'man16':
		pass
	if status== 'man17':
		pass
	if status== 'man18':
		pass









	






















	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			supertotal[0]= False

	pygame.display.update()


pygame.quit()

