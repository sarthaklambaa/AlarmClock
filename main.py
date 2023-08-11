from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title("Alarm Clock")
root.geometry("530x330")

head =  Label(root, text="Alarm Clock", font=('comic sans', 20))
head.grid(row=0, columnspan=3)

original_image = Image.open("clock.png")  
small_image = original_image.resize((150, 150)) 
clock_img = ImageTk.PhotoImage(small_image)

img = Label(root, image=clock_img)
img.grid(rowspan=4, column=0)

root.mainloop()