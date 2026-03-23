import tkinter as tk
from tkinter import messagebox
import database

def get_selected_row(event):
    global selected_tuple
    index = list1.curselection()
    if index:
        selected_tuple = list1.get(index)
        e1.delete(0, tk.END)
        e1.insert(tk.END, selected_tuple[1])
        e2.delete(0, tk.END)
        e2.insert(tk.END, selected_tuple[2])
        e3.delete(0, tk.END)
        e3.insert(tk.END, selected_tuple[3])
        e4.delete(0, tk.END)
        e4.insert(tk.END, selected_tuple[4])

def view_command():
    list1.delete(0, tk.END)
    for row in database.view():
        list1.insert(tk.END, row)

def search_command():
    list1.delete(0, tk.END)
    for row in database.search(name_text.get(), phone_text.get(), email_text.get(), address_text.get()):
        list1.insert(tk.END, row)

def add_command():
    database.insert(name_text.get(), phone_text.get(), email_text.get(), address_text.get())
    list1.delete(0, tk.END)
    list1.insert(tk.END, (name_text.get(), phone_text.get(), email_text.get(), address_text.get()))
    view_command()

def delete_command():
    database.delete(selected_tuple[0])
    view_command()

def update_command():
    database.update(selected_tuple[0], name_text.get(), phone_text.get(), email_text.get(), address_text.get())
    view_command()

window = tk.Tk()
window.title("Contact Management System")

l1 = tk.Label(window, text="Name")
l1.grid(row=0, column=0)
l2 = tk.Label(window, text="Phone")
l2.grid(row=0, column=2)
l3 = tk.Label(window, text="Email")
l3.grid(row=1, column=0)
l4 = tk.Label(window, text="Address")
l4.grid(row=1, column=2)

name_text = tk.StringVar()
e1 = tk.Entry(window, textvariable=name_text)
e1.grid(row=0, column=1)
phone_text = tk.StringVar()
e2 = tk.Entry(window, textvariable=phone_text)
e2.grid(row=0, column=3)
email_text = tk.StringVar()
e3 = tk.Entry(window, textvariable=email_text)
e3.grid(row=1, column=1)
address_text = tk.StringVar()
e4 = tk.Entry(window, textvariable=address_text)
e4.grid(row=1, column=3)

list1 = tk.Listbox(window, height=6, width=35)
list1.grid(row=2, column=0, rowspan=6, columnspan=2)

sb1 = tk.Scrollbar(window)
sb1.grid(row=2, column=2, rowspan=6)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

list1.bind("<<ListboxSelect>>", get_selected_row)

b1 = tk.Button(window, text="View All", width=12, command=view_command)
b1.grid(row=2, column=3)
b2 = tk.Button(window, text="Search", width=12, command=search_command)
b2.grid(row=3, column=3)
b3 = tk.Button(window, text="Add", width=12, command=add_command)
b3.grid(row=4, column=3)
b4 = tk.Button(window, text="Update", width=12, command=update_command)
b4.grid(row=5, column=3)
b5 = tk.Button(window, text="Delete", width=12, command=delete_command)
b5.grid(row=6, column=3)
b6 = tk.Button(window, text="Close", width=12, command=window.destroy)
b6.grid(row=7, column=3)

window.mainloop()
