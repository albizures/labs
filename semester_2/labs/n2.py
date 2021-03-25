import tkinter as tk
import sys
import random
import time


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


class App(tk.Tk):
    def __init__(self, table):
        super().__init__()
        self.bind('<Escape>', self.quit)
        for i in range(len(table)):
            for j in range(len(table[i])):
                entry = tk.Label(self, width=40, text=table[i][j])
                entry.grid(row=i, column=j)

        self.mainloop()

    def quit(self, *args):
        self.destroy()


def timed_sort(arr):
    start_time = time.time()
    pyramid_sort(arr)
    return time.time() - start_time


def main():
    max_size = 10

    random_arr = [
        random.sample(range(0, 100), random.randint(1, max_size)),
        random.sample(range(0, 100), random.randint(1, max_size)),
        random.sample(range(0, 100), random.randint(1, max_size))
    ]

    ordered_arr = [
        pyramid_sort(random_arr[0]),
        pyramid_sort(random_arr[1]),
        pyramid_sort(random_arr[2]),
    ]

    reversed_arr = [
        list(reversed(ordered_arr[0])),
        list(reversed(ordered_arr[1])),
        list(reversed(ordered_arr[2])),
    ]

    table = [
        ["Ordered", timed_sort(random_arr[0]), timed_sort(random_arr[1]), timed_sort(random_arr[2])],
        ["Random", timed_sort(ordered_arr[0]), timed_sort(ordered_arr[1]), timed_sort(ordered_arr[2])],
        ["Reversed", timed_sort(reversed_arr[0]), timed_sort(reversed_arr[1]), timed_sort(reversed_arr[2])]
    ]

    App(table)


if __name__ == '__main__':
    main()
