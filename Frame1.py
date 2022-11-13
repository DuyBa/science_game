import pygame
import draw

def runtest(run_of_manf, supertotal):



    SCREEN_WIDTH = 1000
    SCREEN_HEIGHT = 600

    #BLACK = (  0,   0,   0)
    WHITE = (255, 255, 255)
    RED   = (255,   0,   0)

    FPS = 30

    # --- classses --- (CamelCase names)

    # empty

    # --- functions --- (lower_case names)

    # empty

    # --- main ---

    # - init -

    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    #screen_rect = screen.get_rect()

    pygame.display.set_caption("Tracking System")

    # - objects -

    # ảnh nấm

    rectangle= pygame.image.load('frames/frame1/namdoc1.jpg').convert_alpha()

    # rectangle = pygame.rect.Rect(176, 134, 17, 17)
    rectangle_draging = False

    rectanglee= pygame.rect.Rect(300, 200, 17, 17)

    # - mainloop -

    clock = pygame.time.Clock()
    

    while run_of_manf[1]:

        # - events -

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run_of_manf[1]= supertotal[0]= False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:            
                    if rectangle.colliderect(event.pos):
                        rectangle_draging = True
                        mouse_x, mouse_y = event.pos
                        offset_x = rectangle.x - mouse_x
                        offset_y = rectangle.y - mouse_y

            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:            
                    rectangle_draging = False

            elif event.type == pygame.MOUSEMOTION:
                if rectangle_draging:
                    mouse_x, mouse_y = event.pos
                    rectangle.x = mouse_x + offset_x
                    rectangle.y = mouse_y + offset_y

        # - updates (without draws) -

        # empty

        # - draws (without updates) -

        screen.fill(WHITE)

        draw.draw_normally(rectangle, screen, 200, 200, 300, 60)
        
        pygame.display.flip()

        # - constant game speed / FPS -

        clock.tick(FPS)

    # - end -
