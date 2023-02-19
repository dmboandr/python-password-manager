import tkinter


def km_to_miles():
    km = float(km_to_miles_entry.get())
    miles = round((km / 1.609), 2)
    result_label.config(text=f"{miles}")


window = tkinter.Tk()
window.title("km to miles calculator")
window.minsize(width=150, height=75)
# padding x, padding y
window.config(padx=20, pady=20)

km_label = tkinter.Label(text="Enter kilometers")
km_label.grid(row=0, column=0)

km_to_miles_entry = tkinter.Entry(width=5)
km_to_miles_entry.grid(row=0, column=1)

miles_label = tkinter.Label(text="= miles")
miles_label.grid(row=0, column=2)

calculate_button = tkinter.Button(text="Calculate", command=km_to_miles)
calculate_button.grid(row=1, column=1)

result_label = tkinter.Label(text="0")
result_label.grid(row=1, column=2)

window.mainloop()
