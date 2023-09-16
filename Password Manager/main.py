# Library import
import json
import tkinter
from tkinter import *
import random
import string
from tkinter import messagebox
import pyperclip

window = Tk()

window.title("Password Manager")
window.config(padx=40, pady=40)

# canvas and image size
screen = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
screen.create_image(100, 100, image=logo_img)


# function to generate random password
def search():
    website_var = website_entry.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No data in file")
    else:
        if website_var in data:
            email = data[website_var]['email']
            password = data[website_var]['password']
            messagebox.showinfo(title="Website", message=f"Email: {email}\n"
                                                         f"Password: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details found:(")


def gen_ran_pass():
    password_entry.delete(0, END)
    letters = string.ascii_letters + string.digits + string.punctuation
    ran_pass = ''.join(random.choice(letters) for _ in range(10))
    password_entry.insert(0, ran_pass)
    # this will copy the randomly generated password to the clipboard
    pyperclip.copy(ran_pass)
    return ran_pass


# function to save data
def submit():
    website_var = website_entry.get()
    email_var = email_entry.get()
    password_var = password_entry.get()
    new_data = {website_var: {
        "email": email_var,
        "password": password_var
    }}

    # printing credentials in terminal
    print("The website is: " + website_var)
    print("the email is : " + email_var)
    print("The password is: " + password_var)

    # checking if credential are empty
    if len(website_var) and len(email_var) and len(password_var) != 0:
        # pop up dialog box
        is_ok = messagebox.askokcancel(title="Website", message=f"These are the details entered:\n"
                                                                f"Email:{website_var} \n Password:{password_var}\n"
                                                                f"is it okay to save")
        if is_ok:
            # # Using the repr() function to convert the string values to their string representation
            # website_var = repr(website_var)
            # email_var = repr(email_var)
            # password_var = repr(password_var)

            try:
                # reading data from json file
                with open("data.json", "r") as data_file:
                    # Reading old data
                    data = json.load(data_file)
            except FileNotFoundError:
                with open("data.json", "w") as data_file:
                    json.dump(new_data, data_file, indent=4)
            else:
                # Updating old data with new data
                data.update(new_data)
                with open("data.json", "w") as data_file:
                    # Saving updated data
                    json.dump(data, data_file, indent=4)
            finally:
                # clearing entry box
                website_entry.delete(0, END)
                email_entry.delete(0, END)
                password_entry.delete(0, END)
                # we can use another method to delete entry's value by use set() method but for that we need to use
                # entry variables -->website = tkinter.StringVar()
    else:
        # error message
        messagebox.askretrycancel(title="Error", message="You haven't entered all the credentials")


# label
website_label = tkinter.Label(text='Website:')
email_label = tkinter.Label(text='Email/Username:')
password_label = tkinter.Label(text='Password:')

# entry
website_entry = tkinter.Entry(width=35)
email_entry = tkinter.Entry(width=35)
password_entry = tkinter.Entry(width=21)

# button
gen_password_btn = tkinter.Button(window, text='Generate Password', command=gen_ran_pass)
submit_btn = tkinter.Button(window, text='Add', command=submit, width=36)
search_btn = tkinter.Button(window, text="Search", command=search)

# placing the element in the grid
screen.grid(row=0, column=1)
website_label.grid(row=1, column=0)
website_entry.grid(row=1, column=1, columnspan=1, sticky=W)
search_btn.grid(row=1, column=2)
email_label.grid(row=2, column=0)
email_entry.grid(row=2, column=1, columnspan=2, sticky=W)
password_label.grid(row=3, column=0)
password_entry.grid(row=3, column=1, sticky=W)
gen_password_btn.grid(row=3, column=2, sticky=W)
submit_btn.grid(row=4, column=1, columnspan=2, sticky=W)

# starting cursor in website entry
website_entry.focus()

window.mainloop()

