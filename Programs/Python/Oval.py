# draw an oval

import tkinter as tk

root = tk.Tk()
root.title("Oval")

canvas = tk.Canvas(root, width=500, height=500)
canvas.pack()

canvas.create_oval(10, 10, 300, 200, width=2, fill="yellow")

root.mainloop()

