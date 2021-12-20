import tkinter as tk
from tkinter.constants import CENTER
import time
from tkinter.font import BOLD

graph_bg,graph_color,font_name = "#000000","#FFFFFF","PierSans-Light"

def graphInit(eq, start, end, inc, iter):
    global canvas, area, sqQuant
    graph = tk.Toplevel()
    graph.title("Graph")
    graph.geometry("500x500")
    graph.resizable(False, False)

    canvas = tk.Canvas(graph, bg=graph_bg,height=500,width=500)
    canvas.place(relx=0.5,rely=0.5,anchor=CENTER)

    # Total Area  text
    area = tk.Label(
        graph,
        text="",
        bg=graph_bg,
        fg=graph_color,
        font=(font_name,20,BOLD)
    )
    area.place(relx=.5,y=450,anchor=CENTER)

    # # of squares text
    sqQuant = tk.Label(
        graph,
        text="",
        bg=graph_bg,
        fg=graph_color,
        font=(font_name,10)
    )
    sqQuant.place(relx=.9,y=25,anchor=CENTER)

    summation(eq, start, end, inc, iter, 5, 0)    


        
def summation(eq, start, end, inc, iter, n, i):
    canvas.delete('all')
    f = eq.split(" ")

    # inital vars for each iteration
    total = 0
    intX = (end-start)/n
    curr = start

    # Squares for each iteration
    for j in range(n):          
        y = 0
        # Find f(xi) using function
        for k in range(len(f)):
            y += int(f[k])*pow(curr,len(f)-k-1)
        
        drawSq(curr,y,intX)

        # Adding square area to total Riem. Sum
        total += y*intX
        # increment each x value
        curr += intX

    # update graph text
    area.config(text="Total Area: "+str(round(total,3)))
    sqQuant.config(text=str(n)+" squares")

    # recursivley calling the function allows for paused drawing
    if(i<iter):
        canvas.after(2000,lambda:summation(eq, start, end, inc, iter, n+inc, i+1))

def drawSq(x,y,inc):
    canvas.create_rectangle((x*20,300-(y),((x+inc)*20),300),fill=graph_color)
    
