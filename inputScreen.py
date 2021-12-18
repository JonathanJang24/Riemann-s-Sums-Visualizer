import tkinter as tk

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
        fg=font_color
    )
    eq_field.place(x=300,y=150,height=50,width=250)
