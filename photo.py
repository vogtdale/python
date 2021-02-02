from tkinter import *

root = Tk()
root.title('windowname')
root.geometry("500x600")
root.configure(background="black")
root.resizable(0,0)

image = PhotoImage(file = "internet.gif")
imglabel = Label(image=image, bg="green")
imglabel.place(x=80,y=80)
root.mainloop()