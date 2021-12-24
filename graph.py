import tkinter as tk
from tkinter.constants import CENTER, FALSE
import time
import math
from tkinter.font import BOLD

graph_bg,graph_color,font_name,bg_color, error_color = "#736B92","#F8FFE5","PierSans-Light","#736B92", "#F88379"

def isNum(x):
    isInt = True
    try:
        int(x)
    except:
        isInt = False
    return isInt

def graphInit(eq, start, end, inc, iter):
    global canvas, area, sqQuant, lowerY, upperY
    error = tk.Label(
            text="",
            fg=error_color,
            bg=bg_color,
            font=(font_name, 16)
        )
    error.place(relx=.5,y=520,anchor=CENTER)
    if(not(isNum(start) and isNum(end) and isNum(inc) and isNum(iter))):
        error.config(text="Error, invalid input.")
        return FALSE
    else:
        error.config(text="                                     ")

    start, end, inc, iter = int(start), int(end), int(inc), int(iter)
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
        font=(font_name,16,BOLD)
    )
    area.place(relx=.5,y=470,anchor=CENTER)

    # number of squares text
    sqQuant = tk.Label(
        graph,
        text="",
        bg=graph_bg,
        fg=graph_color,
        font=(font_name,10)
    )
    sqQuant.place(relx=1,y=20,anchor='e')

    # Upper and lower bound label
    lowerX = tk.Label(
        graph,
        text=start,
        bg=graph_bg,
        fg=graph_color,
        font=(font_name,10)
    )
    lowerX.place(x=0, rely=.51, anchor='w')

    upperX = tk.Label(
        graph,
        text=end,
        bg=graph_bg,
        fg=graph_color,
        font=(font_name,10)
    )
    upperX.place(relx=1,rely=.51,anchor='e')

    # Upper and lower Y labels
    lowerY = tk.Label(
        graph,
        text ="3",
        bg=graph_bg,
        fg=graph_color,
        font=(font_name,10)
    )
    lowerY.place(relx=0.05,y=473,anchor=CENTER)
    upperY = tk.Label(
        graph,
        text ="5",
        bg=graph_bg,
        fg=graph_color,
        font=(font_name,10)
    )
    upperY.place(relx=.05,y=15,anchor=CENTER)

    summation(eq, start, end, inc, iter, 5, 0)    
        
def summation(eq, start, end, inc, iter, n, i):
    canvas.delete('all')
    vals = []

    # x axis line
    canvas.create_rectangle((28,255,470,257),fill=graph_color)
    # y axis line
    canvas.create_rectangle((28,30,30,470),fill=graph_color)
    f = eq.split(" ")

    # inital vars for each iteration
    total = 0
    intX = (end-start)/n
    curr = start
    maxY = 0

    # Squares for each iteration
    for j in range(n):          
        y = 0
        # Find f(xi) using function
        for k in range(len(f)):
            y += int(f[k])*pow(curr,len(f)-k-1)
        
        if(abs(y)>maxY):
            maxY = abs(y)
        vals.append((j,y))

        # Adding square area to total Riem. Sum
        total += y*intX
        # increment each x value
        curr += intX

    lowerY.config(text="-"+str(math.ceil(maxY)))
    upperY.config(text=str(math.ceil(maxY)))

    # update graph text
    area.config(text="Total Area: "+str(round(total,3)))
    sqQuant.config(text=str(n)+" squares")


    drawSq(vals,0,n,maxY)
    # recursivley calling the function allows for paused drawing
    if(i<iter-1):
        canvas.after(6000,lambda:summation(eq, start, end, inc, iter, n+inc, i+1))

def drawSq(vals,i,n,maxY):
    x,y = vals[i]

    xdiv = 440/n
    ydiv = 226/maxY

    canvas.create_rectangle((30+(x*xdiv),256-(ydiv*y),(30+((x+1)*xdiv)),256),fill=graph_color)

    if(i<len(vals)-1):
        canvas.after(int(4500/len(vals)),lambda:drawSq(vals,i+1,n,maxY))
    
