import tkinter

window = tkinter.Tk()
window.minsize(width=300, height=100)
window.title("Mile to Km Converter")

unit1 = tkinter.Label(text="Miles")
unit1.grid(row=2, column=7)

unit2 = tkinter.Label(text="Km")
unit2.grid(row=3, column=7)

random_label = tkinter.Label(text="is equal to")
random_label.grid(row=3, column=4)

input = tkinter.Entry(width=10)
input.grid(row=2, column=6)


def button_clicked():
    num = input.get()
    new_num = float(num) * 1.60934
    calculated_num.config(text=f"{new_num}")


button = tkinter.Button(text="Calculate", command=button_clicked)
button.grid(row=4, column=6)

calculated_num = tkinter.Label(text="0")
calculated_num.grid(row=3, column=6)

window.mainloop()
