# Альбисурес дель Валье Хосе Альфредо
# ИУ7-15Б

# Лабораторная работа №9
# Написать программу, реализующую меню:
# 1. Ввод строки.
# 2. Настройка шифрующего алгоритма.
# 3. Шифрование строки, используя шифр Виженера.
# 4. Расшифровывание строки.

def shift(num, offset, size):
    return ((num + offset) % size)


def get_encrypted_code(code, key, start, end):
    code_char = code - range_start
    code_key = key - range_start
    size = range_end - range_start

    return start + shift(code_char, code_key, size)


def get_decrypted_code(code, key, start, end):
    code_char = code - range_start
    code_key = key - range_start
    size = range_end - range_start

    return start + shift(code_char, -code_key, size)


range_start = 32
range_end = 127
to_encrypt = ''
cipher_key = ''
encrypted = ''

while True:
    print('''
    ===========================
    1. Enter a line encrypt.
    2. Enter cipher key
    3. Encrypt line
    4. Decrypt the string
    5. Exit
    ''')

    option = input('> Enter action to perform: ')

    if option == '1':
        to_encrypt = input('> Enter the line: ')
    elif option == '2':
        cipher_key = input('> Enter the cipher key: ')
    elif option == '3':
        if to_encrypt == '':
            print('** Nothing to encrypt **')
            continue
        if cipher_key == '':
            print('** There is no key to encrypt with **')
            continue

        for index, char in enumerate(to_encrypt):
            encrypted += chr(get_encrypted_code(
                ord(char),
                ord(cipher_key[index % len(cipher_key)]),
                range_start, range_end
            ))
        print('Cipher key:', cipher_key)
        print('Line:', to_encrypt)
        print('Encrypted line:', encrypted)
    elif option == '4':
        if encrypted == '':
            print('** Nothing to decrypt **')
            continue
        if cipher_key == '':
            print('** There is no key to decrypt with **')
            continue

        decrypted = ''
        for index, char in enumerate(encrypted):
            decrypted += chr(get_decrypted_code(
                ord(char),
                ord(cipher_key[index % len(cipher_key)]),
                range_start, range_end
            ))
        print('Cipher key:', cipher_key)
        print('Line:', to_encrypt)
        print('Encrypted line:', encrypted)
        print('Decrypted line from encrypted version:', decrypted)
    elif option == '5':
        print("> Bye")
        break
