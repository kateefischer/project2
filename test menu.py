# using Tkinter's Optionmenu() as a combobox

try:
    # Python2
    import Tkinter as tk
except ImportError:
    # Python3
    import tkinter as tk

def select():
    sf = "value is %s" % var.get()
    root.title(sf)
    # optional
    color = var.get()
    root['bg'] = color


root = tk.Tk()
# use width x height + x_offset + y_offset (no spaces!)
root.geometry("%dx%d+%d+%d" % (330, 80, 200, 150))
root.title("choose option")

var = tk.StringVar(root)
# initial value
var.set('Is the person a girl?')

choices = ['Is the person a girl?', 'Is the person a boy?', 'Is this person wearing red?', 'Is this person wearing blue?','Is this person wearing black?', 'Is this person wearing grey?', 'Is this person wearing tan?', 'Is this person wearing white?', 'Is this person wearing purple?' ,'Is this person wearing mint?', 'Is the person smiling with teeth?', 'Is the person smiling without teeth?']
option = tk.OptionMenu(root, var, *choices)
option.pack(side='left', padx=10, pady=10)

button = tk.Button(root, text="check value slected", command=select)
button.pack(side='left', padx=20, pady=10)

root.mainloop()