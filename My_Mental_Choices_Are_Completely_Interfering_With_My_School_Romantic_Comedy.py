from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Maddog")

# Create the PhotoImage and label to hold it
madhav = PhotoImage(file="madhav.png")
label = Label(root, image=madhav)
label.pack()

# Create a button
button = ttk.Button(root, text="born in a world of strife")
button.pack()
# Run the mainloop
root.mainloop()
