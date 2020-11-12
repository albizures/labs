
items = input("Initialize the list: ").split()
space = "|\t\t\t\t\t|"

while True:
    print("|== Current list =======================|")
    print(space)
    for index, item in enumerate(items):
        print("|    {}) {} \t\t\t\t|".format(index + 1, item))
    print(space)
    print("|== Menu ===============================|")
    print(space)
    print("|  1. Add an item\t\t\t|")
    print("|  2. Remove an item\t\t\t|")
    print("|  3. Clear list\t\t\t|")
    print("|  4. Find the max and min values\t|")
    print("|  5. Something\t\t\t|")
    print("|  6. Find rows with fewer vowels\t|")
    print("|  7. Exit \t\t\t\t|")
    print(space)
    print("|=======================================|\n")

    action = int(input('> Enter which action you want to perform: '))
    length = len(items)

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
                items.remove(position)
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
        try:
            for index, item in enumerate(items):
                number = float(item)
                if item > items[maxi]:
                    maxi = index
                if item < items[mini]:
                    mini = index
                print("Max value: ", items[maxi])
                print("Min value: ", items[mini])
        except:
            print("**It is not a list of only numbers**")
        input("> Enter to continue")

    elif 5 == action:
        print("lelele")
        input("> Enter to continue")
    elif 6 == action:
        print("werrwerwer")
        input("> Enter to continue")
    else:
        print("**Invalid action**")
        input("> Enter to continue")
