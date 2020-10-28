

numbers = []

numbers = list(map(float, input("Initialize the list: ").split()))

while True:
    print("|== Menu =========|")
    print("|  1. Add a number\t|")
    print("|  2. Remove a number\t|")
    print("|  3. Clear list\t|")
    print("|  4. Find the max and Min values\t| ")
    print("|  7. Exit \t|")
    print("|===============|")
    print("| Current list: ", numbers)
    for index, number in numbers:
        print("\t", index + 1, ")" ,number)
    print("|===============| \n")
    

    action = int(input('enter which action: '))

    if 1 == action:
        new = float(input("enter the new number: "))
        position = int(input("enter its the position: "))
        numbers.insert(position, new)      
    if 2 == action:
        position = int(input("enter the position of the number to remove: "))
        numbers.remove(position)
    if 3 == action:
        numbers = []
    if 4 == action:
        maxi = 0
        mini = 0
        for index, number in numbers:
            if number > numbers[maxi]:
                maxi = index
            if number < numbers[mini]:
                mini = index
        print("Max value: ", maxi)
        print("Min value: ", maxi)
        
    
    if 8 == action:
        break
