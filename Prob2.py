########################################
# Name: Quinn Varnell
# Collaborators: Abygale Brien
# Estimated time spent (hrs): 1.5
########################################

from pgl import GWindow, GRect

WIDTH = 800
HEIGHT = 600
BRICK_WIDTH = 40
BRICK_HEIGHT = 20
BRICKS_IN_BASE = 15

def draw_pyramid():
    """ 
    Draws a pyramid of bricks centered on the screen with a height of BRICKS_IN_BASE. 
    """

    gw = GWindow(WIDTH, HEIGHT)

    # You got it from here

    # Finds the center of the Graphics Window
    center_x = WIDTH // 2
    center_y = HEIGHT // 2

    # Finds the start of the bottom row.
    bottom_row_y = center_y + (BRICK_HEIGHT * (BRICKS_IN_BASE // 2))

    for row in range(BRICKS_IN_BASE):
        num_bricks = BRICKS_IN_BASE - row  # amount of bricks in current row
        row_y = bottom_row_y - (row * BRICK_HEIGHT)

        total_row_width = num_bricks * BRICK_WIDTH
        row_start_x = center_x - (total_row_width // 2)

        for brick in range(num_bricks):
            brick_rect = GRect(row_start_x + (brick * BRICK_WIDTH), row_y, BRICK_WIDTH, BRICK_HEIGHT)
            gw.add(brick_rect)

if __name__ == '__main__':
    draw_pyramid()
