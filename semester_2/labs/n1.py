import tkinter as tk
from tkinter import ttk
import tkinter.font as tfont
import sys


def close(event):
    sys.exit()


def to_base5(num):
    result = ""
    while num:
        result = str(num % 5) + result
        num //= 5
    return result


class Btn(ttk.Button):
    def __init__(self, master=None, label=0, row_index=0, col_index=0, span=1):
        super().__init__(master=master, text=label, style='black/white.TButton')
        self.grid(row=row_index + 1, column=col_index, columnspan=span)

    def attach(self, on_click):
        self.bind('<Button>', on_click)


def create_interfae(window):
    string_var = tk.StringVar()

    def validate(*args):
        print(args, string_var.get())

        corrected = ''.join(filter(lambda c: c in '+-/*0123456789.', string_var.get()))
        string_var.set(corrected)

    string_var.trace('w', validate)
    input_entry = tk.Entry(window, textvariable=string_var)
    input_entry.grid(row=0, column=0, columnspan=4)

    font = tfont.Font(size=30)

    counter = 0
    buttons = [
        [7, 8, 9, '+'],
        [4, 5, 6, '-'],
        [1, 2, 3, '/'],
        [0, '.', 'AC', '*']
    ]

    def clear_input():
        input_entry.delete(0, 'end')

    def handler(value):
        input_text = input_entry.get()
        if str(value) in '+-/*0123456789.':
            clear_input()
            input_entry.insert(0, input_text + str(value))
        elif value == 'AC':
            clear_input()
        elif value == '=':
            clear_input()
            input_entry.insert(0, str(eval(input_text)))
        elif value == 'base5':
            clear_input()
            input_entry.insert(0, to_base5(eval(input_text)))

    def on_click(value):
        def event_handler(event):
            handler(value)

        return event_handler

    ttk.Style().configure('black/white.TButton', foreground='black', background='white')
    for row_index, row in enumerate(buttons):
        for col_index, button in enumerate(row):
            if button == None:
                continue

            btn = Btn(window, button, row_index + 1, col_index)
            btn.attach(on_click(button))

    btn_equal = Btn(window, '=', len(buttons) + 1, 0, 4)
    btn_equal.attach((on_click('=')))

    btn_convert = Btn(window, 'to 5 base', len(buttons) + 2, 0, 4)
    btn_convert.attach(on_click('base5'))


def main():
    window = tk.Tk()
    window.title("Calculator")
    window.bind('<Escape>', close)

    create_interfae(window)

    window.after(1, lambda: window.focus_force())
    window.lift()
    window.attributes("-topmost", True)

    menubar = tk.Menu(window)
    menu_app = tk.Menu(menubar, tearoff=0)
    menu_app.add_command(label="New")
    menu_app.add_command(label="New")
    menu_app.add_command(label="New")

    window.config(menu=menubar)
    window.mainloop()


if __name__ == '__main__':
    main()
