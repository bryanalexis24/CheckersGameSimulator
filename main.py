import pygame
from checkers.constants import WIDTH, HEIGHT
"""
1. Set up a pygame display
2. Set up a basic event loop
    Ex. Check if mouse was clicked
3. Set up basic drawings
    a. Draw board
    b. Draw pieces
4. Set up logic of game and piece movements
"""
# All caps because it's a constant value
WIN = pygame.display.set_mode((WIDTH, HEIGHT)) # Define both variables in constants file
