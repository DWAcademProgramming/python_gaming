from curses import KEY_LEFT
import pygame

#Initialize pygame
pygame.init()

#Create a dispaly surface and set its condition 
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 300
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Discrete Movement!")

#Setting the game values
VELOCITY = 10

#Load in the images
dragon_image = pygame.image.load("dragon_right.png")
dragon_rect = dragon_image.get_rect()
dragon_rect.centerx = WINDOW_WIDTH//2
dragon_rect.bottom = WINDOW_HEIGHT

# The main game loop
running = True
while running: 
    #Loop through a list of Event Objects that have occured
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT: 
            running = False 
        #Check for discrete movement
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.KEY_LEFT:
                dragon_rect.x -= VELOCITY
            if event.key == pygame.KEY_RIGHT:
                dragon_rect.x += VELOCITY
            if event.key == pygame.KEY_DOWN:
                dragon_rect.x += VELOCITY
            if event.key == pygame.KEY_Up:
                dragon_rect.x -= VELOCITY
    
    #Fill the display surface to cover old images
    display_surface.blit(dragon_image, dragon_rect)
    
    #Blit assets onto the screen
    display_surface.blit(dragon_image, dragon_rect)

    #Update the display
    pygame.display.update()

#End the game
pygame.quit()