import tkinter
from tkinter import *
import tkinter as tk
import PIL.Image
from PIL import ImageTk
import sys

window = tk.Tk()
window.title("Convert to Binary")
window.geometry("720x550")
window.resizable(0,0)
photo = tk.PhotoImage(file = 'Binary.png')
window.wm_iconphoto(False, photo)


cabezera = tkinter.Label(window, text = "Write the number you want to convert to Binary", font = ("Calibri", 20)).pack()

global number


img_bg = PIL.Image.open('background.jpg')
bg = ImageTk.PhotoImage(img_bg)
background = Label(window, image = bg)
background.place(x=0, y=0)


#----------------FUNCTIONS------------------#

def TextoEscrito():
	text = write.get()
	Label["text"] = text

def exit():
	sys.exit()

def calculator():
	modules = [] # la lista para guardar los módulos
	number = int(write.get())
	while number != 0:
		module = number % 2
		cociente = number // 2
		modules.append(module)
		number = cociente
		Label["text"] = modules


write = tk.Entry(window, font = "Calibri 40")
write.pack()

Label = tk.Label(window, font = "Calibri 50")
Label.pack()

button = tkinter.Button(window, text = "Convert",font = "Calibri 30", command = calculator)
button.pack()

exit = tkinter.Button(window, text = "EXIT", font = "Calibri 16", bg = "red", command = exit)
exit.place(x=650, y=490)





window.mainloop()