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
font2 = pygame.font.SysFont("Arial", 35)


#load background
bg_image = pygame.image.load('images/Background/backgroundTN.jpg').convert_alpha()
picture1 = pygame.image.load('images/Freeze/nuocda.png').convert_alpha()
picture2 = pygame.image.load('images/Background/hoicham_1.png').convert_alpha()
picture3 = pygame.image.load('images/Background/hoicham_2.png').convert_alpha()
tuinamdoc_image = pygame.image.load('images/Bag/tui_nam_doc_img.png').convert_alpha()
tuinamthuong_image = pygame.image.load('images/Bag/tui_nam_thuong_img.png').convert_alpha()


#load button imgs
# start_img = pygame.image.load("images/Icon/start_btn.png").convert_alpha()
home_img = pygame.image.load("images/Icon/home_btn.png")
setting_img = pygame.image.load("images/Icon/setting_btn.png")
undo_img = pygame.image.load("images/Icon/undo_btn.png")
close_img = pygame.image.load("images/Icon/close_btn.png")
next_img = pygame.image.load("images/Icon/next_btn.png")
correct_img = pygame.image.load("images/Message/correct.png")
about_img = pygame.image.load('images/Icon/about.png')
namdoc1_img = pygame.image.load("images/Bag/namdoc1.png")
namdoc2_img = pygame.image.load("images/Bag/namdoc2.png")
namthuong1_img = pygame.image.load("images/Bag/namthuong1.png")
namthuong2_img = pygame.image.load("images/Bag/namthuong2.png")





#create button instances
home_btn = button.Button(10, 10, home_img, 1)
setting_btn = button.Button(80, 10, setting_img, 1)
undo_btn = button.Button(150, 10, undo_img, 1)
close_btn = button.Button(900, 10, close_img, 0.8)
next_btn = button.Button(900, 500, next_img, 0.8)
about_btn = button.Button(10, 545,about_img,1)

pic1 = button.Button(180, 140, picture1, 0.8)
#pic2 = button.Button(-80, 220, picture2, 0.4)
pic3 = button.Button(-30, 350, picture3, 0.4)
tuinamdoc_btn = button.Button(10,155,tuinamdoc_image,0.5)
tuinamthuong_btn = button.Button(300,155,tuinamthuong_image,0.5)
namdoc1_btn = button.Button(600, 150, namdoc1_img, 0.15)
namdoc2_btn = button.Button(800, 140, namdoc2_img, 0.7)
namthuong1_btn = button.Button(600, 350, namthuong1_img, 0.15)
namthuong2_btn = button.Button(800, 320, namthuong2_img, 0.25)
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
run = True
while run:
    screen.fill((118,145,176))
    #draw background
    #draw_bg()  
    #draw_text('Lets study', font, (255,50,50), screen, 20, 20)
    # draw_text('BRAIN OUT', font, (255,50,50), screen, 380, 120)
    # if start_button.draw(screen):
    #     pass
    draw_text('Distinguish poisonous and common mushrooms', font2, (255,255,255), screen, 100, 100)
    # draw button 
    home_btn.draw(screen)
    setting_btn.draw(screen)
    undo_btn.draw(screen)
    next_btn.draw(screen)
    close_btn.draw(screen)
    about_btn.draw(screen)
    
    tuinamdoc_btn.draw(screen)
    tuinamthuong_btn.draw(screen)
    namdoc1_btn.draw(screen)
    namdoc2_btn.draw(screen)
    namthuong1_btn.draw(screen)
    namthuong2_btn.draw(screen)
    
    
    
    
    # draw picture
    
    
    #event handler
    for event in pygame.event.get():
        #quit game 
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()
    
pygame.quit()