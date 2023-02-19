# GUI - graphical user interface
import tkinter

# Создание окна
window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

# Создание текста (Label)
my_label = tkinter.Label(text="I am Label", font=("Arial", 12, "italic"))
# my_label.pack(side="top")
my_label.grid(row=0, column=0)
my_label["text"] = "New Text"
my_label.config(text="New Text2")

my_label_2 = tkinter.Label(text="Another label")
my_label_2.grid(row=1, column=1)

# Кнопка (Button)

def button_clicked():
    print("I got clicked")
    print(entry.get())

button = tkinter.Button(text="Click me", command=button_clicked)
button.grid(row=2, column=2)

# Поле ввода (Entry) edit

entry = tkinter.Entry(width=7)
entry.grid(row=2, column=3)

# Способы размещения элементов на экране
# 1. pack() - размещение элементов один за другим
# 2. place() - размещение элементов по координатам x, y
# 3. grid() - размещение элементов в таблице

window.mainloop()

