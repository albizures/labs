# Альбисурес дель Валье Хосе Альфредо
# ИУ7-15Б
# Рубежная работа
# 1) Время работы 1 час. 5 минут на отправление. Почта olvk@bmstu.ru
# 2) Исходный файл называется "in.txt" и никак иначе.
# 3) Используя редактор, создать текстовый файл in.txt.
# В исходном файле записаны строки,
#           в которых чередуются натуральные числа и строки.
# Написать программу, создающую текстовый файл out.txt, в котором вертикально выводятся строки, следующие после простых чисел.
# Файл считывается и записывается построчно, считывать содержимое всего файла в память запрещено.
#
# Например,
# исходный файл:
# 6
# ррр
# 3
# пппп
# 5
# аааааа
#
# результирующий:
# пппааааа
# пппааааа
# пппааааа
# пппааааа
#    ааааа
#    ааааа
#


def is_prime(num):
    if num > 1:
        for index in range(2, num):
            if (num % index) == 0:
                return False
        else:
            return True
    else:
        return False


lines = []

with open('in.txt') as in_file:
    current_number = None
    offset = 0
    for index, line in enumerate(in_file):
        if (len(line.strip()) == 0):
            continue

        if index % 2 == 1 and is_prime(current_number):
            text = line.replace('\n', '')
            for line_index, char in enumerate(text):
                char = text[line_index]
                if len(lines) - 1 < line_index:
                    lines.append(' ' * offset)

                lines[line_index] = lines[line_index] + (char * current_number)
            offset += current_number
        elif index % 2 == 0:
            current_number = int(line)


out_file = open('out.txt', 'w')

out_file.write('\n'.join(lines))
