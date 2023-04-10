from tkinter import *
from tkinter import messagebox
from password_generator import PasswordGenerator
import pyperclip
import json


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
    new_data_dictionary = {
        website: {
            'user_name': user_name,
            'password': password,
        }
    }
    print(new_data_dictionary)

    if len(website) == 0 or len(user_name) == 0:
        messagebox.showerror(title='Error', message='Please fill all the fields')
    else:
        try:
            with open(file='data', mode='r') as data_file:
                passwords_file = json.load(data_file)
                data_file.close()

        except FileNotFoundError:
            with open('data', 'w') as data_file:
                json.dump(new_data_dictionary, data_file)
                data_file.close()
        else:
            passwords_file.update(new_data_dictionary)
            with open('data', 'w') as data_file:
                json.dump(passwords_file, data_file, indent=4)

        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)

        messagebox.showinfo(title='Saved', message='Password saved and copied to clipboard')


def search_password():
    password_for = website_entry.get()

    try:
        with open('data', 'r') as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title='Error', message="No data file found")

    else:
        if password_for in data:
            user_name = data[password_for]['user_name']
            password = data[password_for]['password']
            messagebox.showinfo(title=password_for, message=f'User: {user_name}\n password: {password}')
        else:
            messagebox.showinfo(title="Error", message=f"No details for {password_for} in database")


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
website_entry = Entry(width=21)
website_entry.grid(row=1, column=1)
website_entry.focus()
email_entry = Entry(width=43)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, 'your_email@gmail.com')
password_entry = Entry(width=43)
password_entry.grid(row=3, column=1, columnspan=2)

# buttons

gp_button = Button(text='Generate Password', width=18, command=password_generator)
gp_button.grid(row=4, column=2)

add_button = Button(text='Add', width=18, command=save_password)
add_button.grid(row=4, column=1)

search_button = Button(text='Search', command=search_password)
search_button.grid(row=1, column=2)
window.mainloop()
