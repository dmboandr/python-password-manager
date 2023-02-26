from tkinter import *
from tkinter import messagebox
import random
import string
import json

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
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(password) == 0 or len(email) == 0:
        messagebox.showinfo(title="Ooops!", message="Не оставляйте поля пустыми")
    else:
        #json.dump() - запись в json
        #json.update() - обновить json
        #json.load() - чтение из json
        # сперва читаем содержимое файла
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file)
        else:
            # содержимое файла обновляем
            data.update(new_data)
            # записываем обновленный файл
            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, END)  # чтобы очистить поля для ввода
            password_entry.delete(0, END)

# --------------------- FIND WEBSITE ----------------------------#

def find_password():
    website = website_entry.get()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="Файл не создан")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email {email}\n"
                                                   f"Password: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"Нет информации о "
                                                       f"вебсайте {website}")
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

search_button = Button(text="search", command=find_password)
search_button.grid(row=1, column=2)
generate_btn = Button(text="gen", width=7, command=generate_password)
generate_btn.grid(row=3, column=2)
add_btn = Button(text="add", width=35, command=save_data)
add_btn.grid(row=4, column=1, columnspan=2)

window.mainloop()
