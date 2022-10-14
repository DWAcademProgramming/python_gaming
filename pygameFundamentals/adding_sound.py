import pygame 

#Initialize Pygame
pygame.init()

#Create a display surface and set its caption
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 300
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Adding Sound")

#Load sound effects
sound_1 = pygame.mixer.Sound('sound_1.wav')
sound_2 = pygame.mixer.Sound('sound_2.wav')

#Play the sound effects
sound_1.play()
pygame.time.delay(2000)
sound_2.play()

#Change the volume of the sound effect
sound_2.set_volume(.1)

#Load background music and play/stop it
pygame.mixer.music.load('music.wav')
pygame.mixer.music.play(-1, 0.0)
pygame.time.delay(5000)
pygame.mixer.music.stop()

#The main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

#End the game
pygame.quit()