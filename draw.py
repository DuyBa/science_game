import pygame




def draw_text(text, font, color, surface, x, y):
	textobj= font.render(text, 1, color)
	textrect= textobj.get_rect()
	textrect.topleft= (x, y)
	surface.blit(textobj, textrect)


def draw_bg(your_bg, screen1, x, y):
	#vi bg cua chung ta ko fit size nen chung ta se resize lai, ok
	scaled_bg= pygame.transform.scale(your_bg, (x, y))
	screen1.blit(scaled_bg, (0, 0))


def draw_normally(your_img, screen1, x, y, pos_x, pos_y):

	scaled_img= pygame.transform.scale(your_img, (x, y))
	screen1.blit(scaled_img, (pos_x, pos_y))