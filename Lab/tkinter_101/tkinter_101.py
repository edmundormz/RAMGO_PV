from tkinter_101 import *

window = Tk()


def km_to_miles():
    miles = float(e1_value.get()) * 1.609
    t1.delete("1.0", END)
    t1.insert(END, miles)


# Buttons
b1 = Button(window, text="Execute", command=km_to_miles)
b1.grid(row=0, column=0)

# Texts
t1 = Text(window, height=1, width=20)
t1.grid(row=0, column=2)

# Entries

e1_value = StringVar()
e1 = Entry(window, textvariable=e1_value)
e1.grid(row=0, column=1)

window.mainloop()
