import tkinter as tk
import tkinter.ttk as ttk
from ttkwidgets import TickScale
from constant import *
from logic import *


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.data = []
        self.select_alg_menu = tk.StringVar()
        self.title("Array sorter")
        self.maxsize(MAX_WIDTH, MAX_HEIGHT)

        self.style = ttk.Style(self)
        self.tk.call(
            'source', 'Azure-ttk-theme/azure dark/azure_dark.tcl')
        self.style.theme_use('azure_dark')

        self.top_menu = tk.Frame(self, width=MAX_WIDTH,
                                 height=MAX_HEIGHT/4, bg=grey)

        self.top_menu.grid(row=0, column=0, pady=4)

        self.drawArea = tk.Canvas(self, width=MAX_WIDTH,
                                  height=MAX_HEIGHT, bg=lightBlue)
        self.drawArea.grid(row=1, column=0)

        # first ROW
        tk.Label(self.top_menu, text="Algorithm: ", bg=grey).grid(
            row=0, column=0, padx=5, pady=5, sticky='')
        self.algorithm_menu = ttk.Combobox(
            self.top_menu, textvariable=self.select_alg_menu, values=[
                'SELECTION', 'BUBBLE', 'INSERTION'])
        self.algorithm_menu.grid(row=0, column=1, padx=15, pady=5)
        self.algorithm_menu.current([0])

        tk.Label(self.top_menu, text="Speed [s]: ", bg=grey).grid(
            row=0, column=2, padx=15, pady=5, sticky='SW')
        self.speedScale = TickScale(self.top_menu, from_=0.01, to=2,
                                    digits=2, orient='horizontal')
        self.speedScale.grid(row=0, column=3, columnspan=3,
                             padx=15, pady=0, sticky='W')

        # second ROW
        tk.Label(self.top_menu, text="Size: ", bg=grey).grid(
            row=1, column=0, padx=15, pady=3, sticky='SW')
        self.sizeEntry = TickScale(self.top_menu, from_=1, to=50,
                                   digits=0, orient='horizontal')
        self.sizeEntry.grid(row=1, column=1, padx=15, pady=0, sticky='W')

        tk.Label(self.top_menu, text="Min value: ", bg=grey).grid(
            row=1, column=2, padx=15, pady=3, sticky='SW')
        self.minEntry = TickScale(self.top_menu, from_=1, to=100,
                                  digits=0, orient='horizontal')
        self.minEntry.grid(row=1, column=3, padx=15, pady=3, sticky='W')

        tk.Label(self.top_menu, text="Max Value: ", bg=grey).grid(
            row=1, column=4, padx=15, pady=3, sticky='SW')
        self.maxEntry = TickScale(self.top_menu, from_=1, to=100,
                                  digits=0, orient='horizontal')
        self.maxEntry.grid(row=1, column=5, padx=15, pady=3, sticky='W')

        ttk.Button(self.top_menu, text="Generate",
                   command=lambda: Generate(self),
                   style='Accentbutton').grid(row=1, column=6, padx=15)
        ttk.Button(self.top_menu, text="Start", command=lambda: Start(
            self), style='Accentbutton').grid(row=0, column=6, padx=15)

    def Draw(self, color=list):
        self.drawArea.delete("all")
        total_height = MAX_HEIGHT-100
        rect_width = MAX_WIDTH / (len(self.data)+1)
        free_space = 20
        new_arr = []
        for i in self.data:
            new_arr.append(i / max(self.data))
        for i, height in enumerate(new_arr):
            x_left_top = i * rect_width + free_space
            y_left_top = total_height - height * (total_height-20)
            x_right_bottom = (i+1) * rect_width + free_space
            y_right_bottom = total_height
            self.drawArea.create_rectangle(
                x_left_top, y_left_top, x_right_bottom,
                y_right_bottom, fill=color[i])
            if int(self.sizeEntry.get()) < 30:
                self.drawArea.create_text(
                    x_left_top+2, y_left_top,
                    anchor='sw', text=str(self.data[i]))
        self.update_idletasks()
