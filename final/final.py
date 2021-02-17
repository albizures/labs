# Альбисурес дель Валье Хосе Альфредо
# ИУ7-15Б


# Даны два файла: in1.txt и in2.txt, в каждом по N строк.
# В первом файле записаны номера строк второго файла от 1
# до N (не по порядку), номера не повторяются.
# В каждой строке второго файла записаны 2 натуральных
# числа через пробел.
# Требуется вывести в файл out.txt суммы чисел
# из файла in2.txt, каждую с новой строки,
# по порядку в соответствии с номерами,
# определёнными в файле in1.txt. Выводить только те суммы,
# в которых количество чётных цифр больше, чем нечётных.
# Файлы в память целиком не считывать, числовой тип к
# строковому для подсчёта количества чётных цифр
# не приводить.

def read_line(line):
    file = open('in2.txt', 'r')

    for index, value in enumerate(file):
        if index == line:
            return value


def parse_line(line):
    left, right = line.split()
    return (int(left), int(right))


def get_digits(number):
    if number < 10:
        return [number]

    digits = []
    residual = number
    while residual >= 10:
        digits.append(residual % 10)
        residual = residual // 10

    digits.append(residual)
    digits.reverse()
    return digits


def main():
    in1 = open('in1.txt')
    output = open('output.txt', 'w')

    for i, line in enumerate(in1):
        number_line = int(line)
        result = sum(parse_line(read_line(number_line)))
        digits = get_digits(result)
        evens = 0
        odds = 0

        for digit in digits:
            if digit % 2 == 0:
                evens += 1
            else:
                odds += 1
        print(f'Result of line {number_line} is: {digits}')
        if evens > odds:
            output.write(str(result))
            output.write('\n')


if __name__ == "__main__":
    main()
