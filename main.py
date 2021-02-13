from tkinter import *

# App Interface
interface = Tk()
interface.title("A3AJAGBE OFFLINE PASSWORD-MANAGER")
interface.config(padx=20, pady=20, bg="white")

# Add image using canvas widget
canvas = Canvas(width=125, height=125)
bg_image = PhotoImage(file="lock.png")
canvas.create_image(65, 65, image=bg_image)
canvas.grid(column=1, row=1)

# Keep the app open until exited
interface.mainloop()
