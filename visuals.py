import tkinter as tk


font_color = "#FFF"
bg_color = "#000000"

root = tk.Tk()

root.geometry("640x640")

label = tk.Label(
    text = "Riemann's Sum Visualizer",
    font=("Arial",16),
    foreground=font_color,
    background=bg_color
)
label.place(
    x = 100,
    y = 200,
    anchor='n'
)

# lambda creates anon-func as the .after function requires a method
label.after(3000, lambda: label.place(
    x = 500,
    y = 500,
    anchor='s'
))


root.mainloop()