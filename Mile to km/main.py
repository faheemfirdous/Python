from tkinter import *

window = Tk()
window.title("Mile to KM convertor")
window.minsize(width=250, height=100)


# controlling function

def convertor():
    miles = box.get()
    km = float(miles) * 1.60934
    result_label.config(text=km)


# font

font = ("Arial", 12)

# labels

mile_label = Label(text="mile", font=font)
mile_label.grid(row=1, column=3)
is_equal_label = Label(text="is equal to ", font=font)
is_equal_label.grid(row=2, column=1)
km_label = Label(text="km", font=font)
km_label.grid(row=2, column=3)

# button

button = Button(text="Calculate", font=font, command=convertor)
button.grid(row=3, column=2)

# box

box = Entry(width=10)
box.grid(row=1, column=2)

# label

result_label = Label(text="", font=font)
result_label.grid(row=2, column=2)

window.mainloop()
