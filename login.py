from tkinter import *
import tkinter.messagebox as box

def submit():
    username = entry1.get()
    password = entry2.get()
    if (username == "admin" and password == "123"):
        box.showinfo("info", " correct")
    else:
        box.showinfo("info", "Invalid")


root = Tk()

frame = Frame(root)


label1 = Label(root, text="Username:")
label1.pack(padx=15,pady=5)
entry1 = Entry(root, bg="green")
entry1.pack(padx=15,pady=5)

label2 = Label(root, text="Password:")
label2.pack(padx=15,pady=5)
entry2 = Entry(root, bg="red", show="*")
entry2.pack(padx=15,pady=5)

btn = Button(frame, text="submit", command=submit)
btn.pack(side= RIGHT, padx=25)

frame.pack(padx=100,pady=19,)
root.mainloop()