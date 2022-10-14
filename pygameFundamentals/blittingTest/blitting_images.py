import pygame 

#Initialize Pygame
pygame.init()

#Create a display surface and set its caption
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 500
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Blitting Images")

#Create images returning the surface object with the iamge drawn on it
#We can then get the rect of the surface and use the rect to position the image
dragon_left_image = pygame.image.load("C:\Users\David\python_gaming\pygameFundamentals\blittingTest\dragon_left.png")
dragon_left_rect = dragon_left_image.get_rect()
dragon_left_rect.topleft(0,0)

dragon_right_image = pygame.image.load("C:\Users\David\python_gaming\pygameFundamentals\blittingTest\dragon_right.png")
dragon_right_rect = dragon_right_image.get_rect()
dragon_right_rect.topright(WINDOW_WIDTH,0)

#The main game loop
running = True
while running: 
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            running = False
    #Blitting the surface objects
    display_surface.blit(dragon_left_image, dragon_left_rect)
    display_surface.blit(dragon_right_image, dragon_right_rect)
    #Update the display
    pygame.display.update()
#End the game
pygame.quit()