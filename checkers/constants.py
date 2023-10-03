import pygame
"""
If any values must be changed, all variables can be tracked here and easily be changed,
preventing potential bugs
"""
import pygame
# Names of constants are typically all capitalized
WIDTH, HEIGHT = 800, 800 # Dimensions in pixels of the game's window
ROWS, COLS = 8, 8 # Number of rows and columns checkers board will have
SQUARE_SIZE = WIDTH//COLS # The size of one square on the checker board

# RGB, colors will be used on the checkerboard display
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREY = (128, 128, 128)
