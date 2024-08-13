import tkinter as tk
from tkinter import ttk
from mainFrame import StartPage


class Procesare(tk.Frame):
    def __init__(self, parent,controller):
        tk.Frame.__init__(self, parent)

        label = ttk.Label(self, text ="Procesare Imagini")
        label.grid(row = 0, column = 4, padx = 10, pady = 10)

        button1 = ttk.Button(self, text ="Pagina de Start",command = lambda : controller.show_frame(StartPage))
        button1.grid(row = 1,column = 1,padx = 10,pady =10)
        
