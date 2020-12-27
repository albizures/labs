# Альбисурес дель Валье Хосе Альфредо
# ИУ7-15Б
# шестая лаборатория

items = input("Initialize the list: ").split()
listOfNumber = True
numbers = []

space = "|{:<39}|".format("")
vowels = 'aeiou'

while True:
    print("|== Current list =======================|")
    print(space)
    for index, item in enumerate(items):
        print("|    {}) {:<32}|".format(index + 1, item))
    print(space)
    print("|== Menu ===============================|")
    print(space)
    print("|  {:<37}|".format('1. Add an item'))
    print("|  {:<37}|".format('2. Remove an item'))
    print("|  {:<37}|".format('3. Clear list'))
    print("|  {:<37}|".format('4. Find the max and min values'))
    print("|  {:<37}|".format('5. Prime negative numbers'))
    print("|  {:<37}|".format('6. Find string with fewer vowels'))
    print("|  {:<37}|".format('7. Exit'))
    print(space)
    print("|=======================================|\n")

    action = int(input('> Enter which action you want to perform: '))
    length = len(items)

    try:
        numbers = list(map(int, items))
    except:
        listOfNumber = False

    if action == 7:
        print("Exiting the program")
        break
    if 1 == action:
        while True:
            new = input("> Enter the new item: ")
            position = int(input("> Enter the position: ")) - 1
            if position < 0 or position > length + 1:
                print("**The position is invalid**")
            else:
                items.insert(position, new)
                break
    elif 2 == action:
        while True:
            position = int(input("> Enter the position of the item to remove: "))
            if position < 0 or position > length:
                print("**The position is invalid**")
            else:
                del items[position - 1]
                break

    elif 3 == action:
        items = []
        print("The list has been cleaned")
        input("> Enter to continue")
    elif length <= 0:
        print("**The list is empty**")
        input("> Enter to continue")
    elif 4 == action:
        maxi = 0
        mini = 0

        if listOfNumber:
            for index, number in enumerate(numbers):
                if number > numbers[maxi]:
                    maxi = index
                if number < numbers[mini]:
                    mini = index
            print("Max value: ", numbers[maxi])
            print("Min value: ", numbers[mini])
        else:
            print("**It is not a list of only numbers**")

        input("> Enter to continue")
    elif 5 == action:
        if listOfNumber:
            primeNumbers = []
            for number in numbers:
                if number > 0:
                    continue
                num = abs(number)
                if num > 1:
                    isPrime = True
                    for i in range(2, num//2 + 1):
                        if (num % i) == 0:
                            isPrime = False
                            break
                    if isPrime:
                        primeNumbers.append(number)
                else:
                    primeNumbers.append(number)
            print(primeNumbers)
        else:
            print("**It is not a list of only numbers**")
        input("> Enter to continue")
    elif 6 == action:
        withLessVowels = []
        for item in items:
            vowelCounter = 0
            for char in item:
                if char in vowels:
                    vowelCounter += 1
            consonantsCounter = len(item) - vowelCounter
            if consonantsCounter < vowelCounter:
                withLessVowels.append(item)
        print(withLessVowels)
        input("> Enter to continue")
    else:
        print("**Invalid action**")
        input("> Enter to continue")
