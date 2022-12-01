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



#load button imgs
# start_img = pygame.image.load("images/Icon/start_btn.png").convert_alpha()
home_img = pygame.image.load("images/Icon/home_btn.png")
setting_img = pygame.image.load("images/Icon/setting_btn.png")
undo_img = pygame.image.load("images/Icon/undo_btn.png")
close_img = pygame.image.load("images/Icon/close_btn.png")
next_img = pygame.image.load("images/Icon/next_btn.png")
correct_img = pygame.image.load("images/Message/correct.png")
about_img = pygame.image.load('images/Icon/about.png')
sodo_img = pygame.image.load('images/Sodo/Sodoo.png')
gr_father_img = pygame.image.load('images/Sodo/GrFather.png')
gr_mother_img = pygame.image.load('images/Sodo/GrMother.png')
father_img = pygame.image.load('images/Sodo/Father.png')
mother_img = pygame.image.load('images/Sodo/Mother_cut.png')
child_img = pygame.image.load('images/Sodo/child_cut.png')



#create button instances
home_btn = button.Button(10, 10, home_img, 1)
setting_btn = button.Button(80, 10, setting_img, 1)
undo_btn = button.Button(150, 10, undo_img, 1)
close_btn = button.Button(900, 10, close_img, 0.8)
next_btn = button.Button(900, 500, next_img, 0.8)
about_btn = button.Button(10, 545,about_img,1)

pic1 = button.Button(180, 140, picture1, 0.8)
#pic2 = button.Button(-80, 220, picture2, 0.4)

Sodo_btn = button.Button(80,140,sodo_img,0.8)
gr_father_btn = button.Button(540,100,gr_father_img, 0.45)
gr_mother_btn = button.Button(800,150,gr_mother_img, 0.45)
mother_btn = button.Button(90, 250, mother_img, 0.35)
father_btn = button.Button(750, 330, father_img, 0.40)
child_btn = button.Button(600, 400, child_img, 0.3)




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
    draw_text('COMPLETE THE FAMILY MAP', font2, (255,255,255), screen, 100, 100)
    # draw button 
    home_btn.draw(screen)
    setting_btn.draw(screen)
    undo_btn.draw(screen)
    next_btn.draw(screen)
    close_btn.draw(screen)
    about_btn.draw(screen)
    
    Sodo_btn.draw(screen)
    gr_father_btn.draw(screen)
    gr_mother_btn.draw(screen)
    mother_btn.draw(screen)
    father_btn.draw(screen)
    child_btn.draw(screen)
    # draw picture
    
    
    #event handler
    for event in pygame.event.get():
        #quit game 
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()
    
pygame.quit()