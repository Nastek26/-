import pygame

pygame.init()
clock = pygame.time.Clock()
FPS = 60

app = pygame.display.set_mode((400, 400), 0, 32)

game_on = True
while game_on:
    clock.tick(FPS)
    # event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_on = False
    # update


    # render
    app.fill((0, 0, 0))
    pygame.display.flip()

pygame.quit()