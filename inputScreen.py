import tkinter as tk
from tkinter.constants import CENTER
from tkinter.font import BOLD
from graph import graphInit

font_color, bg_color, font_name  = "#F8FFE5","#736B92", "PierSans-Light"


def fields(root):
    global eq_field, start_field, inc_field, iter_field
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
        text="Lower Bound: ",
        bg=bg_color,
        fg=font_color,
        font=(font_name, 24)
    )
    start_label.place(x=25,y=225)

    start_field = tk.Entry(
        root, 
        font=(font_name, 24),
        bg=bg_color,
        fg = font_color
    )
    start_field.place(x=300, y=225,height=50,width=250)

    end_label = tk.Label(
        text="Upper Bound: ",
        bg=bg_color,
        fg=font_color,
        font=(font_name, 24)
    )
    end_label.place(x=25,y=300)

    end_field = tk.Entry(
        root, 
        font=(font_name, 24),
        bg=bg_color,
        fg = font_color
    )
    end_field.place(x=300, y=300,height=50,width=250)

    inc_label = tk.Label(
        text="Increment: ",
        bg=bg_color,
        fg=font_color,
        font=(font_name, 24)
    )
    inc_label.place(x=25,y=375)

    inc_field = tk.Entry(
        root, 
        font=(font_name, 24),
        bg=bg_color,
        fg = font_color
    )
    inc_field.place(x=300, y=375,height=50,width=250)

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
        command = lambda: graphInit(eq_field.get(), int(start_field.get()), int(end_field.get()), int(inc_field.get()), int(iter_field.get()))
    )
    graph_button.place(relx=.5,y=575,anchor=CENTER)


