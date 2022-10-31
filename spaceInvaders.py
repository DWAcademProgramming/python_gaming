import pygame, random

#Initialize pygame
pygame.init()

#Create a dispaly surface and set its condition 
WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 700
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Space Invaders")

#Set FPS and clock
FPS = 60
clock = pygame.time.Clock()

#Define Classes
class Game():
    def __init__(self):
        """Initialize the game"""
        pass

    def update(self): 
        """Update the game"""
        pass
    def draw(self): 
        """Draw the HUD and other information to display"""
        pass

    def shift_aliens(self):
        """Shift the direction of the aliens"""
        pass

    def check_collisions(self): 
        """Check for collisions"""
        pass

    def check_round_completion(self):
        """Check to see if a player has completed a round"""
        pass 

    def start_new_round(self):
        """Start a new round"""
        pass

    def check_game_status(self):
        """Check to see th status of the game"""
        pass

    def pause_game(self):
        """Pauses the game"""
        pass

    def reset_game(self):
        """Reset the game"""
        pass

class Player(pygame.sprite.Sprite):
    def __init__(self):
        """initialize the player"""
        pass 

    def update(self): 
        """Update the player"""
        pass

    def fire(self):
        """Fire a bullet"""
        pass 

    def reset(self):
        """Reset the player's position"""
        pass

class Alien(pygame.sprite.Sprite):
    def __init__(self):
        """initialize the alien"""
        pass 

    def update(self): 
        """Update the alien"""
        pass

    def fire(self):
        """Fire a bullet"""
        pass 

    def reset(self):
        """Reset the alien's position"""
        pass

class PlayerBullet(pygame.sprite.Sprite): 
    """A class to model a bullet fired by the player"""

    def __init___(self):
        """Init the bullet"""
        pass

    def Self update(self): 
        """Update the bullet"""
        pass

class AlienBullet(pygame.sprite.Sprite): 
    """A class to model a bullet fired by the player"""

    def __init___(self):
        """Init the bullet"""
        pass

    def update(self): 
        """Update the bullet"""
        pass

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