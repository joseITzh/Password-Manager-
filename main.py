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
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    new_data = {
        website: {
            "email": email,
            "password": password
        }}

    #This message box returns a boolean value, if you press "ok", then the result will be true.
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(message="Don't leave any fields empty!!!")
    else:
        #"a" means that it will be appended to the end of the file.
        #When you open a file with "r" mode, the file will be read.
        #When you open a file in "w" mode, if the file doesn't exist, it will be created.

        #To add information to a json file you need to read it first and then you can update it.

        #Open the file.
        try:
            # Try opening the file and try reading the data inside.
            with open("data.json", "r") as data_file:
                # Reading old data.
                data = json.load(data_file)

        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                # Saving updated data
                # We are dumping the new_data (first argument) nested dictionary.
                # The second argument is the data file we want to put it into.
                json.dump(new_data, data_file, indent=4)

        else:
            # If file was found, we will get hold of the data we got on the try block.
            # Updating old data with new data.
            data.update(new_data)

            with open("data.json", "w") as data_file:
                # Saving updated data
                # We are dumping the new_data (first argument) nested dictionary.
                # The second argument is the data file we want to put it into.
                json.dump(data, data_file, indent=4)

        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)

# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    website = website_entry.get()
    try:
        with open("data.json") as data_file:
            #If we print "data", we get a nested dictionary.
            data = json.load(data_file)
    except FileNotFoundError:
        #In case there is no json file.
        messagebox.showinfo(title="Error", message="No Data File Found.")
    else:
        #Checking if the key is in the dictionary.
        if website_entry in data:
            #It is a nested dictionary... looks like this when you access it...
            email = data[website_entry]["email"]
            password = data[website_entry]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email} \nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} exists.")
    # ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)
#Size of whole window.
canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
#X and Y position for image.
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

#Labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

#Entries
website_entry = Entry(width=21)
website_entry.grid(row=1, column=1)
#The cursor will be in the entry widget.
website_entry.focus()
email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
#The 0 means that you will start typing at the index 0.
email_entry.insert(0, "angela@gmail.com")
password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

# Buttons
search_button = Button(text="Search", width=13, command=find_password)
search_button.grid(row=1, column=2)
generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(row=3, column=2)
add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
