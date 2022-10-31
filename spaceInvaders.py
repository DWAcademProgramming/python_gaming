import pygame

#Initialize pygame
pygame.init()

#Create a dispaly surface and set its condition 
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 300
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Space Invaders")

# The main game loop
running = True
while running: 
    #Loop through a list of Event Objects that have occured
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT: 
            running = False 

#End the game
pygame.quit()