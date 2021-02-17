# Альбисурес дель Валье Хосе Альфредо
# ИУ7-15Б

# Задача:
# Даны 2 текстовых файла in1.txt и in2.txt,
# в которые записаны неубывающие последовательности
# натуральных чисел (по одному числу в строке,
# значения чисел не превышают 3000).
# Не используя списки и методы сортировки,
# а также не считывая файлы в память целиком,
# сформировать файл out.txt, в который записать
# неубывающую последовательность чисел, содержащую
# все числа из исходных файлов.
# Далее сформировать файл out1.txt, в который записать
# римские представления чисел из файла out.txt, выравненные по центру.

roman_sybs = {
    1: 'I', 4: 'IV', 5: 'V', 9: 'IX',
    10: 'X', 40: 'XL', 50: 'L', 90: 'XC',
    100: 'C', 400: 'CD', 500: 'D', 900: 'CM',
    1000: 'M'
}


def read_file(filename):
    with open(filename) as file:
        while True:
            line = file.readline()
            if not line:
                break
            yield line


def to_roman(number):
    roman_number = ''
    for syb_value in reversed(roman_sybs):
        syb = roman_sybs[syb_value]
        for index in range(number // syb_value):
            roman_number += syb
            number -= syb_value
    return roman_number


def main():
    file = open('out1.txt', 'w')

    enum1 = read_file('in1.txt')
    enum2 = read_file('in2.txt')

    value1 = int(next(enum1))
    value2 = int(next(enum2))
    while True:
        try:
            if (value1 > value2):
                file.write(to_roman(value2))
                value2 = int(next(enum2))
            else:
                file.write(to_roman(value1))
                value1 = int(next(enum1))
            file.write('\n')
        except:
            break
    file.close()


if __name__ == '__main__':
    main()
