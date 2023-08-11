from tkinter import *

root = Tk()
root.title=("Alarm Clock")
root.geometry("530x330")
head =  Label(root, text="Alarm Clock", font=('comic sans', 20))
head.grid(row=0, columnspan=3)

root.mainloop()