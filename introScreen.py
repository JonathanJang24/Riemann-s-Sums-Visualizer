import tkinter as tk
from tkinter import font
from tkinter.constants import CENTER, GROOVE, RIDGE, S, SUNKEN, UNDERLINE
from tkinter.font import BOLD, ITALIC
from PIL import Image, ImageTk
from inputScreen import fields

font_color, bg_color, font_name  = "#F8FFE5","#736B92", "PierSans-Light"

def start():
    # clears widgets off of current screen 
    for w in root.winfo_children():
        if(str(w)!='.!label'):
            w.destroy()
    fields(root)

# Tkinter initialization
root = tk.Tk()
root.geometry("640x640")
root.configure(bg=bg_color)
root.resizable(False,False)
root.title("Riemann's Sum")

#Wave background
frame = tk.Frame(root)
frame.place(relx=.5,rely=.8,anchor=CENTER)
canvas = tk.Canvas(frame,bg=bg_color,width=840,height=840,highlightthickness=0)
canvas.pack()
waveinit = Image.open("wave.png")
waveinit = waveinit.resize((740,480))
wave = ImageTk.PhotoImage(waveinit)
canvas.create_image(380,310,anchor=CENTER,image=wave)

# Title Label
title = tk.Label(
    text = "Riemann's Sum Visualizer",
    font=(font_name,35,BOLD,UNDERLINE),
    fg=font_color,
    bg=bg_color,
)
title.place(relx=.5,y=80,anchor=CENTER)

# Created by label
credit = tk.Label(
    text = "Created by: Jonathan Jang",    font=(font_name,24,UNDERLINE),
    fg=font_color,
    bg=bg_color
)
credit.place(relx=.5,y=160,anchor=CENTER)

# Description label
description = tk.Label(
    text="A Python program created with the intent to help students\nbetter visualize and understand the concept of\nRiemann's Sums. Riemann's Sums is an essential calculus\nconcept which estimates the area under a curve. As more\nrectangles are used to estimate, a limit is formed that\napproaches the indefinite integral: the true value of the area.",
    font=(font_name, 16),
    foreground=font_color,
    bg=bg_color
)
description.place(relx=.5,y=300,anchor=CENTER)

begin = tk.Button(
    text="Begin Visualizing →",
    foreground=font_color,
    font=(font_name,20,BOLD),
    background=bg_color,
    command = start,
    activebackground=bg_color,
    activeforeground=font_color
)
begin.place(relx=.5,y=500,anchor=CENTER)


root.mainloop()