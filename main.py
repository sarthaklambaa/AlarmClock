from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import time
from pygame import mixer

root = Tk()
root.title("Alarm Clock")

root.grid_rowconfigure(0, pad=20)
root.grid_rowconfigure(5, pad=20)
root.grid_columnconfigure(0, pad=20)
root.grid_columnconfigure(3, pad=40)

alarmtime = StringVar()
msginp = StringVar()

mixer.init()

head = Label(root, text="Alarm Clock", font=('Helvetica', 20, 'bold'))
head.grid(row=0, column=1, columnspan=2, pady=10)


def ala():
    confirm = messagebox.askquestion("Set Alarm", "Do you want to set the alarm?")
    if confirm == 'yes':
        a = alarmtime.get()
        AlarmT = a
        CurrentTime = time.strftime('%H:%M')

        while AlarmT != CurrentTime:
            CurrentTime = time.strftime('%H:%M')

        if AlarmT == CurrentTime:
            mixer.music.load("alarm.mp3")
            mixer.music.play()
            msg = messagebox.showinfo("Info", f"Alarm: {msginp.get()}")
            if msg == 'ok':
                mixer.stop()

original_image = Image.open("clock.png")
small_image = original_image.resize((150, 150))
clock_img = ImageTk.PhotoImage(small_image)

img = Label(root, image=clock_img)
img.grid(row=1, rowspan=4, column=0, padx=20)

input_time = Label(root, text="Input Time", font=('Helvetica', 18))
input_time.grid(row=1, column=1, columnspan=2, sticky="w", pady=5)

alarm_time = Entry(root, textvariable=alarmtime, font=('Helvetica', 18), width=8)
alarm_time.grid(row=1, column=3, sticky="w", pady=5)

msg = Label(root, text="Message", font=('Helvetica', 18))
msg.grid(row=2, column=1, columnspan=2, sticky="w", pady=5)

msg_input = Entry(root, textvariable=msginp, font=('Helvetica', 18), width=15)
msg_input.grid(row=2, column=3, columnspan=2, sticky="w", pady=5)

submit = Button(root, text="Set Alarm", font=('Helvetica', 18), command=ala)
submit.grid(row=3, column=1, columnspan=2, sticky="w", pady=10)

root.mainloop()
