import tkinter as tk
import gspread
from PIL import Image, ImageTk
from tkinter import Label, Tk, Canvas, Frame, BOTH, NW, W
gc = gspread.service_account(filename='C:/Users/kyles/Desktop/HACCS/auth.json')
sh = gc.open("tester")
worksheet = sh.get_worksheet(1)
Bed1111 = worksheet.acell('B2').value
Bed2111 = worksheet.acell('B3').value
root = tk.Tk()
root.title('Hospital Bed Map')
root.geometry('600x400+50+50')
root.resizable(True,True)
greenimg = ImageTk.PhotoImage(Image.open("green.png"))
gren = Label(root, image = greenimg)
redimg = ImageTk.PhotoImage(Image.open("red.png"))

red = Label(root, image = redimg)
yellowimg = ImageTk.PhotoImage(Image.open("yellow.png"))
ylow = Label(root, image = yellowimg)
while True:
    if Bed1111 == 0:
        gren.pack()
    elif Bed1111 == 1:
        red.pack()
    elif Bed1111 == 2:
        ylow.pack()
    if Bed2111 == 0:
        gren.pack()
    elif Bed2111 == 1:
        red.pack()
    elif Bed2111 == 2:
        ylow.pack()
    root.mainloop()


