

numbers = []

numbers = list(map(float, input("Initialize the list: ").split()))
space = "|\t\t\t\t\t|"

while True:
    print("|== Current list =======================|")
    print(space)
    for index, number in enumerate(numbers):
        print("|    {}) {} \t\t\t\t|".format(
            index + 1, number))
    print(space)
    print("|== Menu ===============================|")
    print(space)
    print("|  1. Add a number\t\t\t|")
    print("|  2. Remove a number\t\t\t|")
    print("|  3. Clear list\t\t\t|")
    print("|  4. Find the max and min values\t| ")
    print("|  7. Exit \t\t\t\t|")
    print(space)
    print("|=======================================|\n")

    action = int(input('> Enter which action you want to perform: '))
    length = len(numbers)

    if 1 == action:
        while True:
            new = float(input("> Enter the new number: "))
            position = int(input("> Enter the position: ")) - 1
            if position < 0 or position > length + 1:
                print("**The position is invalid**")
            else:
                numbers.insert(position, new)
                break
    elif 2 == action:
        while True:
            position = int(input("> Enter the position of the number to remove: "))
            if position < 0 or position > length:
                print("**The position is invalid**")
            else:
                numbers.remove(position)
                break

    elif 3 == action:
        numbers = []
        print("The list has been cleaned")
    elif 4 == action:
        maxi = 0
        mini = 0
        for index, number in enumerate(numbers):
            if number > numbers[maxi]:
                maxi = index
            if number < numbers[mini]:
                mini = index
        print("Max value: ", numbers[maxi])
        print("Min value: ", numbers[mini])
        input("> Enter to continue")

    elif 7 == action:
        break
    else:
        print("**Invalid action**")
        input("> Enter to continue")
