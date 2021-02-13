from tkinter import *


def save():
    """This function saves the information in a text file"""

    # Get the data in the entries
    website = website_entry.get()
    user = user_entry.get()
    password = password_entry.get()

    # Add to the txt file
    with open("pass-manager-data.txt", mode='a') as file:
        file.write(f'{website} | {user} | {password}\n')

    # Clear the entry file
    website_entry.delete(0, "end")
    password_entry.delete(0, "end")


# App Interface
interface = Tk()
interface.title("A3AJAGBE OFFLINE PASSWORD-MANAGER")
interface.config(padx=50, pady=50, bg="white")

# Add image using canvas widget
canvas = Canvas(width=125, height=125)
bg_image = PhotoImage(file="lock.png")
canvas.create_image(65, 65, image=bg_image)
canvas.grid(column=0, columnspan=2, row=0)

# UI Layout
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

website_entry = Entry(width=30)
website_entry.grid(column=1, row=1)
website_entry.focus()

user_label = Label(text="Email or Username:")
user_label.grid(column=0, row=2)

user_entry = Entry(width=30)
user_entry.insert(END, "a3ajagbe@gmail.com")
user_entry.grid(column=1, row=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

password_entry = Entry(width=30)
password_entry.grid(column=1, row=3)

generate_button = Button(text="Generate Password", padx=5, pady=5)
generate_button.grid(column=0, row=4)

add_button = Button(text="Add Information", padx=5, pady=5, fg="#fc1352", command=save)
add_button.grid(column=1, row=4)

# Keep the app open until exited
interface.mainloop()
