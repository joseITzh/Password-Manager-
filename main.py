#With "*" all the classes are imported. Modules are not included.
from tkinter import *
from tkinter import messagebox
import random
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    #Creating and populating lists with list comprehension.
    password_letters = [random.choice(letters) for char in range(nr_letters)]
    password_symbols = [random.choice(symbols) for char in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for char in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_numbers
    #The shuffle method reorganize the order of the list items.
    random.shuffle(password_list)

    for char in range(nr_symbols):
      password_list += random.choice(symbols)

    for char in range(nr_numbers):
      password_list += random.choice(numbers)

    random.shuffle(password_list)

    password = "".join(password_list)
    #The password entry will have the generated password as a placeholder.
    password_entry.insert(0, password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    entry_website = website.get()
    entry_email = email.get()
    entry_password = password_entry.get()
    #This message box returns a boolean value, if you press "ok", then the result will be true.

    if len(entry_website) == 0 or len(entry_password) == 0:
        messagebox.showinfo(message="Don't leave any fields empty!!!")
    else:
        is_ok =messagebox.askokcancel(title=entry_website, message=f"These are the details entered: \nEmail: {entry_email} \nPassword: {entry_password} \nIs it okey to save?")

    if is_ok:
        # If file doesn't exist, it will be created.
        # "a" means that it will be appended to the end of the file.
        data = open("data.txt", "a")
        data.write(f"{entry_website} | {entry_email} | {entry_password} \n")
        #With .delete(0, END) the previously prompted information in the entries will be cleaned.
        website.delete(0, END)
        password_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)
#Size of whole window.
canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
#X and Y position for image.
canvas.create_image(100, 100, image=logo_img)

canvas.grid(row=1, column=2)

label1 = Label(text="Website: ")
label1.grid(row=2, column=1)
website = Entry(width=35)
website.grid(row=2, column=2, columnspan=2)
#The cursor will be in the entry widget.
website.focus()

label2 = Label(text="Email/ Username: ")
label2.grid(row=3, column=1)
email = Entry(width=35)
email.grid(row=3, column=2, columnspan=2)
#The 0 means that you will start typing at the index 0.
email.insert(0, string="abogangsterbesode3@gmail.com")

label3 = Label(text="Password: ")
label3.grid(row=4, column=1)
password_entry = Entry(width=21)
password_entry.grid(row=4, column=2)

gen_pass = Button(text="Generate Password", command=generate_password)
gen_pass.grid(row=4, column=3)

add = Button(width=36, text="Add", command=save)
add.grid(row=5, column=2, columnspan=2)


window.mainloop()