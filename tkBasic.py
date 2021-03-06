import tkinter as tk
from tkinter import LEFT, RIGHT, END, TOP, X, YES
import numpy as np

# Window
window = tk.Tk()
window.title('My Window')
window.geometry('500x650')

# Generate Data
xs = np.linspace(0, 400)
ys = xs * np.sin(xs/400*np.pi) + 100

# Canvas
canvas = tk.Canvas(window, bg='blue', height=400, width=400)
# Draw line
for i in range(len(xs)-1):
    x0, y0, x1, y1 = xs[i], ys[i], xs[i+1], ys[i+1]
    line = canvas.create_line(x0, y0, x1, y1)

# Draw points
points = {}
for i in range(len(xs)):
    x0, y0, x1, y1 = xs[i]-4, ys[i]-4, xs[i]+4, ys[i]+4 # 4 is radius
    oval = canvas.create_oval(x0, y0, x1, y1, fill='yellow')
    points[(xs[i], ys[i])] = oval

# Change Color when mouse click
def callback(event):
    def find_nearest_point(event, points):
        best_dist = float('inf')
        best_oval = None
        for (xi, yi), o in points.items():
            dist = np.sqrt((event.x - xi)**2 + (event.y - yi)**2)
            if dist < best_dist:
                best_oval = o
                best_dist = dist
        if best_oval: 
            return best_oval
    oval = find_nearest_point(event, points)
    canvas.itemconfig(oval, fill="red")
    print("clicked at", event.x, event.y)

canvas.bind("<Button-1>", callback)
canvas.pack()

# Params
fields = 'Last Name', 'First Name', 'Job', 'Country'
def fetch(entries):
   for entry in entries:
      field = entry[0]
      text  = entry[1].get()
      entry[1].delete(0, END)
      print('%s: "%s"' % (field, text))

def makeform(root, fields):
   entries = []
   for field in fields:
      row = tk.Frame(root)
      lab = tk.Label(row, width=15, text=field, anchor='w')
      ent = tk.Entry(row)
      row.pack(side=TOP, fill=X, padx=5, pady=5)
      lab.pack(side=LEFT)
      ent.pack(side=RIGHT, expand=YES, fill=X)
      entries.append((field, ent))
   return entries

ents = makeform(window, fields)

# Button
b_submit = tk.Button(window, text='Submit', width=15, height=2,
                     command=(lambda e=ents: fetch(e)))
b_submit.pack(side=LEFT)

def reset_color():
    for o in points.values():
        canvas.itemconfig(o, fill='yellow')
b_reset = tk.Button(window, text='Reset', width=15, height=2, command=reset_color)
b_reset.pack(side=LEFT)

b_quit = tk.Button(window, text='Quit', width=15, height=2, command=window.quit)
b_quit.pack(side=LEFT)

# Main Loop
window.mainloop()
