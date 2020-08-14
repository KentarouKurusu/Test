import pygame

pygame.init()

display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('A bit Racey')

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
car_width = 73

clock = pygame.time.Clock()
carImg = pygame.image.load('racecar.png')

def car(x,y):
    gameDisplay.blit(carImg, (x,y))

def game_loop():
    x =  int(display_width * 0.45)
    y = int(display_height * 0.8)
    x_change = 0
    gameExit = False

    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            #print(event)
            ############################
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    if x > 5:
                        x_change = -5
                elif event.key == pygame.K_RIGHT:
                    if x < display_width - car_width - 5:
                        x_change = 5
            ######################

        if x < 5 and x_change < 0:
            x_change = 0
        elif x > display_width - car_width - 5 and x_change > 0:
            x_change = 0

        x += int(x_change)
        
        gameDisplay.fill(white)
        car(x,y)

        # if x > display_width - car_width or x < 0:
        #     gameExit = True    

        pygame.display.update()
        clock.tick(60)

game_loop()
pygame.quit()
quit()