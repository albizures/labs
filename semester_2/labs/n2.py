import tkinter as tk
from tkinter import ttk, messagebox
import tkinter.font as tfont
import sys
import random
import timeit


max_size = 10


def heapify(arr, index, length):
    left = 2 * index + 1
    right = left + 1
    if (left < length) and arr[left] > arr[index]:
        biggest = left
    else:
        biggest = index

    if right < length and arr[right] > arr[biggest]:
        biggest = right

    if biggest != index:
        arr[biggest], arr[index] = arr[index], arr[biggest]
        heapify(arr, biggest, length)


def pyramid_sort(arr):
    new_arr = arr.copy()
    length = len(new_arr)

    # make a heap
    for index in reversed(range(length // 2)):
        heapify(new_arr, index, length)

    for index in reversed(range(length)):
        # move sorted element to the end
        new_arr[index], new_arr[0] = new_arr[0], new_arr[index]
        # check the rest of the array
        heapify(new_arr, 0, index)

    return new_arr


def reverse(arr):
    new_arr = arr.copy()
    length = len(new_arr)
    for index in range(length // 2):
        temp = new_arr[index]
        opposite_index = -(index + 1)
        new_arr[index] = new_arr[opposite_index]
        new_arr[opposite_index] = temp

    return new_arr


def list_to_string(arr):
    return ','.join([str(val) for val in arr])


def get_times_list(arr):
    ordered = pyramid_sort(arr)
    ordered_reversed = list(reversed(arr))

    return [
        timeit.timeit(lambda: pyramid_sort(arr), number=1),
        timeit.timeit(lambda: pyramid_sort(ordered), number=1),
        timeit.timeit(lambda: pyramid_sort(ordered_reversed), number=1),
    ]


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.bind('<Escape>', self.quit)
        self.n = [
            random.sample(range(0, 100), random.randint(1, max_size)),
            random.sample(range(0, 100), random.randint(1, max_size)),
            random.sample(range(0, 100), random.randint(1, max_size)),
        ]

        self.init_ui()

        self.mainloop()

    def validate(self, var):
        corrected = ''.join(filter(lambda c: c in '0123456789, ', var.get()))
        var.set(corrected)

    def create_list_input(self, labe_text, value, row, command_update, command_generate):
        string_var = tk.StringVar()
        string_var.trace('w', lambda *args: self.validate(string_var))
        tk.Label(self.top_frame, text=labe_text + ": ").grid(row=row, column=0)

        entry = tk.Entry(self.top_frame, textvariable=string_var)
        entry.grid(row=row, column=1, columnspan=4)
        entry.delete(0, tk.END)
        entry.insert(0, str(value))

        update = ttk.Button(self.top_frame, text="Update", style='black/white.TButton', command=command_update)
        update.grid(row=row, column=5)

        generate = ttk.Button(self.top_frame, text="Generate", style='black/white.TButton', command=command_generate)
        generate.grid(row=row, column=6)

        return entry

    def init_ui(self):
        self.top_frame = tk.Frame(self)
        self.top_frame.grid(row=0, column=0, padx=20, pady=20)

        ttk.Style().configure('black/white.TButton', foreground='black')

        times = [
            get_times_list(self.n[0]),
            get_times_list(self.n[1]),
            get_times_list(self.n[2]),
        ]

        table = [
            ["", "N1", "N2", "N3"],
            ["Ordered:"],
            ["Random:"],
            ["Reversed:"]
        ]

        table_frame = tk.Frame(self)
        table_frame.grid(row=1, column=0, padx=20, pady=20)
        for i in range(len(table)):
            for j in range(len(table[i])):
                label = tk.Label(table_frame, text=table[i][j], borderwidth=2, relief=tk.RIDGE)
                label.grid(row=i, column=j, sticky=tk.NSEW)

        columns = []
        for i in range(len(times)):
            columns.append([])
            for j in range(len(times[i])):
                var = tk.StringVar()
                var.set(times[i][j])
                label = tk.Label(table_frame, textvariable=var, borderwidth=2, relief=tk.RIDGE)
                label.grid(row=i + 1, column=j + 1, sticky=tk.NSEW)
                columns[i].append(var)

        entry_list_1 = self.create_list_input(
            "N1",
            list_to_string(self.n[0]),
            0,
            lambda *args: self.update_list(columns[0], 0),
            lambda *args: self.generate_list(entry_list_1, 0),
        )
        entry_list_2 = self.create_list_input(
            "N2",
            list_to_string(self.n[1]),
            1,
            lambda *args: self.update_list(columns[1], 1),
            lambda *args: self.generate_list(entry_list_2, 1),
        )
        entry_list_3 = self.create_list_input(
            "N3",
            list_to_string(self.n[2]),
            2,
            lambda *args: self.update_list(columns[2], 2),
            lambda *args: self.generate_list(entry_list_3, 2),
        )

    def quit(self, *args):
        self.destroy()

    def generate_list(self, entry, index):
        self.n[index] = random.sample(range(0, 100), random.randint(1, max_size))
        entry.delete(0, tk.END)
        entry.insert(0, list_to_string(self.n[index]))

    def update_list(self, column, index):
        time = get_times_list(self.n[index])

        for i, entry in enumerate(column):
            entry.set(time[index])


def main():
    App()


if __name__ == '__main__':
    main()
