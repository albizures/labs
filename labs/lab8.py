# Альбисурес дель Валье Хосе Альфредо
# ИУ7-15Б
# восьмая лаборатория

def f(x):
    return x+5


def f_integral(x):
    return (x*(x+10)) / 2


def left(f, lower_bound, upper_bound, width):
    summ = 0
    x = lower_bound
    while x < upper_bound:
        summ += f(x)
        x += width
    return summ * width


def right(f, lower_bound, upper_bound, width):
    return left(f, lower_bound + width, upper_bound + width, width)


def print_table(title, rows):
    print()
    print(title)
    columns = len(rows[0])
    divider = (' ' + '-' * 18) * columns
    print(divider)
    for column in rows:
        for cell in column:
            if type(cell) == str:
                print('|{:^18}'.format(cell), end='')
            elif cell < 1e-3:
                print('|{:^18.3e}'.format(cell), end='')
            else:
                print('|{:^18.4f}'.format(cell), end='')

        print('|')
        print(divider)


lower_bound = float(input('Enter the lower bound (from): '))
upper_bound = float(input('Enter the upper bound (to): '))

divisions = (
    float(input('Enter the accuracy for the second time (rectagle width): ')),
    float(input('Enter the accuracy for the second time (rectagle width): '))
)

area = f_integral(upper_bound) - f_integral(lower_bound)

width = (
    (upper_bound - lower_bound) / divisions[0],
    (upper_bound - lower_bound) / divisions[1],
)

first_time = (
    left(f, lower_bound, upper_bound, width[0]),
    right(f, lower_bound, upper_bound, width[0])
)

second_time = (
    left(f, lower_bound, upper_bound, width[1]),
    right(f, lower_bound, upper_bound, width[1])
)

left_error = (
    abs(first_time[0] - area),
    abs(second_time[0] - area)
)

relative_left_error = (
    left_error[0] / area,
    left_error[1] / area
)


right_error = (
    abs(first_time[1] - area),
    abs(second_time[1] - area)
)

relative_right_error = (
    right_error[0] / area,
    right_error[1] / area
)

print('Area of the function in between [{}, {}] is {:.4f}'.format(lower_bound, upper_bound, area))

print_table('Values: ', [
    ['Method', 'First', 'Second'],
    ['Left side', first_time[0], second_time[0]],
    ['Right side', first_time[1], second_time[1]]
])

print_table('Error: ', [
    ['Method', 'First', 'Second'],
    ['Left side', left_error[0], left_error[1]],
    ['Right side', right_error[0], right_error[1]]
])

print_table('Relative error: ', [
    ['Method', 'First', 'Second'],
    ['Left side', relative_left_error[0], relative_left_error[1]],
    ['Right side', relative_right_error[0], relative_right_error[1]]
])

eps = float(input('Enter the precision: '))

parts = 2
result = 0
prev_result = 0
while True:
    width = (upper_bound - lower_bound) / parts
    prev_result = result
    result = left(f, lower_bound, upper_bound, width)
    if abs(result - prev_result) < eps:
        break
    parts *= 2


print('The precision is reach with {} partitions '.format(parts))
print('And the result is: {}'.format(result))
