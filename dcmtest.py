# 1. dòng 20 để nhét ảnh cần kéo thả
# 2. dòng 21 để scale cho thằng 1.
# 3.  dòng 55 cụm size_x cho đến pos_y là vị trí cho vật tĩnh
# 4. dòng 65 để đặt ví trí ban đầu cho thằng 1.
# 5. dòng 107 để logic cho 2 thằng chạm nhau, bản chất là x, y của thằng 
# này nằm trong zone của x, y của thằng kia






import pygame
import random
import draw
import button

class Key(pygame.sprite.Sprite):
    def __init__(self, xpos, ypos, id):
        super(Key, self).__init__()
        self.your_img= pygame.image.load('images/Sodo/Father.png').convert_alpha()
        self.image=  pygame.transform.scale(self.your_img, (180, 180))
        self.clicked= False
        self.rect= self.image.get_rect()
        self.rect.y= ypos
        self.rect.x= xpos
        self.clicked= False
        self.id= id 
        self.linkReady= False
        self.links= []

class Key2(pygame.sprite.Sprite):
    def __init__(self, xpos, ypos, id):
        super(Key2, self).__init__()
        self.your_img= pygame.image.load('images/Sodo/GrMother.png').convert_alpha()
        self.image=  pygame.transform.scale(self.your_img, (150, 150))
        self.clicked= False
        self.rect= self.image.get_rect()
        self.rect.y= ypos
        self.rect.x= xpos
        self.clicked= False
        self.id= id 
        self.linkReady= False
        self.links= []

class Key3(pygame.sprite.Sprite):
    def __init__(self, xpos, ypos, id):
        super(Key3, self).__init__()
        self.your_img= pygame.image.load('images/Sodo/child_cut.png').convert_alpha()
        self.image=  pygame.transform.scale(self.your_img, (150, 150))
        self.clicked= False
        self.rect= self.image.get_rect()
        self.rect.y= ypos
        self.rect.x= xpos
        self.clicked= False
        self.id= id 
        self.linkReady= False
        self.links= []
Black= (0, 0, 0)
White= (255, 255,255)



pygame.init()

size= (1000, 600)
screen= pygame.display.set_mode(size)

pygame.display.set_caption("dcm")

done= False
clock= pygame.time.Clock()

key_list= pygame.sprite.Group()
key_list2= pygame.sprite.Group()
key_list3 = pygame.sprite.Group()


print1= False
print2= False
print3= False


#test_img = pygame.Surface((50, 50))
#test_img.fill(pygame.Color( 90,140,65))

#Vi Tri Father
size_x= 200
size_y= 200 
pos_x= 300
pos_y= 200

#Vi tri GrandMother
size_x2 = 200
size_y2 = 200 
pos_x2 = 400
pos_y2 = 300

#Vi tri Child
size_x3 = 150
size_y3 = 150 
pos_x3 = 300
pos_y3 = 450

#Key1
bag_img= pygame.image.load('images/Sunrise/sun_png.png').convert_alpha()

bag_rect= bag_img.get_rect(topleft= (pos_x, pos_y))

ok_img= pygame.image.load('images/Sunrise/sun_png.png').convert_alpha()

#Key2
bag_img2 = pygame.image.load('images/Sodo/GrMother.png').convert_alpha()

bag_rect2 = bag_img.get_rect(topleft= (pos_x3, pos_y3))

ok_img2 = pygame.image.load('images/Sodo/GrMother.png').convert_alpha()

#Key3
bag_img3 = pygame.image.load('images/Sodo/child_cut.png').convert_alpha()

bag_rect3 = bag_img.get_rect(topleft= (pos_x2, pos_y2))

ok_img3 = pygame.image.load('images/Sodo/child_cut.png').convert_alpha()


#add keylist 
#father 
key_list.add(Key(700, 250, len(key_list)+ 1))
#grand mother 
key_list2.add(Key2(600,400, len(key_list2)+ 1))
#child
key_list3.add(Key3(750,100, len(key_list3) +1))


#font 
font1 = pygame.font.SysFont("Segoe Script", 50)
font2 = pygame.font.SysFont("Arial", 50)


#load background
bg_image = pygame.image.load('images/Background/backgroundTN.jpg').convert_alpha()
picture1 = pygame.image.load('images/Freeze/nuocda.png').convert_alpha()
picture2 = pygame.image.load('images/Background/hoicham_1.png').convert_alpha()
picture3 = pygame.image.load('images/Background/hoicham_2.png').convert_alpha()
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
firework1_img = pygame.image.load('images/Firework/firework.png')
firework2_img = pygame.image.load('images/Firework/firework1.png')
check_img = pygame.image.load('images/Icon/checkmark.png')
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
check_btn = button.Button(760, 520, check_img,0.6)
pic1 = button.Button(180, 140, picture1, 0.8)
#pic2 = button.Button(-80, 220, picture2, 0.4)
pic3 = button.Button(-30, 350, picture3, 0.4)
compass = button.Button(400, 220, compass_image, 0.4)
sun_btn = button.Button(400, 420, sun_img, 0.3)
correct_btn =button.Button(-10, 200, correct_img, 0.5)
about_btn = button.Button(10, 545,about_img,1)
Sodo_btn = button.Button(80,140,sodo_img,0.8)
gr_father_btn = button.Button(540,100,gr_father_img, 0.45)
gr_mother_btn = button.Button(800,150,gr_mother_img, 0.45)
mother_btn = button.Button(90, 250, mother_img, 0.35)
father_btn = button.Button(750, 330, father_img, 0.40)
child_btn = button.Button(600, 400, child_img, 0.3)
firework1_btn = button.Button(200, 100, firework1_img, 0.5)
firework2_btn = button.Button(550, 100, firework2_img, 0.5)




#creat window menu - tạo cửa sổ menu
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1000


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


while not done:
    screen.fill((118,145,176))
    #draw background
    #draw_bg()  
    #draw_text('Lets study', font, (255,50,50), screen, 20, 20)
    # draw_text('BRAIN OUT', font, (255,50,50), screen, 380, 120)
    # if start_button.draw(screen):
    #     pass
    draw_text('COMPLETE THE FAMILY MAP', font2, (255,255,255), screen, 20, 80)
    # draw button 
    home_btn.draw(screen)
    setting_btn.draw(screen)
    undo_btn.draw(screen)
    next_btn.draw(screen)
    close_btn.draw(screen)
    #check_btn.draw(screen)
    # option1_btn.draw(screen)
    # option2_btn.draw(screen)
    # option3_btn.draw(screen)
    
    
    # draw picture
    #pic1.draw(screen)
    #pic2.draw(screen)
    #compass.draw(screen)
    #pic3.draw(screen)
    
    #sun_btn.draw(screen)
    about_btn.draw(screen)
    
    Sodo_btn.draw(screen)
    gr_father_btn.draw(screen)
    #gr_mother_btn.draw(screen)
    mother_btn.draw(screen)
    #father_btn.draw(screen)
    #child_btn.draw(screen)
    
    
    for event in pygame.event.get():
        if event.type== pygame.QUIT:
            done= True

        if event.type== pygame.MOUSEBUTTONDOWN:
            pos= pygame.mouse.get_pos()
            x= pos[0]
            y= pos[1]


            if event.button== 1:
                for key1 in key_list:
                    if key1.rect.collidepoint(pos):
                        key1.clicked= True
                        
                for key2 in key_list2:
                    if key2.rect.collidepoint(pos):
                        key2.clicked= True
                        
                for key3 in key_list3:
                    if key3.rect.collidepoint(pos):
                        key3.clicked= True


        if event.type== pygame.MOUSEBUTTONUP:
            for key1 in key_list:
                key1.clicked= False
                
            for key2 in key_list2:
                key2.clicked= False
            
            for key3 in key_list3:
                key3.clicked= False
                
            drag_id= 0 


    for key1 in key_list:
        if key1.clicked== True:
            pos= pygame.mouse.get_pos()
            key1.rect.x= pos[0]- (key1.rect.width/ 2)
            key1.rect.y= pos[1]- (key1.rect.height/ 2)
            
    for key2 in key_list2:
        if key2.clicked== True:
            pos= pygame.mouse.get_pos()
            key2.rect.x= pos[0]- (key2.rect.width/ 2)
            key2.rect.y= pos[1]- (key2.rect.height/ 2)
            
    for key3 in key_list3:
        if key3.clicked== True:
            pos= pygame.mouse.get_pos()
            key3.rect.x= pos[0]- (key3.rect.width/ 2)
            key3.rect.y= pos[1]- (key3.rect.height/ 2)

    #screen.fill(Black)
    
    key_list.draw(screen)
    key_list2.draw(screen)
    key_list3.draw(screen)
    
    # this is fucking size and fucking position

    #draw.draw_normally(bag_img, screen, size_x, size_y, pos_x, pos_y)

    #Vi tri dung cua Father
    for key1 in key_list: 
        if print1== False:
            if key1.rect.x > pos_x and key1.rect.x < pos_x+ size_x-100:
                print1= True
                break
    #Vi tri dung cua Grand Mother
    for key2 in key_list2: 
        if print2== False:
            if key2.rect.x > pos_x2 and key2.rect.x < pos_x2+ size_x2-100:
                print2= True
                break
    #Vi tri dung cua child 
    for key3 in key_list3: 
        if print3== False:
            if key3.rect.x > pos_x3 and key3.rect.x < pos_x3+ size_x3-100:
                print3= True
                break
    
    if print1== True and print2 == True and print3 == True: 
        #correct_btn.draw(screen)
        firework1_btn.draw(screen)
        #firework2_btn.draw(screen)
        




    # test rect of this fucking image
    # screen.blit(test_img, bag_rect)

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
