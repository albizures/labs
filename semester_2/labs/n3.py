import tkinter as tk
from tkinter import ttk, messagebox
import math
import matplotlib
import matplotlib.pyplot as plt
import numpy as np


def f(x):
    return math.sin(x) + 0.5


def d2f(x):
    return -math.sin(x)


def steff_by_steps(f, a, b, eps, steps):
    step = (b - a) / steps
    x1 = a

    results = []
    while (x1 < b):
        x2 = x1 + step
        f1 = f(x1)
        f2 = f(x2)
        if f1 * f2 <= 0:
            result = steff(f, x1, x2, eps)
            x, fx, iteration, error_code = result
            results.append((len(results) + 1, f"({x1};{x2})", x, str(fx), str(iteration), error_code))
        else:
            results.append((len(results) + 1, f"({x1};{x2})", '', '', '', 'Not Found'))
        x1 = x2
    return results


def steff(f, a, b, eps):
    x = a
    counter = 0
    while True:
        counter += 1
        fx = f(x)

        if(abs(fx) < eps):
            return x, fx, counter, ''

        x -= (fx**2) / (f(x + fx) - fx)

        if x >= b:
            return '', '', '', 'Not found',


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.bind('<Escape>', self.quit)
        self.columns = []
        self.init_ui()
        self.mainloop()

    def create_headers(self):
        tk.Label(self.table_frame, borderwidth=2, relief=tk.RIDGE, text=f"{'Root Number':^35}").grid(row=0, column=0, sticky=tk.NSEW)
        tk.Label(self.table_frame, borderwidth=2, relief=tk.RIDGE, text=f"{'[xi; xi+1]':^20}").grid(row=0, column=1, sticky=tk.NSEW)
        tk.Label(self.table_frame, borderwidth=2, relief=tk.RIDGE, text=f"{'x':^40}").grid(row=0, column=2, sticky=tk.NSEW)
        tk.Label(self.table_frame, borderwidth=2, relief=tk.RIDGE, text=f"{'f(x)':^40}").grid(row=0, column=3, sticky=tk.NSEW)
        tk.Label(self.table_frame, borderwidth=2, relief=tk.RIDGE, text="Number of iterations").grid(row=0, column=4, sticky=tk.NSEW)
        tk.Label(self.table_frame, borderwidth=2, relief=tk.RIDGE, text="Error code").grid(row=0, column=5, sticky=tk.NSEW)

    def clean_rows(self):
        for column in self.columns:
            for row in column:
                row.grid_forget()

    def show_result(self, results):
        self.clean_rows()

        for column in range(6):
            for row, result in enumerate(results):
                label = tk.Label(self.table_frame, text=result[column], borderwidth=2, relief=tk.RIDGE)
                label.grid(row=row+1, column=column, sticky=tk.NSEW)

    def init_ui(self):
        self.start_point = tk.StringVar(value="-4")
        self.end_point = tk.StringVar(value="2")
        self.steps = tk.StringVar(value="2")
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

        self.create_headers()

    def get_roots(self):
        a = float(self.start_point.get())
        b = float(self.end_point.get())
        eps = float(self.eps.get())
        steps = float(self.steps.get())

        if a > b:
            # swap
            a, b = b, a

        return steff_by_steps(f, a, b, eps, steps)

    def calculate(self):
        self.show_result(self.get_roots())

    def quit(self, *args):
        self.destroy()

    def show_graph(self):
        a = float(self.start_point.get())
        b = float(self.end_point.get())
        eps = float(self.eps.get())
        steps = float(self.steps.get())
        roots = self.get_roots()

        fig, ax = plt.subplots()
        xs = [x for x in np.linspace(a, b, 100)]
        ys = []
        prev_y = f(xs[0])
        prev_d2x = d2f(xs[0])

        for root in roots:
            if root[2] != '':
                plt.axvline(x=round(root[2], 2), color="green")

        for x in xs:
            y = f(x)
            ys.append(y)
            d2x = d2f(x)
            if (prev_d2x > 0 and d2x <= 0) or (prev_d2x < 0 and d2x >= 0):
                plt.axvline(x=x, color="red")
            prev_y = y
            prev_d2x = d2x

        ys = [f(x) for x in xs]
        ax.plot(xs, ys)

        ax.set(xlabel='x', ylabel='y')
        ax.grid()

        plt.show()


def main():
    App()


if __name__ == '__main__':
    main()
