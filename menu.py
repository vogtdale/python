from tkinter import *
from tkFileDialog import askopenfilename

root = Tk()

menubar = Menu(root)

def FileNew():
    print "New file"

def OpenFile():
    name = askopenfilename()
    print name


# create pull down menus and add it to menubar

filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="New", command=FileNew)
filemenu.add_command(label="Open...", command=OpenFile)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)

menubar.add_cascade(label="File", menu=filemenu)

# display menubar 
root.config(menu=menubar)

root.mainloop()