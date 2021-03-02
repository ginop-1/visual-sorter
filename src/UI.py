import tkinter as tk
import tkinter.ttk as ttk
from ttkwidgets import TickScale
from constant import *
from logic import *
from threading import Thread


class App(tk.Tk):
    '''
    Main class, it contains all functions and objects connected to UI.
    '''

    def __init__(self):
        '''
        Create the structure of the UI
        '''
        super().__init__()
        self.data = []  # List that contain the data to sort
        self.select_alg_menu = tk.StringVar()
        self.stop = False
        self.rectangles = []
        self.colors = []
        self.title("Array sorter")
        self.maxsize(MAX_WIDTH, MAX_HEIGHT)
        self.iconphoto(True, tk.PhotoImage(file='sorter_icon.png'))

        # Setup of custom style
        self.style = ttk.Style(self)
        self.tk.call(
            'source', 'Azure-ttk-theme/azure dark/azure_dark.tcl')
        self.style.theme_use('azure_dark')

        # top_menu contains all the interactive component (button, sliders...)
        self.top_menu = tk.Frame(self, width=MAX_WIDTH,
                                 height=MAX_HEIGHT/4, bg=grey)

        self.top_menu.grid(row=0, column=0, pady=4)

        # drawArea is the Canvas where rectangles'll be drawn
        self.drawArea = tk.Canvas(self, width=MAX_WIDTH,
                                  height=MAX_HEIGHT, bg=lightBlue)
        self.drawArea.grid(row=1, column=0)

        # first ROW
        tk.Label(self.top_menu, text="Algorithm: ", bg=grey).grid(
            row=0, column=0, padx=5, pady=5, sticky='')
        self.algorithm_menu = ttk.Combobox(
            self.top_menu, textvariable=self.select_alg_menu, values=[
                'SELECTION', 'BUBBLE', 'INSERTION', 'QUICKSORT'])
        self.algorithm_menu.grid(row=0, column=1, padx=15, pady=5)
        self.algorithm_menu.current([0])

        tk.Label(self.top_menu, text="Speed [s]: ", bg=grey).grid(
            row=0, column=2, padx=15, pady=5, sticky='SW')
        self.speedScale = TickScale(self.top_menu, from_=0.005, to=2,
                                    digits=3, orient='horizontal')
        self.speedScale.grid(row=0, column=3, columnspan=3,
                             padx=15, pady=0, sticky='W')

        # second ROW
        tk.Label(self.top_menu, text="Size: ", bg=grey).grid(
            row=1, column=0, padx=15, pady=3, sticky='SW')
        self.sizeEntry = TickScale(self.top_menu, from_=1, to=200,
                                   digits=0, orient='horizontal')
        self.sizeEntry.grid(row=1, column=1, padx=15, pady=0, sticky='W')

        tk.Label(self.top_menu, text="Min value: ", bg=grey).grid(
            row=1, column=2, padx=15, pady=3, sticky='SW')
        self.minEntry = TickScale(self.top_menu, from_=1, to=200,
                                  digits=0, orient='horizontal')
        self.minEntry.grid(row=1, column=3, padx=15, pady=3, sticky='W')

        tk.Label(self.top_menu, text="Max Value: ", bg=grey).grid(
            row=1, column=4, padx=15, pady=3, sticky='SW')
        self.maxEntry = TickScale(self.top_menu, from_=1, to=200,
                                  digits=0, orient='horizontal')
        self.maxEntry.grid(row=1, column=5, padx=15, pady=3, sticky='W')

        ttk.Button(self.top_menu, text="Generate",
                   command=lambda: Generate(self),
                   style='Accentbutton').grid(row=1, column=6, padx=15)
        ttk.Button(self.top_menu, text="Start",
                   command=lambda: Thread(target=Start, args=(self, )).start(),
                   style='Accentbutton').grid(row=0, column=6, padx=15)
        ttk.Button(self.top_menu, text="Stop",
                   command=lambda: self.Stop(),
                   style='Accentbutton').grid(row=0, column=7, padx=15)

    def Draw(self, color=list, generate_flag=False):
        '''
        Creation of rectangles, it takes a color[] list
        because when sorting we need to know which are the
        rectangles to draw
        '''
        if self.stop:
            color = [rectBlue for x in range(len(self.data))]
        total_height = MAX_HEIGHT-(MAX_HEIGHT/10)  # left some space at top
        # rect_width is calculated knowing that there is
        # some free_space at the start and at the end
        rect_width = (MAX_WIDTH - MAX_WIDTH /
                      (len(self.data))) / (len(self.data))
        free_space = rect_width/2
        new_arr = []
        for i in self.data:
            # calculating relative height for canvas coordinate
            new_arr.append(i / max(self.data))
        if generate_flag:
            self.drawArea.delete("all")
        for i, height in enumerate(new_arr):
            x_left_top = i * rect_width + free_space
            y_left_top = total_height - height * (total_height-20)
            x_right_bottom = (i+1) * rect_width + free_space
            y_right_bottom = total_height
            if generate_flag:
                self.colors = [rectBlue for x in range(int(self.sizeEntry.get()))]
                self.rectangles.append(self.drawArea.create_rectangle(
                x_left_top, y_left_top, x_right_bottom,
                y_right_bottom, fill=color[i]))
            elif self.colors[i] != color[i]:
                self.drawArea.delete(self.rectangles[i])
                self.rectangles[i] = self.drawArea.create_rectangle(
                x_left_top, y_left_top, x_right_bottom,
                y_right_bottom, fill=color[i])
        for i in range(len(self.colors)):
            self.colors[i] = color[i]
        # self.update_idletasks()

    def Stop(self):
        # print("stopped")
        self.stop = True
