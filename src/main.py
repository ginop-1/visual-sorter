import  tkinter        as      tk
import  tkinter.ttk    as      ttk
from    ttkwidgets     import  TickScale
from    constant       import *
from    random         import  randint, seed, shuffle
from    time           import  time
import  algo

# function
array_values= []

def Generate():
    global array_values
    array_values = []
    min_value = int(minEntry.get())
    max_value = int(maxEntry.get())
    size = int(sizeEntry.get())
    for i in range(size):
        array_values.append(int((max_value/size)*(i+1)))
    shuffle(array_values)
    Draw(array_values, [rectBlue for x in range(len(array_values))])

def Draw(arr_data, color):
    drawArea.delete("all")
    total_height = MAX_HEIGHT-100
    rect_width = MAX_WIDTH / (len(arr_data)+1)
    free_space = 20
    new_arr = []
    for i in arr_data:
        new_arr.append( i / max(arr_data))
    for i, height in enumerate(new_arr):
        x_left_top      = i * rect_width        + free_space
        y_left_top      = total_height - height * (total_height-20)
        x_right_bottom  = (i+1) * rect_width    + free_space
        y_right_bottom  = total_height
        drawArea.create_rectangle(x_left_top, y_left_top, x_right_bottom, y_right_bottom, fill=color[i])
        if int(sizeEntry.get()) < 30:
            drawArea.create_text(x_left_top+2, y_left_top, anchor='sw', text=str(arr_data[i]))
    window_root.update_idletasks()

def Start():
    global array_values
    if (algorithm_menu.get() == 'SELECTION'):
        algo.selection_sort(array_values, Draw, speedScale.get())
    elif (algorithm_menu.get() == 'BUBBLE'):
        algo.bubble_sort(array_values, Draw, speedScale.get())
    elif (algorithm_menu.get() == 'INSERTION'):
        algo.insertion_sort(array_values, Draw, speedScale.get())

# creating window_root
window_root = tk.Tk()
window_root.title("Array sorter")
window_root.maxsize(MAX_WIDTH, MAX_HEIGHT)

# custom style
style = ttk.Style(window_root)
window_root.tk.call('source', 'Azure-ttk-theme/azure dark/azure_dark.tcl')
style.theme_use('azure_dark')

# stringVar
select_alg_menu = tk.StringVar()

# UI structure
top_menu = tk.Frame(window_root, width=MAX_WIDTH, height=MAX_HEIGHT/4, bg=grey)
top_menu.grid(row=0, column=0, pady=4)

drawArea = tk.Canvas(window_root, width=MAX_WIDTH, height=MAX_HEIGHT, bg=lightBlue)
drawArea.grid(row=1, column=0)

# first ROW
tk.Label(top_menu, text="Algorithm: ", bg=grey).grid(row=0, column=0, padx=5, pady=5, sticky='')
algorithm_menu = ttk.Combobox(top_menu, textvariable=select_alg_menu, values=['SELECTION', 'BUBBLE', 'INSERTION'])
algorithm_menu.grid(row=0, column=1, padx=15, pady=5)
algorithm_menu.current(0)

tk.Label(top_menu, text="Speed [s]: ", bg=grey).grid(row=0, column=2, padx=15, pady=5, sticky='SW')
speedScale = TickScale(top_menu, from_=0.01, to=2, digits=2, orient='horizontal')
speedScale.grid(row=0, column=3, columnspan=3, padx=15, pady=0, sticky='W')

# second ROW
tk.Label(top_menu, text="Size: ", bg=grey).grid(row=1, column=0, padx=15, pady=3, sticky='SW')
sizeEntry = TickScale(top_menu, from_=1, to=50, digits=0, orient='horizontal')
sizeEntry.grid(row=1, column=1, padx=15, pady=0, sticky='W')


tk.Label(top_menu, text="Min value: ", bg=grey).grid(row=1, column=2, padx=15, pady=3, sticky='SW')
minEntry = TickScale(top_menu, from_=1, to=100, digits=0, orient='horizontal')
minEntry.grid(row=1, column=3, padx=15, pady=3, sticky='W')

tk.Label(top_menu, text="Max Value: ", bg=grey).grid(row=1, column=4, padx=15, pady=3, sticky='SW')
maxEntry = TickScale(top_menu, from_=1, to=100, digits=0, orient='horizontal')
maxEntry.grid(row=1, column=5, padx=15, pady=3, sticky='W')

ttk.Button(top_menu, text="Generate", command=Generate, style='Accentbutton').grid(row=1, column=6, padx=15)
ttk.Button(top_menu, text="Start", command=Start, style='Accentbutton').grid(row=0, column=6, padx=15)

window_root.mainloop()