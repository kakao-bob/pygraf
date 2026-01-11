# import tkinter
import math
import pygraf as pf

pf.screen_conf("Example", 1200, 700, False)
pf.draw_coord(200, sep_step=1, sep_size=0.2)


pf.y_plot("y = math.cos(x) ").draw("red")
pf.y_plot("y = math.sin(x) ").draw("blue")
pf.y_plot("y = (x+5)**0.5 - 7", x_from=-5, x_to=100).draw("black")

l = [5,4,3,4,3,4,5]
pf.list_plot(l, start_x=-3).draw("green")

pf.zoom(1) # приблизить картинку


pf.screen_save()