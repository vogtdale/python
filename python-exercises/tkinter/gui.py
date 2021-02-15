from tkinter import *

def submit():

    n = int(entry_number.get())
    results = n*2

    entry_number2.delete(0,END)
    entry_number2.insert(0,results)


    

window = Tk()
window.geometry("400x300")
label_number = Label(window, text = " Enter the value") 
label_number.place(x = 50, y = 50)
entry_number = Entry(window)
entry_number.place(x = 200, y = 55)

label_number2 = Label(window, text = " Double Value") 
label_number2.place(x = 50, y = 100)
entry_number2 = Entry(window)
entry_number2.place(x = 200, y = 100)

submit_button = Button(window, text=" Submit", command = submit)
submit_button.place(x = 300, y = 200)

window.mainloop()