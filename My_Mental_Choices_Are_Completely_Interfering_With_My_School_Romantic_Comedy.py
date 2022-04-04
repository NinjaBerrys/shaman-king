from tkinter import *

root = Tk()
root.title("Maddog")

# Create the PhotoImage and label to hold it
madhav = PhotoImage(file="madhav.png")
label = Label(root, image=madhav)
label.pack()
# Run the mainloop
root.mainloop()
