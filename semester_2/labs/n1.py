import math
import tkinter as tk
from tkinter import ttk, messagebox
import tkinter.font as tfont
import sys

about_message = """Эта программа позволяет выполнять основные математические операции и преобразовывать результат в 5-ю и обратно
Автор: Альбисурес дель валье Хосе Алфредо
Группа: ИУ7-25б
"""


def get_number_parts(num):
    decimals = 0
    str_num = str(num)
    if '.' in str_num:
        num, decimals = map(int, str(num).split('.'))
        decimals = decimals / 10
    return num, decimals


def to_base5(raw_num):
    result = ""
    str_num = str(raw_num)
    num, decimals = get_number_parts(raw_num)
    while num:
        result = str(num % 5) + result

        num //= 5
    if decimals > 0:
        result += '.'

    counter = 0
    while decimals:
        decimals *= 5
        num, decimals = get_number_parts(decimals)
        result = result + str(num)
        counter += 1
        if counter > 5:
            break

    return result


def to_base10(num):
    result = 0
    str_num = str(num)
    index = str_num.find('.')
    if index == -1:
        index = len(str_num)
    for char in str_num:
        if char == '.':
            continue
        index -= 1
        result += int(char) * 5**index
    return result


def is_operation(operation):
    return isinstance(operation, str) and operation in '+-/*'


def is_dot(operation):
    return isinstance(operation, str) and operation == '.'


class Btn(ttk.Button):
    def __init__(self, master=None, label=0, row_index=0, col_index=0, span=1):
        super().__init__(master=master, text=label, style='black/white.TButton')
        self.grid(row=row_index + 1, column=col_index, columnspan=span)

    def attach(self, on_click):
        self.bind('<Button>', on_click)


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Calculator")
        self.bind('<Escape>', self.quit)
        self.last_input = None

        self.init_ui()
        self.init_menus()

        self.after(1, lambda: self.focus_force())
        self.lift()
        self.mainloop()

    def init_ui(self):
        self.string_var = tk.StringVar()
        self.string_var.trace('w', self.validate)

        self.input_entry = tk.Entry(self, textvariable=self.string_var)
        self.input_entry.grid(row=0, column=0, columnspan=4)

        font = tfont.Font(size=30)

        buttons = [
            [7, 8, 9, '+'],
            [4, 5, 6, '-'],
            [1, 2, 3, '/'],
            [0, '.', 'AC', '*']
        ]

        ttk.Style().configure('black/white.TButton', foreground='black', background='white')
        for row_index, row in enumerate(buttons):
            for col_index, button in enumerate(row):
                if button == None:
                    continue

                btn = Btn(self, button, row_index + 1, col_index)
                btn.attach(self.on_click(button))

        btn_equal = Btn(self, '=', len(buttons) + 1, 0, 4)
        btn_equal.attach(self.on_click('='))

        btn_convert = Btn(self, 'to 5 base', len(buttons) + 2, 0, 2)
        btn_convert.attach(self.on_click('base5'))

        btn_convert = Btn(self, 'to 10 base', len(buttons) + 2, 2, 2)
        btn_convert.attach(self.on_click('base10'))

    def init_menus(self):
        menubar = tk.Menu(self)

        self.config(menu=menubar)

        menu_app = tk.Menu(menubar)
        menu_actions = tk.Menu(menubar)

        menu_app.add_command(label="About", command=self.show_info)
        menu_app.add_command(label="Exit", command=self.quit)

        menu_actions.add_command(label="Clear", command=self.clear_input)

        menubar.add_cascade(label="App", menu=menu_app)
        menubar.add_cascade(label="Input", menu=menu_actions)

    def validate(self, *args):
        corrected = ''.join(filter(lambda c: c in '+-/*0123456789.', self.string_var.get()))

        length = len(corrected)
        if length > 1:
            last = corrected[length - 1]
            second_last = corrected[length - 2]
            if (is_operation(last) and is_operation(second_last)) or (is_dot(last) and is_dot(second_last)):
                corrected = corrected[0: -1]
        elif is_operation(corrected):
            corrected = ''

        print(corrected)
        self.string_var.set(corrected)

    def clear_input(self):
        self.string_var.set('')

    def show_info(self):
        messagebox.showinfo("About", about_message)

    def change_handler(self, value):
        input_text = self.input_entry.get()
        final_input_value = input_text

        if is_operation(value):
            if is_operation(self.last_input) or not input_text.strip():
                return

        if is_dot(value):
            if is_dot(self.last_input) or not input_text.strip():
                return

        if str(value) in '+-/*0123456789.':
            self.clear_input()
            final_input_value = input_text + str(value)
        elif value == 'AC':
            self.clear_input()
            return
        elif value == '=':
            if not input_text.strip():
                return
            self.clear_input()
            final_input_value = str(eval(input_text))

        if value == 'base5' or value == 'base10':
            if len(input_text.strip()) == 0:
                messagebox.showerror("Error", "Nothing to convert")
                return

        if value == 'base5':
            final_input_value = to_base5(eval(input_text))
        elif value == 'base10':
            final_input_value = str(to_base10(eval(input_text)))

        self.last_input = value
        self.clear_input()
        self.string_var.set(final_input_value)

    def on_click(self, value):
        def event_handler(event):
            self.change_handler(value)

        return event_handler

    def quit(self, *args):
        self.destroy()


def main():
    App()


if __name__ == '__main__':
    main()
