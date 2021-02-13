import random
from tkinter import *
from tkinter import messagebox


def generate_password():
    """This function generates a random length password"""
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+', '@']

    password = []

    for num in range(2, 4):
        num_output = random.choice(numbers)
        password += num_output

    for symbol in range(2, 4):
        symbol_output = random.choice(symbols)
        password += symbol_output

    for letter in range(6, 10):
        letter_output = random.choice(letters)
        password += letter_output

    # Shuffle the generated password
    random.shuffle(password)

    # Convert the list to string
    password_generated = "".join(password)
    # Add the password generated to the password entry
    password_entry.insert(0, password_generated)


def save():
    """This function saves the information in a text file"""

    # Get the data in the entries
    website = website_entry.get()
    user = user_entry.get()
    password = password_entry.get()

    # Prevent empty field submission
    if len(website) == 0 or len(user) == 0 or len(password) == 0:
        messagebox.showwarning(title="Warning",
                               message="Empty fields cannot be submitted")
    else:
        # Verify details before saving
        confirm = messagebox.askokcancel(title="Information submitted",
                                         message=f"These are the details submitted: \n"
                                                 f"Website: {website}\n"
                                                 f"Email/Username: {user}\n"
                                                 f"Password: {password}\n"
                                                 f"Is it okay to save?")

        if confirm:
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

generate_button = Button(text="Generate Password", padx=5, pady=5, command=generate_password)
generate_button.grid(column=0, row=4)

add_button = Button(text="Add Information", padx=5, pady=5, fg="#fc1352", command=save)
add_button.grid(column=1, row=4)

# Keep the app open until exited
interface.mainloop()
