import pygame
from .constants import BLACK, RED, ROWS, SQUARE_SIZE
"""
Represents the checkers board
Will handle: 
1. Moving specific pieces
2. Deleting specific pieces
3. Drawing itself onto the screen
"""

class Board: 
    def __init__(self):
        self.board = [] # Internal representation of board (2D array)
        self.selected_piece = None # Keep track of currently selected piece
        self.red_left = self.white_left = 12 # Number of red and white pieces at start
        self.red_kings = self.white_kings = 0 # Number of red & white king pieces at start

    # Will draw red and black squares in checkerboard pattern on the window
    def draw_squares(self, win):
        win.fill(BLACK) # Fills the entire window in black
        for row in range(ROWS):
            for col in range(row % 2, ROWS, 2): # Start in every other column to draw red square on top of window
                pygame.draw.rect(win, RED, (row * SQUARE_SIZE, col * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE)) # Draw red square
                        