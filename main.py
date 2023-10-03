import pygame
from checkers.constants import WIDTH, HEIGHT
from checkers.board import Board

"""
1. Set up a pygame display
2. Set up a basic event loop
    Ex. Check if mouse was clicked
3. Set up basic drawings
    a. Draw board
    b. Draw pieces
4. Set up logic of game and piece movements
"""
# Constants folder is specific to checkers game, FPS & WIN are specific to rendering and drawing game
FPS = 60 # Frame rate for game

WIN = pygame.display.set_mode((WIDTH, HEIGHT)) # Define both variables in constants file
pygame.display.set_caption('Checkers Game') # Name displayed at top of window when opened

# Main function that will run the game
def main():
    run =  True
    # Have the game run at a constant frame rate
    clock = pygame.time.Clock()
    # Make board object
    board = Board()

    piece = board.get_piece(0, 1) # Test
    board.move(piece, 4, 3) # Test

    # Event loop that will run every x times per second to make checks/update display
    while run:
        clock.tick(FPS)
        # Check if any events have occurred within current time
        for event in pygame.event.get():
            # Check if event is specific type
            if event.type == pygame.QUIT: # Event example
                run = False # Ends loop

            if event.type == pygame.MOUSEBUTTONDOWN: # Checks if mouse is pressed
                pass
        board.draw(WIN) # Draw square at end of each loop
        pygame.display.update() # Update the display in pygame
    pygame.quit() # Closes window

main() # Call to function
