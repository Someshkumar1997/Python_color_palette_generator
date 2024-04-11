import tkinter as tk
import random

root = tk.Tk()

root.title("Color Palette Generator")
root.geometry("300x600")


select_field = tk.StringVar(value= "1")
select = tk.OptionMenu(root, select_field, "1", "2", "3", "4", "5")
select.pack(side= "top", pady= 10)

generate_button = tk.Button(root, text="Generate", command= generate_palette)
generate_button.pack(side= "top")

color_frame = tk.Frame(root)
color_frame.pack(pady= 10)


root.mainloop()