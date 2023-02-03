# importing library

from tkinter import *
from PIL import ImageTk, Image
import time

splash_root = Tk()
splash_root.title("splash-screen")
# screen size
splash_root.geometry("300x550")
splash_root.config(bg="#FFFFFF")
# splash screen content
splash = ImageTk.PhotoImage(Image.open("L1.png"))
splashLogo = Label(splash_root, image=splash).place(x=15, y=30)

label2 = Label(splash_root, text='Loading...', fg='white', bg='#ff9a00')  # decorate it
label2.configure(font=("Calibri", 11))
label2.place(x=10, y=500)

# making animation

image_a = ImageTk.PhotoImage(Image.open('Ellipse1.png'))
image_b = ImageTk.PhotoImage(Image.open('Ellipse2.png'))

for i in range(3):  # loops

    l1 = Label(splash_root, image=image_a, border=0, relief=SUNKEN).place(x=120, y=400)
    l2 = Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=140, y=400)
    l3 = Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=160, y=400)
    l4 = Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=180, y=400)
    splash_root.update_idletasks()
    time.sleep(0.5)

    l1 = Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=120, y=400)
    l2 = Label(splash_root, image=image_a, border=0, relief=SUNKEN).place(x=140, y=400)
    l3 = Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=160, y=400)
    l4 = Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=180, y=400)
    splash_root.update_idletasks()
    time.sleep(0.5)

    l1 = Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=120, y=400)
    l2 = Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=140, y=400)
    l3 = Label(splash_root, image=image_a, border=0, relief=SUNKEN).place(x=160, y=400)
    l4 = Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=180, y=400)
    splash_root.update_idletasks()
    time.sleep(0.5)

    l1 = Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=120, y=400)
    l2 = Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=140, y=400)
    l3 = Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=160, y=400)
    l4 = Label(splash_root, image=image_a, border=0, relief=SUNKEN).place(x=180, y=400)
    splash_root.update_idletasks()
    time.sleep(0.5)


# new window to open
def new_win():
    home = Tk()
    home.title('HOME PAGE')
    home.geometry("300x550")
    home.config(bg="#FFFFFF")
    # anything we need to appear in main page write in this function

    home.mainloop()


splash_root.destroy()
new_win()
splash_root.mainloop()
