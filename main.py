# Pygame game template

import pygame
import sys
import config # Import the config module

def init_game():
    pygame.init()
    screen = pygame.display.set_mode((config.WINDOW_WIDTH, config.WINDOW_HEIGHT)) # Use constants from config
    pygame.display.set_caption(config.TITLE)
    return screen

def handle_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                return False
    return True

def main():
    screen = init_game()
    clock = pygame.time.Clock() # Initalize the clock here
    running = True
    while running:
        running = handle_events()
        screen.fill(config.GREEN) # Use color from config

        thickness = 5
        for y_offset in range(0, 800, 20):
            pygame.draw.line(screen, config.WHITE, [0, 0 + y_offset], [800,0  + y_offset], thickness)

        y_offset = 0
        thickness = 5
        while y_offset < 800:
            pygame.draw.line(screen, config.BLUE, [0,5  + y_offset], [800, 5 + y_offset], thickness)
            y_offset = y_offset + 10

        
        for x_offset in range(0, 800, 20):
            thickness = 5
            pygame.draw.line(screen, config.RED, [0 + x_offset, 0 ], [0 + x_offset, 650], thickness)

        pygame.display.flip() # Limit the frame rate to the specified frames per second
        clock.tick(config.FPS) # Use the clock to control the frame rate
    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main()



