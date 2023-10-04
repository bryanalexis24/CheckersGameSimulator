import pygame
from checkers.constants import WIDTH, HEIGHT, SQUARE_SIZE, RED
from checkers.game import Game

"""
1. Set up a pygame display
2. Set up a basic event loops
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

# Take the position of mouse and indicate what row/column mouse is in
def get_row_col_from_mouse(pos):
    x, y = pos # x and y positions of mouse
    row = y // SQUARE_SIZE # Indicate row mouse is positioned in
    col = x // SQUARE_SIZE # Indicate column mouse is positioned in
    return row, col

# Main function that will run the game
def main():
    run =  True
    # Have the game run at a constant frame rate
    clock = pygame.time.Clock()
    # Make game object
    game = Game(WIN)
    # Event loop that will run every x times per second to make checks/update display
    while run:
        clock.tick(FPS)
        # Check if any events have occurred within current time
        for event in pygame.event.get():
            # Check if event is specific type
            if event.type == pygame.QUIT: # Event example
                run = False # Ends loop
            if event.type == pygame.MOUSEBUTTONDOWN: # Checks if mouse is pressed
                # Call methods to move piece
                pos = pygame.mouse.get_pos()
                row, col = get_row_col_from_mouse(pos)
                game.select(row, col)
        game.update() # Update game
    pygame.quit() # Closes window
main() # Call to function
