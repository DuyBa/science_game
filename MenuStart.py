import pygame
import button
pygame.init()

#creat window menu - tạo cửa sổ menu
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1000

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Main Menu")

#font 
font = pygame.font.SysFont("Segoe Script", 50)

#load background
bg_image = pygame.image.load('images/Background/menu_background.jpg').convert_alpha()

#load button imgs
start_img = pygame.image.load("images/Icon/start_btn.png").convert_alpha()


#load img
main_img = pygame.image.load("images/Icon/brain_400.png").convert_alpha()


#create button instances
start_button = button.Button(470, 400, start_img, 1)
main_button = button.Button(400, 180, main_img, 0.6 )


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
    #screen.fill((202,228,241))
    #draw background
    draw_bg()  
    #draw_text('Lets study', font, (255,50,50), screen, 20, 20)
    draw_text('BRAIN OUT', font, (255,50,50), screen, 380, 120)
    if start_button.draw(screen):
        pass
    
    main_button.draw(screen)
    
    #event handler
    for event in pygame.event.get():
        #quit game 
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()
    
pygame.quit()