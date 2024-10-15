############################################################
# Name: Quinn Varnell
# Name(s) of anyone worked with: N/A
# Est time spent (hr): 2
############################################################

from pgl import GWindow, GRect, GOval, GLine, GLabel

# Setting up initial window dimensions. 
# You can change these if you want. They are in number of pixels.
GW_WIDTH = 600
GW_HEIGHT = GW_WIDTH
RADIUS_L = 0.4 * GW_WIDTH
RADIUS_M = 0.25 * RADIUS_L
RADIUS_S = 0.25 * RADIUS_M

def draw_image():
    """ Creates a window and draws a student's creation"""

    # Creating the window
    gw = GWindow(GW_WIDTH, GW_HEIGHT)
    
    # And now it is your turn! Add your code below! Make sure you meet all the requirements!

    p_rect = GRect(150, 100, 200, 400)
    gw.add(p_rect)
    p_rect.set_filled(True)
    p_rect.set_color('purple')

    g_rect = GRect(350, 100, 100, 400)
    gw.add(g_rect)
    g_rect.set_filled(True)
    g_rect.set_color('dark_green')

    gs_rect = GRect(150, 371, 200, 129) #
    gw.add(gs_rect)
    gs_rect.set_filled(True)
    gs_rect.set_color('dark_green')

    ps_rect = GRect(350, 371, 100, 129)
    gw.add(ps_rect)
    ps_rect.set_filled(True)
    ps_rect.set_color('purple')
    
    p_circle = GOval(2*RADIUS_M, 2*RADIUS_M)
    gw.add(p_circle)
    p_circle.set_location(290, 250)
    p_circle.set_filled(True)
    p_circle.set_color('purple')

    g_circle_a = GOval(4*RADIUS_M, 2.52*RADIUS_M)
    gw.add(g_circle_a)
    g_circle_a.set_location(200, 100)
    g_circle_a.set_filled(True)
    g_circle_a.set_color('dark_green')
    
    sg_rect = GRect(300, 100, 100, 100)
    gw.add(sg_rect)
    sg_rect.set_filled(True)
    sg_rect.set_color('dark_green')
    
    gr_rect = GRect(150, 371, 300, 67)
    gw.add(gr_rect)
    gr_rect.set_filled(True)
    gr_rect.set_color('brown')

    line = GLine(150, 100, 450, 500)
    gw.add(line)
    line.set_color('red')

    line_b = GLine(150, 500, 450, 100)
    gw.add(line_b)
    line_b.set_color('red')

    gw.add(GLabel('Nope', 285, 400))
    

if __name__ == '__main__':
    draw_image()
