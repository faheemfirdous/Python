# Library import
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

# variable to catch input
website = tkinter.StringVar()
email = tkinter.StringVar()
password = tkinter.StringVar()


# function to generate random password
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
    website_var = website.get()
    email_var = email.get()
    password_var = password.get()

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

            # saving credential in a txt file
            file = open("passlog.txt", 'a')
            file.write(website_var + " | " + email_var + " | " + password_var + "\n")
            file.close()

            # clearing entry box
            website.set("")
            email.set("")
            password.set("")
    else:
        messagebox.askretrycancel(title="Error", message="You haven't entered all the credentials")


# label
website_label = tkinter.Label(text='Website:')
email_label = tkinter.Label(text='Email/Username:')
password_label = tkinter.Label(text='Password:')

# entry
website_entry = tkinter.Entry(textvariable=website, width=35)
email_entry = tkinter.Entry(textvariable=email, width=35)
password_entry = tkinter.Entry(textvariable=password, width=21)

# button
gen_password_btn = tkinter.Button(window, text='Generate Password', command=gen_ran_pass)
submit_btn = tkinter.Button(window, text='Add', command=submit, width=36)

# placing the element in the grid
screen.grid(row=0, column=1)
website_label.grid(row=1, column=0)
website_entry.grid(row=1, column=1, columnspan=2, sticky=W)
email_label.grid(row=2, column=0)
email_entry.grid(row=2, column=1, columnspan=2, sticky=W)
password_label.grid(row=3, column=0)
password_entry.grid(row=3, column=1, sticky=W)
gen_password_btn.grid(row=3, column=2, sticky=W)
submit_btn.grid(row=4, column=1, columnspan=2, sticky=W)

# starting cursor in website entry
website_entry.focus()

window.mainloop()
