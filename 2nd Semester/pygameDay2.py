import pygame
pygame.init()
canvas = pygame.display.set_mode((400,600))
done = False
xloc=0
clock=pygame.time.Clock()
while done == False:
    for event in pygame.event.get():
        if event == pygame.QUIT:
            done = True
        pygame.draw.rect(canvas,(25,55,110),(100,200,50,80))
        pygame.display.update()
        xloc=xloc+1
        clock.tick(60)
pygame.quit()