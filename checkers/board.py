import pygame
from .constants import BLACK, RED, ROWS, SQUARE_SIZE, COLS, WHITE
from .piece import Piece
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
        self.red_left = self.white_left = 12 # Number of red and white pieces at start
        self.red_kings = self.white_kings = 0 # Number of red & white king pieces at start
        self.design_board() # Creates the board

    # Will draw red and black squares in checkerboard pattern on the window
    def draw_squares(self, win):
        win.fill(BLACK) # Fills the entire window in black
        for row in range(ROWS):
            for col in range(row % 2, ROWS, 2): # Start in every other column to draw red square on top of window
                pygame.draw.rect(win, RED, (row * SQUARE_SIZE, col * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE)) # Draw red square

    # Delete piece from where it is and move to new position
    def move(self, piece, row, col):
        # Swap the values of the piece that will be moved, and the empty piece that is the position desired
        self.board[piece.row][piece.col], self.board[row][col] = self.board[row][col], self.board[piece.row][piece.col]
        # Move the piece
        piece.move(row, col)
        # Check if row, col that we move to is a position where piece should become king
        if row == ROWS - 1 or row == 0: # Remove - 1 if not working
            piece.make_king()
            if piece.color == WHITE:
                self.white_kings += 1
            else:
                self.red_kings += 1

    # Give board object row and col, and it'll give you a piece in return
    def get_piece(self, row, col):
        return self.board[row][col]
    
    # Design the internal representation of the board, and add pieces
    # White pieces at top, red at bottom
    def design_board(self):
        for row in range(ROWS):
            self.board.append([]) # List that represents what each row will have inside
            for col in range(COLS):
                # Draw piece in every other column, alternating per row
                if col % 2 == ((row + 1) % 2):
                    # Draw white pieces in first 3 rows
                    if row < 3:
                        self.board[row].append(Piece(row, col, WHITE))
                    # Draw red pieces in last 3 rows
                    elif row > 4:
                        self.board[row].append(Piece(row, col, RED))
                    # Blank piece
                    else:
                        self.board[row].append(0) 
                # If we don't add a piece, add 0 to separate and keep track of where pieces are
                else:
                    self.board[row].append(0)
    # Draw each piece on non 0 spaces
    def draw(self, win):
        self.draw_squares(win) # Call method here so that it doesn't have to be called again in main class
        for row in range(ROWS):
            for col in range(COLS):
                piece = self.board[row][col]
                if piece != 0:
                    piece.draw(win)
                    
    # Remove pieces after they're jumped over
    def remove(self, pieces):
        for piece in pieces:
            self.board[piece.row][piece.col] = 0

    # Gets valid potential moves
    def get_valid_moves(self, piece):
        moves = {} # Store potential moves
        left = piece.col - 1 
        right = piece.col + 1
        row = piece.row

        # Valid moves
        if piece.color == RED or piece.king:
            moves.update(self._traverse_left(row - 1, max(row - 3, -1), -1, piece.color, left))
            moves.update(self._traverse_right(row - 1, max(row - 3, -1), -1, piece.color, right))
        if piece.color == WHITE or piece.king:
            moves.update(self._traverse_left(row + 1, min(row + 3, ROWS), 1, piece.color, left))
            moves.update(self._traverse_right(row + 1, min(row + 3, ROWS), 1, piece.color, right))
        return moves

    # Look at left diagonal
    def _traverse_left(self, start, stop, step, color, left, skipped = []):
        moves = {}
        last = [] # Pieces that would be skipped to move to desired square
        for r in range(start, stop, step):
            # If potential move is outside of board, stop
            if left < 0:
                break
            current = self.board[r][left]
            # Found empty square
            if current == 0:
                # If a piece was jumped over and there isn't another piece that can be skipped, can't move to square
                if skipped and not last:
                    break
                # Double jump, combine last skipped with next skipped piece
                elif skipped:
                    moves[(r, left)] = last + skipped
                else:
                    moves[(r, left)] = last # Add as possible move
                # Have piece jumped over, check if double jump is possible
                if last:
                    # Check which direction piece will be moved
                    if step == -1:
                        row = max(r - 3, 0)
                    else:
                        row = min(r + 3, ROWS)
                    # Call recursively to see double jump
                    moves.update(self._traverse_left(r + step, row, step, color, left - 1, skipped = last))
                    moves.update(self._traverse_right(r + step, row, step, color, left + 1, skipped = last))
                break
            # Same pieces can't be jumped over
            elif current.color == color:
                break
            # If other color, store in potential skip moves
            else:
                last = [current]
            left -= 1
        return moves

    # Look at right diagonal
    def _traverse_right(self, start, stop, step, color, right, skipped = []):
        moves = {}
        last = [] # Pieces that would be skipped to move to desired square
        for r in range(start, stop, step):
            # If potential move is outside of board, stop
            if right >= COLS:
                break
            current = self.board[r][right]
            # Found empty square
            if current == 0:
                # If a piece was jumped over and there isn't another piece that can be skipped, can't move to square
                if skipped and not last:
                    break
                # Double jump, combine last skipped with next skipped piece
                elif skipped:
                    moves[(r, right)] = last + skipped
                else:
                    moves[(r, right)] = last # Add as possible move
                # Have piece jumped over, check if double jump is possible
                if last:
                    # Check which direction piece will be moved
                    if step == -1:
                        row = max(r - 3, 0)
                    else:
                        row = min(r + 3, ROWS)
                    # Call recursively to see double jump
                    moves.update(self._traverse_left(r + step, row, step, color, right - 1, skipped = last))
                    moves.update(self._traverse_right(r + step, row, step, color, right + 1, skipped = last))
                break
            # Same pieces can't be jumped over
            elif current.color == color:
                break
            # If other color, store in potential skip moves
            else:
                last = [current]
            right += 1
        return moves