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
    'Lorem ipsum (1-2) dolor sit amet consectetur 2 **2 adipisicing elit',
    'quibusdam sed doloribus. Aut eligendi ipsum reprehenderit',
    'dolor reprehenderit 1+3/3 quibusdam sed asperiores, (6/2)**3 aut eligendi vis',
    'necessitatibus hic temporibus. Eos reiciendis pariatur recusandae',
    'reiciendis fugiat asperiores exercitationem nesciunt possimus voluptas nam quaerat',
    'platonem maiestatis, amet 1/(9**(1/2)) vis an. Albucius laboramus voluptatibus Ad eos scripta eleifend',
    'scripta hic, amet maiestatis vis an albucius nesciunt eos eligendi eleifend.'
]


def remove_extra_spaces(line):
    return ' '.join(filter(lambda word: word != '', line.split(' ')))


def right_pad(line, size):
    return f'{line:>{size}}'


def width_pad(line, size):
    words = line.split(' ')
    extra_space = size - len(line)
    if extra_space == 0:
        return line
    space_by = extra_space / len(words)
    space_each_word = 1 if space_by < 0 else ceil(space_by)
    new_words = []

    for index, word in enumerate(words):
        extra_space -= space_each_word
        if extra_space < 0:
            space_each_word += extra_space

        space = ' ' * space_each_word

        if index == len(words) - 1:
            new_words.append(space + word)
        else:
            new_words.append(word + ' ' + space)
    return ''.join(new_words)


def safe_number(num):
    try:
        if '.' in num or 'e' in num:
            return float(num)
        else:
            return int(num)
    except:
        return None


def find_inner_exp(exp):
    if not('(' in exp or ')' in exp):
        return exp

    final_exp = exp
    while '(' in final_exp or ')' in final_exp:
        open_index = final_exp.index('(')
        index = open_index + 1
        openings = 1

        while index < len(final_exp):
            char = final_exp[index]
            if char in '(':
                openings += 1
            if char in ')':
                openings -= 1
                if openings == 0:
                    inner_exp = final_exp[open_index + 1: index]
                    result = str(eval_exp(inner_exp))
                    final_exp = final_exp[:open_index] + result + final_exp[index + 1:]
                    break
            index += 1

    final_exp = final_exp.replace('+-', '-')
    final_exp = final_exp.replace('-+', '-')
    final_exp = final_exp.replace('++', '+')
    final_exp = final_exp.replace('--', '-')
    return final_exp


def eval_exp(raw):
    raw = raw.replace(' ', '')
    exp = find_inner_exp(raw)
    num = safe_number(exp)

    if type(num) in [int, float]:
        return num

    if '-' in exp:
        left, right = exp.split('-')
        if left[-1].isnumeric():
            return eval_exp(left) - eval_exp(right)
    if '+' in exp:
        left, right = exp.split('+')
        if (left[-1].isnumeric()):
            return eval_exp(left) + eval_exp(right)
    if '/' in exp:
        left, right = exp.split('/')
        return eval_exp(left) / eval_exp(right)
    if '**' in exp:
        left, right = exp.split('**')
        return eval_exp(left) ** eval_exp(right)
    if '*' in exp:
        left, right = exp.split('*')
        return eval_exp(left) * eval_exp(right)


def eval_exps(line):
    exps = get_exps(line)
    new_line = line
    for exp in exps:
        result = str(eval_exp(exp))
        if result != None:
            new_line = new_line.replace(exp, result + ' ')
    return new_line


def get_exps(line):
    exps = ['']
    for char in line:
        if char.isdigit() or char in '+-/*%()':
            exps[-1] += char
        elif char == ' ' and exps[-1] != '':
            exps[-1] += char
        else:
            if exps[-1] != '':
                exps.append('')

    return list(filter(lambda e: e != ' ' and e != '', exps))


def get_sentences(text):
    sentences = ['']
    for line in text:
        if '. ' in line:
            start, end = line.split('. ')
            sentences[-1] += ' ' + start + '.'
            sentences.append(end)
        else:
            sentences[-1] += ' ' + line
    return sentences


def main(text):
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
                text[index] = eval_exps(line)
            # input('> Press enter to continue')
        elif option == '7':
            letter = ''
            while len(letter) != 1:
                letter = input('Enter a letter: ')

            sentences = get_sentences(text)
            counter = {}
            for index, sentence in enumerate(sentences):
                counter[index] = 0
                words = sentence.split(' ')
                for word in words:
                    if word != '' and word[0] == letter:
                        counter[index] += 1

            sentence_index = 0
            for index in counter:
                if counter[sentence_index] < counter[index]:
                    sentence_index = index
            print(f'The sentences with the bigger number of words starting with the letter {letter} is:')
            print(f'\n    {sentences[sentence_index]}\n')
            input('> Press enter to continue')

        elif option == '8':
            break


if __name__ == "__main__":
    main(text)
