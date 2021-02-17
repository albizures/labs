# Лабораторная работа No 11
# Имитировать работу базы данных, используя бинарный файл.
# Запись содержит 3-4 поля. Например, запись 'книга' содержит поля 'автор', 'наименование', 'год издания'.
# Необходимо сделать меню:
# 1. Создание БД.
# 2. Добавление записи в БД.
# 3. Вывод всей БД.
# 4. Поиск записи по одному полю.
# 5. Поиск записи по двум полям.
# Для работы с текущей записью используется словарь.

import pickle
import os


def read_data(pathname):
    with open(pathname, 'rb') as file:
        while True:
            try:
                yield pickle.load(file)
            except EOFError:
                break


def dump_record(pathname, record):
    with open(pathname, 'ab') as file:
        pickle.dump(record, file)


def add_field(record, name):
    value = input(f'> Enter value for {name} property: ')
    record[name] = value


def search_in_record(record, query):
    for field, search in query:
        if not(search in record[field]):
            return False
    return True


def search_in_db(db, query):
    return list(filter(lambda record: search_in_record(record, query), db))


def wait(): return input('> Press enter to continue...')


field_names = ['author', 'name', 'year']
field_options = ', '.join(field_names)


def print_headers(headers, size):
    div = (' ' + ('-' * (size + 1))) * len(headers)
    for header in headers:
        print(f'|{header:^{size}}', end=' ')
    print('|')
    print(div)


def print_record(record, size):
    for field in record:
        print(f'|{record[field]:^{size}}', end=' ')
    print('|')


def print_data(headers, pathname):
    table_size = 20
    print_headers(headers, table_size)
    for record in read_data(pathname):
        print_record(record, table_size)


def print_results(headers, results):
    table_size = 20
    if len(results) == 0:
        print('Not records found')

    print(f'{len(results)} records found')

    print_headers(headers, table_size)
    for result in results:
        print_record(result, table_size)

    wait()


pathname = None
defaultPathname = 'db.pkl'

while True:
    print(f'''
    1. Creating a database.
    2. Add an entry.
    3. Print db
    4. Search for a record by one field.
    5. Search for a record in two fields.
    6. Exit
    ''')

    option = input('> Enter action to perform: ')

    if option == '1':
        pathname = input(f'> Enter pathname fo the db ({defaultPathname}): ') or defaultPathname
        if os.path.exists(pathname):
            anwser = input('There is already a db, do you want to reinitialize it? (Y/n): ')
            if anwser != 'n':
                os.remove(pathname)
        print('The db has been set')
        wait()
    elif pathname == None:
        print('No db set yet')
        wait()
    elif option == '2':
        new_record = {}

        for name in field_names:
            add_field(new_record, name)
        dump_record(pathname, new_record)
    elif option == '3':
        print_data(field_names, pathname)
    elif option == '4':
        field = None
        while not(field in field_names):
            field = input(f'> Enter the field to search into ({field_options}): ')
        search = input('> Enter your search: ')

        print_results(
            field_names,
            search_in_db(read_data(pathname), [[field, search]])
        )
    elif option == '5':
        query = []
        while len(query) != 2:
            field = None
            while not(field in field_names):
                field = input(f'> Enter the #{len(query) + 1} field to search into ({field_options}): ')
                search = input('> Enter your search: ')
            query.append([field, search])

        print_results(
            field_names,
            search_in_db(read_data(pathname), query)
        )

    if option == '6':
        break
