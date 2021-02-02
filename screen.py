from tkinter import * 

root = Tk()

def window(self):
    self.title('sceen')
    self.resizable(0,0)
    self.update_idletasks()
    windowWidth = 650
    windowHeight = 400
    screenwidth = self.winfo_screenwidth()
    screenHeight = self.winfo_screenheight()
    x = (self.winfo_screenwidth() / 2) - (windowWidth / 2)
    y = (self.winfo_screenheight() / 2) - (windowHeight /2)
    self.geometry('%dx%d+%d+%d' % (windowWidth, windowHeight, x, y))
  
window(root)
root.mainloop()