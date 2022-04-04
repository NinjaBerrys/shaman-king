from tkinter import *

root = Tk()
root.title("Maddog")

# Create the PhotoImage and label to hold it
madhav = PhotoImage(file="madhav.png")
image_label = Label(root, image=madhav)
image_label.pack()

# Run the mainloop
root.mainloop()
