# Альбисурес дель Валье Хосе Альфредо
# ИУ7-15Б

# Лабораторная работа No10
# Задан текст массивом строк. Текст -- фрагмент литературного произведения (5-7 предложений). Ни одна строка не оканчивается точкой кроме последней.
# Текст задается в программе, пользовательский ввод не требуется.
# Необходимо создать меню, выполняющее следующие действия:
# 1. Выравнивание текста по левому краю.
# 2. Выравнивание текста по правому краю.
# 3. Выравнивание текста по ширине.
# 4. Удаление заданного слова.
# 5. Замена одного слова другим во всем тексте.
# 6. Вычисление арифметического выражения.
# 7. Индивидуальное задание.
#       Найти предложение с максимальным количеством слов,
#       начинающихся на заданную букву.


from math import ceil
import re

text = [
    'Lorem ipsum (1-2) dolor sit amet consectetur ((2 ** 2)) adipisicing elit,',
    'quibusdam sed doloribus, aut eligendi ipsum reprehenderit',
    'dolor reprehenderit 1+3/3 quibusdam sed asperiores, (6/2)**3 aut eligendi vis',
    'necessitatibus hic temporibus? Eos reiciendis pariatur recusandae',
    'reiciendis fugiat asperiores, exercitationem nesciunt possimus voluptas nam quaerat?',
    'platonem maiestatis, amet vis an albucius laboramus voluptatibus Ad eos scripta eleifend',
    'scripta hic, amet maiestatis vis an albucius nesciunt eos eligendi eleifend.'
]


def remove_extra_spaces(line):
    return ' '.join(filter(lambda word: word != '', line.split(' ')))


def right_pad(line, size):
    return f'{line:>{size}}'


def width_pad(line, size):
    words = line.split(' ')
    extra_space = line_size - len(line)
    if extra_space == 0:
        return line
    space_by = extra_space / len(words)
    space_each_word = 1 if space_by < 0 else ceil(space_by)
    new_words = []
    print(extra_space, len(words), space_each_word, line)
    for index, word in enumerate(words):
        extra_space -= space_each_word
        if extra_space < 0:
            space_each_word += extra_space

        space = ' ' * space_each_word

        if index == len(words) - 1:
            new_words.append(space + word)
        else:
            new_words.append(word + ' ' + space)
    print(len(''.join(new_words)), size, space_each_word)
    return ''.join(new_words)


def evaluate_expression(expression):
    try:
        return str(eval(expression))
    except:
        return None


def evaluate_expressions(line):
    expressions = get_expressions(line)
    new_line = line
    for expression in expressions:
        result = evaluate_expression(expression)
        if result != None:
            new_line = new_line.replace(expression, result + ' ')
    return new_line


def get_expressions(line):
    expressions = ['']
    for char in line:
        if char.isdigit() or char in '+-/*%()':
            expressions[-1] += char
        elif char == ' ' and expressions[-1] != '':
            expressions[-1] += char
        else:
            if expressions[-1] != '':
                expressions.append('')

    return list(filter(lambda e: e != ' ' and e != '', expressions))


while(True):
    paragrah = '\n'.join(text)
    print(f'''
===========================
{paragrah}
===========================

    1. Align text to left
    2. Align text to right
    3. Align to the width
    4. Remove a word
    5. Replace all
    6. Calculate arithmetic expressions.
    7. Find sentence with the bigger number of words starting with a given letter.
    8. Exit
    ''')

    line_size = max(map(len, text))
    option = input('> Enter action to perform: ')

    if option == '1':
        text = list(map(remove_extra_spaces, text))
    elif option == '2':
        text = list(map(
            lambda line: right_pad(remove_extra_spaces(line), line_size),
            text
        ))
    elif option == '3':
        text = list(map(remove_extra_spaces, text))
        text = list(map(lambda line: width_pad(line, line_size), text))
    elif option == '4':
        to_replace = input('Enter the word to remove: ')
        for index, line in enumerate(text):
            new_words = []
            words = line.split(' ')
            for word in words:
                if word != to_replace:
                    new_words.append(word)

            new_line = ' '.join(new_words)
            if line != new_line:
                text[index] = new_line
                break
    elif option == '5':
        to_replace = input('Enter the word to replace: ')
        replace_with = input('Enter the word to replace it with: ')
        for index, line in enumerate(text):
            new_line = []
            words = line.split(' ')
            for word in words:
                if word == to_replace:
                    new_line.append(replace_with)
                else:
                    new_line.append(word)

            text[index] = ' '.join(new_line)
    elif option == '6':
        for index, line in enumerate(text):
            text[index] = evaluate_expressions(line)
        # input('> Press enter to continue')
    elif option == '7':
        letter = ''
        while len(letter) != 1:
            letter = input('Enter a letter: ')

        counter = {}
        for index, line in enumerate(text):
            counter[index] = 0
            words = line.split(' ')
            for word in words:
                if word != '' and word[0] == letter:
                    counter[index] += 1

        line_index = 0
        for index in counter:
            if counter[line_index] < counter[index]:
                line_index = index
        print(f'The line with the bigger number of words starting with the letter {letter} is:')
        print(f'\n    {text[line_index]}\n')
        input('> Press enter to continue')

    elif option == '8':
        break
