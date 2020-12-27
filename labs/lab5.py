# Альбисурес дель Валье Хосе Альфредо
# ИУ7-15Б
# пятая лаборатория

x = float(input("Enter X: "))
iteration = int(input("Enter the iteration: "))
eps = float(input("Enter eps: "))
step = int(input("Enter the step: "))


divider = " ----------------" * 3

print(divider)
print("|{:^16}|{:^16}|{:^16}|".format("N", "t", "s"))
print(divider)

summa = 0
index = 0
iter_control = 0

while True:
    value = (-x) ** index
    summa += value

    if iter_control == index:
        if abs(value) > 10e+4:
            print("|{:^16}|{:^16.3e}|{:^16.3e}|".format(index + 1, value, summa))
        else:
            print("|{:^16}|{:^16}|{:^16}|".format(index + 1, value, summa))
        iter_control += step

    index += 1

    if abs(value) < eps:
        print(divider)
        print('the sequence converged in {} iteration.'.format(index))
        break
    if index > iteration:
        print(divider)
        print('the sequence didn\'t converge in {} iteration.'.format(iteration))
        break
