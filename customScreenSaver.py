import pygame  

# This section is just defining some colors for later use, hello world
BLACK = (0,0,0)
WHITE = (255,255,255)
GREEN = (0,255,0)
RED = (255, 0, 0)

# This initializes the pygame library for later use
pygame.init()

# SCREEN SECTION !!!! This area defines a window that we can operate our game out of
size = (1920,1030) # The resolution takes in two arguments, here we are setting the size variable to hold two values which correspond to screen size detailed below...
screen = pygame.display.set_mode(size)# <--takes in our arguments to display a new window with the matching size


pygame.display.set_caption("Screensaver")

# Loops until the player clicks the close button
done = False

# Manages how fast the screen updates
clock = pygame.time.Clock()

#PRACTICE CODE
#starting position of a rectangle
rect_x = 50
rect_y = 50

#speed and direction
rect_change_x = 5
rect_change_y = 5

#font to draw text on the screen
font = pygame.font.Font(None, 36)

#boolean to trigger if the game is over
game_over = False

# The following is our Main Program Loop
while not done:
    # Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        #can spell out other game over scenarios in this area, like lives == 0
        elif event.type == pygame.MOUSEBUTTONDOWN:
            game_over = True

    # Game Logic goes here.....
    if not game_over:
        #this will move the rectangles starting point
        rect_x += rect_change_x
        rect_y += rect_change_y

        #bounce the ball if needed
        if rect_y > 950 or rect_y < 0:
            rect_change_y = rect_change_y * -1
        if rect_x > 1870 or rect_x < 0:
            rect_change_x = rect_change_x * -1
    
    #Screen clearing goes here.....
    screen.fill(BLACK)

    #draw the rectangle
    pygame.draw.rect(screen, GREEN, [rect_x, rect_y, 50, 50])

    if game_over:
        #if the game is over, this will draw out text based on the font we set earlier
        text = font.render("Game Over", True, WHITE)
        text_rect = text.get_rect()
        text_x = screen.get_width() / 2 - text_rect.width / 2
        text_y = screen.get_height() / 2 - text_rect.height / 2
        screen.blit(text, [text_x, text_y])
    else:
        # if the game isn't over yet, draw this stuff
        text = font.render(". . . lost in space . . .", True, WHITE)
        text_rect = text.get_rect()
        text_x = screen.get_width() / 2 - text_rect.width / 2
        text_y = screen.get_height() / 2 - text_rect.height / 2
        screen.blit(text, [text_x, text_y])

    #Update the screen to reflect what you've drawn to it
    pygame.display.flip()

    #This will limit our screen to an FPS
    clock.tick(60)
#Close the window and quit the program
pygame.quit()