import pygame
import random

pygame.init()


screen = pygame.display.set_mode((800,600))

bg_image = pygame.image.load('bg.JPG')

player1 = pygame.Rect(50, 50, 30, 30)
player1_color = (255,0,0)
grid_size = 7
cell_size = 50  
grid_origin = (100, 50)  

def movePlayer(player, roll):
    player.move_ip(roll*5, 0)


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
        # Check for a key press to roll the dice
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:  # Press space to roll the dice
                roll = random.randint(1, 6)
                movePlayer(player1, roll)
    
    # Clear screen
    screen.fill((255, 255, 255))

    for row in range(grid_size):
        for col in range(grid_size):
            rect = pygame.Rect(
                grid_origin[0] + col * cell_size,  # x position
                grid_origin[1] + row * cell_size,  # y position
                cell_size,                        # width
                cell_size                         # height
            )
            pygame.draw.rect(screen, (255,255,255), rect, 1)  
    
    
    # Draw player
    pygame.draw.rect(screen, player1_color, player1)
    
    # Update display
    pygame.display.flip()

# Quit Pygame
pygame.quit()