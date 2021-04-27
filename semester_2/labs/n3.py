import tkinter as tk
from tkinter import ttk, messagebox
import math
import matplotlib
import matplotlib.pyplot as plt
import numpy as np


def f(x):
    return x**3 + x**2 - 4 * x


def df(x):
    return 3 * x**2 + 2 * x - 4


def steff(f, a, b, eps):
    x = b
    counter = 0
    while a < x:
        fx = f(x)

        if fx == 0 or abs(fx) < eps:
            return str(x), f"({a};{b})", str(x), str(fx), str(counter), '',

        gx = f(x + fx) / fx - 1
        x = x - (fx / gx)
        counter += 1
    else:
        return '', f"({a};{b})", str(x), str(fx), str(counter), 'Not found',


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.bind('<Escape>', self.quit)

        self.init_ui()
        self.mainloop()

    def create_result_col(self, text, column):
        value = tk.StringVar()
        tk.Label(self.table_frame, borderwidth=2, relief=tk.RIDGE, text=text).grid(row=0, column=column, sticky=tk.NSEW)
        label = tk.Label(self.table_frame, textvariable=value, borderwidth=2, relief=tk.RIDGE)
        label.grid(row=1, column=column, sticky=tk.NSEW)

        return value

    def init_ui(self):
        self.start_point = tk.StringVar(value="-3")
        self.end_point = tk.StringVar(value="2")
        self.steps = tk.StringVar(value="100")
        self.eps = tk.StringVar(value="1e-10")

        ttk.Style().configure('black/white.TButton', foreground='black')

        input_frame = tk.Frame(self)
        input_frame.grid(row=0, column=0)

        tk.Label(input_frame, text="Start point").grid(row=0, column=0)
        tk.Entry(input_frame, textvariable=self.start_point).grid(row=0, column=1)

        tk.Label(input_frame, text="End point").grid(row=1, column=0)
        tk.Entry(input_frame, textvariable=self.end_point).grid(row=1, column=1)

        tk.Label(input_frame, text="Steps").grid(row=2, column=0)
        tk.Entry(input_frame, textvariable=self.steps).grid(row=2, column=1)

        tk.Label(input_frame, text="Eps").grid(row=3, column=0)
        tk.Entry(input_frame, textvariable=self.eps).grid(row=3, column=1)

        ttk.Button(input_frame, style='black/white.TButton', text="Calculate", command=self.calculate).grid(row=2, column=3)
        ttk.Button(input_frame, style='black/white.TButton', text="Show Graph", command=self.show_graph).grid(row=2, column=4)

        self.table_frame = tk.Frame(self)
        self.table_frame.grid(row=1, column=0, padx=20, pady=20)

        self.root_number = self.create_result_col(text=f"{'Root Number':^35}", column=0)
        self.section = self.create_result_col(text=f"{'[xi; xi+1]':^20}", column=1)
        self.x = self.create_result_col(text=f"{'x':^40}", column=2)
        self.f_x = self.create_result_col(text=f"{'f(x)':^40}", column=3)
        self.iterations = self.create_result_col(text="Number of iterations", column=4)
        self.error = self.create_result_col(text="Error code", column=5)

    def calculate(self):
        a = float(self.start_point.get())
        b = float(self.end_point.get())
        eps = float(self.eps.get())
        steps = float(self.steps.get())

        if a > b:
            # swap
            a, b = b, a

        root_number, section, x, fx, iteractions, error = steff(f, a, b, eps)
        self.root_number.set(root_number)
        self.section.set(section)
        self.x.set(x)
        self.f_x.set(fx)
        self.iterations.set(iteractions)
        self.error.set(error)

    def quit(self, *args):
        self.destroy()

    def show_graph(self):
        a = float(self.start_point.get())
        b = float(self.end_point.get())
        eps = float(self.eps.get())
        steps = float(self.steps.get())

        fig, ax = plt.subplots()
        xs = [x for x in np.linspace(a, b, 100)]
        ys = []
        prev_y = f(xs[0])
        for x in xs:
            y = f(x)
            ys.append(y)

            if prev_y * y < 0:
                plt.axvline(x=x, color="red")
            prev_y = y

        ys = [f(x) for x in xs]
        ax.plot(xs, ys)

        ax.set(xlabel='x', ylabel='y')
        ax.grid()

        plt.show()


def main():
    App()


if __name__ == '__main__':
    main()
