from tkinter import *
from PIL import Image, ImageTk

# Import necessary libraries
from tkinter import Tk, Label, Entry, Button
from PIL import Image, ImageTk

# Create the main window
root = Tk()
root.title("Alarm Clock")

# Set padding and margins
root.grid_rowconfigure(0, pad=20)
root.grid_rowconfigure(5, pad=20)
root.grid_columnconfigure(0, pad=20)
root.grid_columnconfigure(3, pad=40)

# Create the header
head = Label(root, text="Alarm Clock", font=('comic sans', 20))
head.grid(row=0, column=1, columnspan=2)

# Load and display the image
original_image = Image.open("clock.png")
small_image = original_image.resize((150, 150))
clock_img = ImageTk.PhotoImage(small_image)

img = Label(root, image=clock_img)
img.grid(row=1, rowspan=4, column=0, padx=20)

# Create input elements
input_time = Label(root, text="Input Time", font=('comic sans', 18))
input_time.grid(row=1, column=1, columnspan=2, sticky="w")

alarm_time = Entry(root, font=('comic sans', 18), width=6)
alarm_time.grid(row=1, column=3, sticky="w")

msg = Label(root, text="Message", font=('comic sans', 18))
msg.grid(row=2, column=1, columnspan=2, sticky="w")

msg_input = Entry(root, font=('comic sans', 18), width=8)
msg_input.grid(row=2, column=3, columnspan=2, sticky="w")

# Create the submit button
submit = Button(root, text="Set Alarm", font=('comic sans', 18))
submit.grid(row=3, column=1, columnspan=2, sticky="w")

# Run the main loop
root.mainloop()
