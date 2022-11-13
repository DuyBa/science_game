import pygame

def runtest(run_of_manf, WHITE, supertotal, rectangle, rectangle_draging, screen, RED, clock, FPS):
    

    while run_of_manf[1]:

        # - events -

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run_of_manf[1]= supertotal[0]= False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:            
                    if rectangle.collidepoint(event.pos):
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

        pygame.draw.rect(screen, RED, rectangle)
        
        pygame.display.flip()

        # - constant game speed / FPS -

        clock.tick(FPS)

    # - end -
