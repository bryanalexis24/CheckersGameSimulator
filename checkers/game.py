"""
Responsible for handling the logic of the game
1. Who's turn
2. Valid jump movement
3. Etc.
"""
import pygame
from .board import Board
from .constants import RED, WHITE, BLUE, SQUARE_SIZE
class Game:
    # Intance variables 
    def _init(self):
        self.selected = None
        self.board = Board()
        self.turn = RED
        self.valid_moves = {}

    # Initialize the game
    def __init__(self, win):
        self._init()
        self.win = win

    # Update pygame display
    def update(self):
        self.board.draw(self.win)
        self.draw_valid_moves(self.valid_moves) ##### Might have to import ####################
        pygame.display.update()

    # Reset game, instead of calling _init
    def reset(self):
        self._init()

    # Handles what happens when piece is selected
    def select(self, row, col):
        # If piece is selected, move to another row and column
        if self.selected:
            result = self._move(row, col)
            # If non valid move
            if not result:
                self.selected = None # Reset selection
                self.select(row, col) # Reselect another piece
        piece = self.board.get_piece(row, col)
        # If a non-empty piece is selected
        if piece != 0 and piece.color == self.turn:
            self.selected = piece
            self.valid_moves = self.board.get_valid_moves(piece)
            return True # Return true if selection was valid
        return False # Return false if not valid
    
    # Move piece
    def _move(self, row, col):
        piece = self.board.get_piece(row, col)
        # Can only move piece if empty space is selected after first non-empty space (piece) is selected
        if self.selected and piece == 0 and (row, col) in self.valid_moves:
            self.board.move(self.selected, row, col) # Move currently selected piece to row and column
            skipped = self.valid_moves[(row, col)]
            if skipped:
                self.board.remove(skipped)
            self.change_turn() # Change the turn
        else:
            return False
        return True
    
    # Change the turn
    def change_turn(self):
        self.valid_moves = {}
        if self.turn == RED:
            self.turn = WHITE
        else:
            self.turn = RED

    # Draw squares for all valid moves
    def draw_valid_moves(self, moves):
        for move in moves:
            row, col = move
            pygame.draw.circle(self.win, BLUE, (col * SQUARE_SIZE + SQUARE_SIZE // 2, row * SQUARE_SIZE + SQUARE_SIZE // 2), 15)