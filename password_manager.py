from tkinter import *
from tkinter import messagebox
import random
import string

# ------------------- PASSWORD GENERATOR ----------------#

def generate_password():
    password_entry.delete(0, END)
    # "abcdefg....ABCDEF"
    letters = string.ascii_letters
    # 0123456789
    digits = string.digits
    symbols = ["!", "@", "#", "%", "^", "&"]

    nr_letters = random.randint(8, 10)
    nr_digits = random.randint(2, 4)
    nr_symbols = random.randint(2, 4)

    # password = []

    # for char in range(nr_letters):
    #     password.append(random.choice(letters))
    #FvuyCvFsC
    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    #264
    password_digits = [random.choice(digits) for _ in range(nr_digits)]
    #!^
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]

    password_list = password_letters + password_digits + password_symbols
    random.shuffle(password_list)
    password = "".join(password_list) # из массива собирает строку
                                        # ["a", "b"] -> "ab"
    password_entry.insert(0, password)
# -------------------- SAVE PASSWORD -------------------#

def save_data():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(password) == 0 or len(email) == 0:
        messagebox.showinfo(title="Ooops!", message="Не оставляйте поля пустыми")
    else:
        is_ok = messagebox.askokcancel(title="", message=f"Вы ввели {website}\n{password}\n{email}")
    #json JavaScript Object Notation
    # только когда мы произвели удачный ввод
    # is_ok = True
    if is_ok:
        with open("data.txt", "a") as data_file:
            data_file.write(f"{website} | {email} | {password}\n")
        website_entry.delete(0, END) # чтобы очистить поля для ввода
        password_entry.delete(0, END)

# --------------------- GUI ----------------------------#

window = Tk()
window.title("Password manager")
window.config(padx=20, pady=20)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# Labels

website_label = Label(text="Website")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username")
email_label.grid(row=2, column=0)
password_label = Label(text="Password")
password_label.grid(row=3, column=0)

# Entries
website_entry = Entry(width=35)
website_entry.grid(row=1, column=1)
email_entry = Entry(width=25)
email_entry.insert(0, "example@gmail.com")
email_entry.grid(row=2, column=1)
password_entry = Entry(width=25)
password_entry.grid(row=3, column=1)


# Buttons

generate_btn = Button(text="gen", width=7, command=generate_password)
generate_btn.grid(row=3, column=2)
add_btn = Button(text="add", width=35, command=save_data)
add_btn.grid(row=4, column=1, columnspan=2)

window.mainloop()
