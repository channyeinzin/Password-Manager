import tkinter as tk
from tkinter import messagebox
import random

FONT = ("Courier", 10, "bold")

# Password Generator
def generate_password():
    letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    numbers = '0123456789'
    symbols = '!#$%&()*+'

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = [random.choice(letters) for _ in range(nr_letters)]
    password_list += [random.choice(symbols) for _ in range(nr_symbols)]
    password_list += [random.choice(numbers) for _ in range(nr_numbers)]

    random.shuffle(password_list)
    password = ''.join(password_list)

    password_input.delete(0, tk.END)
    password_input.insert(0, password)

# Save Password
def add():
    if not all([website_input.get(), username_input.get(), password_input.get()]):
        messagebox.showinfo(title="Incomplete Input", message="Please fill in all fields.")
        return

    entry_dict = {
        "website": website_input.get(),
        "username": username_input.get(),
        "password": password_input.get()
    }

    if messagebox.askyesno(title="Confirm Entry", message=f"{entry_dict}\nIs this okay?"):
        website_input.delete(0, tk.END)
        username_input.delete(0, tk.END)
        password_input.delete(0, tk.END)

        with open("data.txt", "a") as data_file:
            data_file.write(f"{str(entry_dict)},\n")

# UI Setup
window = tk.Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

# Logo
logo_img = tk.PhotoImage(file="logo.png")
logo_label = tk.Label(window, image=logo_img)
logo_label.grid(row=0, column=0, columnspan=3)

# Labels
labels = ["Website:", "Email/Username:", "Password:"]
for i, label_text in enumerate(labels, start=1):
    label = tk.Label(window, text=label_text, font=FONT)
    label.grid(row=i, column=0, sticky=tk.W, pady=(10, 0))

# Inputs
website_input = tk.Entry(window, font=FONT, width=35)
website_input.grid(row=1, column=1, columnspan=2, pady=(10, 0))
website_input.focus()

username_input = tk.Entry(window, font=FONT, width=35)
username_input.grid(row=2, column=1, columnspan=2, pady=(10, 0))

password_input = tk.Entry(window, font=FONT, width=20)
password_input.grid(row=3, column=1, pady=(10, 0))

# Buttons
gen_pass = tk.Button(window, text="Generate Password", font=FONT, command=generate_password)
gen_pass.grid(row=3, column=2, pady=(10, 0), padx=(10, 0))

add_button = tk.Button(window, text="Add", font=FONT, command=add)
add_button.grid(row=4, column=2, pady=(10, 0), padx=(10, 0))

window.mainloop()
