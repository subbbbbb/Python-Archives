import pygame

pygame.init()

BLACK = (0,0,0)
WHITE = 255,255,255
FPS = 60
playing = True
WIDTH = 600
HEIGHT = 400
canvas = pygame.display.set_mode((WIDTH,HEIGHT))
clock = pygame.time.Clock()
x = 0

while playing is True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False
    canvas.fill(BLACK)
    clock.tick(FPS)
    pygame.draw.rect(canvas,WHITE,[x,200,80,40])
    pygame.display.update()
    x = x+1
pygame.quit() 