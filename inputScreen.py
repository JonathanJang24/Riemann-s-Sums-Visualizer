import tkinter as tk
from tkinter.constants import CENTER
from tkinter.font import BOLD
from graph import visual

font_color = "#F8FFE5"
bg_color = "#736B92"
font_name = "PierSans-Light"

def fields(root):

    eq_label = tk.Label(
        text="Enter equation: ",
        bg=bg_color,
        fg=font_color,
        font=(font_name, 24)
    )
    eq_label.place(x=25,y=150)

    eq_field = tk.Entry(
        root,
        font=(font_name, 24),
        bg=bg_color,
        fg=font_color,
    )
    eq_field.place(x=300,y=150,height=50,width=250)

    start_label = tk.Label(
        text="Starting Number: ",
        bg=bg_color,
        fg=font_color,
        font=(font_name, 24)
    )
    start_label.place(x=25,y=250)

    start_field = tk.Entry(
        root, 
        font=(font_name, 24),
        bg=bg_color,
        fg = font_color
    )
    start_field.place(x=300, y=250,height=50,width=250)

    inc_label = tk.Label(
        text="Increment: ",
        bg=bg_color,
        fg=font_color,
        font=(font_name, 24)
    )
    inc_label.place(x=25,y=350)

    inc_field = tk.Entry(
        root, 
        font=(font_name, 24),
        bg=bg_color,
        fg = font_color
    )
    inc_field.place(x=300, y=350,height=50,width=250)

    iter_label = tk.Label(
        text="Iterations: ",
        bg= bg_color,
        fg=font_color,
        font=(font_name, 24)
    )
    iter_label.place(x=25,y=450)

    iter_field = tk.Entry(
        root, 
        font=(font_name, 24),
        bg=bg_color,
        fg = font_color
    )
    iter_field.place(x=300, y=450,height=50,width=250)

    graph_button = tk.Button(
        text="Graph →",
        bg = bg_color,
        fg = font_color,
        font=(font_name, 20, BOLD),
        activebackground=bg_color,
        activeforeground=font_color,
        command = visual
    )
    graph_button.place(relx=.5,y=575,anchor=CENTER)


