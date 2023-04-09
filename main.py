from tkinter import *
from tkinter import messagebox
from password_generator import PasswordGenerator
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

#
def password_generator():
    password_entry.delete(0, END)
    pswd = PasswordGenerator()
    pswd.minlen = 12
    pswd.maxlen = 12
    generated_password = str(pswd.generate())
    password_entry.insert(0, generated_password)
    pyperclip.copy(generated_password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = website_entry.get()
    user_name = email_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(user_name) == 0:
        messagebox.showerror(title='Error', message='Please fill all the fields')
    else:
        with open('password_data.txt', 'a') as data:
            data.write(f'{website} | {user_name} | {password}\n')
            website_entry.delete(0, END)
            password_entry.delete(0, END)
        messagebox.showinfo(title='Saved', message='Password saved and copied to clipboard')


# ---------------------------- UI SETUP -------- ----------------------- #
# window


window = Tk()
window.title('Password Manager')
window.config(pady=50, padx=50)

# logo
logo = PhotoImage(file='logo.png')

# canvas
canvas = Canvas(height=200, width=200, )
canvas.create_image(150, 100, image=logo)
canvas.grid(row=0, column=1, )

# Labels
website_label = Label(text='Website:')
website_label.grid(row=1, column=0)
email_label = Label(text='Email/Username:')
email_label.grid(row=2, column=0)
password_label = Label(text='Password:')
password_label.grid(row=3, column=0)

# Entries
website_entry = Entry(width=36)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()
email_entry = Entry(width=36)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, 'your_email@gmail.com')
password_entry = Entry(width=36)
password_entry.grid(row=3, column=1, columnspan=2)

# buttons

gp_button = Button(text='Generate Password', width=18, command=password_generator)
gp_button.grid(row=4, column=2)

add_button = Button(text='Add', width=18, command=save_password)
add_button.grid(row=4, column=1)

window.mainloop()
