import sys, pygame
pygame.init()

size = width, height = 320, 240
speed = [2, 2]
black = 0, 0, 0
white = (255,)*3

screen = pygame.display.set_mode(size)

ball = pygame.draw.circle(screen,white,[50,50],5)
ballrect = pygame.draw.rect(screen,white,[50,50,50,50])

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    ballrect = ballrect.move(speed)
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]

    screen.fill(black)
    pygame.display.flip()