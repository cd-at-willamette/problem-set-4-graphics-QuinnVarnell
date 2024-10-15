########################################
# Name: Quinn Varnell
# Collaborators: Abygale Brien
# Estimate time spent (hrs): 1
########################################

from pgl import GWindow, GRect, GLabel, GLine
import random

GW_WIDTH = 500                      # Width of window
GW_HEIGHT = 500                     # Height of window
SQUARE_SIZE = 50                    # Width and height of square
SCORE_DX = 10                       # Distance from left of window to origin
SCORE_DY = 10                       # Distance up from bottom of window to baseline
SCORE_FONT = "bold 40pt 'serif'"    # Font for score

def clicky_box():

    # Defining the callback function, which you won't need until Part C
    def on_mouse_down(event):
        x = event.get_x()
        y = event.get_y()
        if gw.get_element_at(x, y) != None: #if there is something at the x and y coordinate, do if statement.
            n_x = random.randint(0, GW_WIDTH - SQUARE_SIZE)
            n_y = random.randint(0, GW_HEIGHT - SQUARE_SIZE)
            rect.set_location(n_x, n_y)
            points = int(score.get_label())
            points += 1
            score.set_label(str(points))
        else:
            points = 0
            score.set_label(str(points))

    # Down here you should initialize the window and draw the initial square
    # Make sure you tab it in so that it is part of the clicky_box function

    gw = GWindow(GW_WIDTH, GW_HEIGHT)

    rect = GRect(GW_WIDTH/2 - SQUARE_SIZE/2, GW_HEIGHT/2 - SQUARE_SIZE/2, SQUARE_SIZE, SQUARE_SIZE)
    gw.add(rect)
    rect.set_filled(True)
    rect.set_color('dark_green')

    gw.add_event_listener("mousedown", on_mouse_down)

    score = GLabel('0', SCORE_DX, GW_HEIGHT - 10)
    gw.add(score)
    score.set_font(SCORE_FONT)










if __name__ == '__main__':
    clicky_box()
