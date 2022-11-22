import pygame
import button

pygame.init()

#creat window menu - tạo cửa sổ menu
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1000

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Main Menu")

#font 
font1 = pygame.font.SysFont("Segoe Script", 50)
font2 = pygame.font.SysFont("Arial", 50)


#load background
bg_image = pygame.image.load('images/Background/backgroundTN.jpg').convert_alpha()
picture1 = pygame.image.load('images/Pictures/bayhoi_completed.png').convert_alpha()
picture2 = pygame.image.load('images/Background/hoicham_1.png').convert_alpha()
compass_image = pygame.image.load('images/Compass/baban.png').convert_alpha()
sun_img = pygame.image.load('images/Sunrise/sun_png.png').convert_alpha()

#load button imgs
# start_img = pygame.image.load("images/Icon/start_btn.png").convert_alpha()
home_img = pygame.image.load("images/Icon/home_btn.png")
setting_img = pygame.image.load("images/Icon/setting_btn.png")
undo_img = pygame.image.load("images/Icon/undo_btn.png")
close_img = pygame.image.load("images/Icon/close_btn.png")
next_img = pygame.image.load("images/Icon/next_btn.png")
choice1_img = pygame.image.load("images/Temp/choice1_btn.png")
choice2_img = pygame.image.load("images/Temp/choice2_btn.png")
choice3_img = pygame.image.load("images/Temp/choice3_btn.png")
correct_img = pygame.image.load("images/Message/correct.png")



#create button instances
home_btn = button.Button(10, 10, home_img, 1)
setting_btn = button.Button(80, 10, setting_img, 1)
undo_btn = button.Button(150, 10, undo_img, 1)
close_btn = button.Button(900, 10, close_img, 0.8)
next_btn = button.Button(900, 500, next_img, 0.8)
pic1 = button.Button(390, 140, picture1, 0.4)
pic2 = button.Button(-80, 220, picture2, 0.4)
option1_btn = button.Button(150, 450, choice1_img, 0.4)
option2_btn = button.Button(400, 470, choice2_img, 0.4)
option3_btn = button.Button(625, 465, choice3_img, 0.4)
compass = button.Button(400, 220, compass_image, 0.4)
sun_btn = button.Button(400, 420, sun_img, 0.3)
correct_btn =button.Button(-10, 200, correct_img, 0.5)
#draw background 
def draw_bg():
   scale_bg = pygame.transform.scale(bg_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
   screen.blit(scale_bg, (0,0))

#draw text
def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)
    
#game loop 
def frame1():
    run = True
    while run:
        screen.fill((118,145,176))
        #draw background
        #draw_bg()  
        #draw_text('Lets study', font, (255,50,50), screen, 20, 20)
        # draw_text('BRAIN OUT', font, (255,50,50), screen, 380, 120)
        # if start_button.draw(screen):
        #     pass
        draw_text('At what temperature does water boil?', font2, (0,0,0), screen, 100, 100)
        # draw button 
        home_btn.draw(screen)
        setting_btn.draw(screen)
        undo_btn.draw(screen)
        next_btn.draw(screen)
        close_btn.draw(screen)
        option1_btn.draw(screen)
        option2_btn.draw(screen)
        option3_btn.draw(screen)
        
        # draw picture
        pic1.draw(screen)
        pic2.draw(screen)
        
        #event handler
        for event in pygame.event.get():
            #quit game 
            if event.type == pygame.QUIT:
                run = False
                
        pygame.display.update()
    
def frame2():
    
#game loop 
    run = True
    while run:
        screen.fill((118,145,176))
        #draw background
        #draw_bg()  
        #draw_text('Lets study', font, (255,50,50), screen, 20, 20)
        # draw_text('BRAIN OUT', font, (255,50,50), screen, 380, 120)
        # if start_button.draw(screen):
        #     pass
        draw_text('At what temperature does water freeze?', font2, (255,255,255), screen, 100, 100)
        # draw button 
        home_btn.draw(screen)
        setting_btn.draw(screen)
        undo_btn.draw(screen)
        next_btn.draw(screen)
        close_btn.draw(screen)
        option1_btn.draw(screen)
        option2_btn.draw(screen)
        option3_btn.draw(screen)
        
        
        # draw picture
        pic1.draw(screen)
        pic2.draw(screen)
        
        #event handler
        for event in pygame.event.get():
            #quit game 
            if event.type == pygame.QUIT:
                run = False
    pygame.display.update()
    
    
def frame3():
    
    #game loop 
    run = True
    while run:
        screen.fill((118,145,176))
        #draw background
        #draw_bg()  
        #draw_text('Lets study', font, (255,50,50), screen, 20, 20)
        # draw_text('BRAIN OUT', font, (255,50,50), screen, 380, 120)
        # if start_button.draw(screen):
        #     pass
        draw_text('Which direction does the sun rise?', font2, (255,255,255), screen, 100, 100)
        # draw button 
        home_btn.draw(screen)
        setting_btn.draw(screen)
        undo_btn.draw(screen)
        next_btn.draw(screen)
        close_btn.draw(screen)
        
        
        
        # draw picture
        
        compass.draw(screen)
        #pic3.draw(screen)
        sun_btn.draw(screen)
        correct_btn.draw(screen)
        
        #event handler
        for event in pygame.event.get():
            #quit game 
            if event.type == pygame.QUIT:
                run = False
        pygame.display.update()
    
pygame.quit()