from tkinter import *

root = Tk()

width_of_window = 500
height_of_window = 500

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x = (screen_width/2) - (width_of_window/2)
y = (screen_height/2) - (height_of_window/2)

root.geometry("%dx%d+%d+%d" % (width_of_window, height_of_window, x, y))

mainloop()

