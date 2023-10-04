import pygame
from .constants import RED, WHITE, SQUARE_SIZE, GREY, CROWN
class Piece:
    PADDING = 17 # Padding between piece and edge of square
    OUTLINE = 2 # The outline/border

    # Initialize the object's (or checkers piece) attributes
    def __init__(self, row, col, color):
        # Instance variables
        self.row = row
        self.col = col
        self.color = color
        self.king = False
        # Store pieces' positions
        self.x = 0 
        self.y = 0
        # Call method
        self.calc_pos() 

    # Calculate x and y position based on the row and column the piece is located in
    def calc_pos(self):
        # Circular pieces are drawn from the center, therefore must be in middle of square on board
        self.x = SQUARE_SIZE * self.col + SQUARE_SIZE // 2 # x coordinate of center of square
        self.y = SQUARE_SIZE * self.row + SQUARE_SIZE // 2 # y coordinate of center of square

    # Marks a piece as a king piece when called
    def make_king(self):
        self.king = True
    
    # Draw pieces on window
    def draw(self, win):
        radius = SQUARE_SIZE // 2 - self.PADDING # Radius of circle
        pygame.draw.circle(win, GREY, (self.x, self.y), radius + self.OUTLINE) # Draw outline
        pygame.draw.circle(win, self.color, (self.x, self.y), radius) # Draw inner circle
        # Draw crown on king piece
        if self.king:
            # Calculations are done to make sure the crown is drawn at the middle, instead of starting at middle
            win.blit(CROWN, (self.x - CROWN.get_width() // 2, self.y - CROWN.get_height() // 2))

    # Move piece to new position
    def move(self, row, col):
        self.row = row
        self.col = col
        self.calc_pos()