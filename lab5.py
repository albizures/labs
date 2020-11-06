value = float(input("Value: "))
steps = int(input("steps: "))

print(" ---------------" * 3)
print("|\tN\t|\tt\t|\ts\t|")
print(" ---------------" * 3)

sum = 0
for i in range(0, steps):
    current = value ** i
    sum += current * (1 if i % 2 == 0 else -1)
    print("|\t{}\t|\t{}\t|\t{}\t|".format(i + 1, current, sum))

print(" ---------------" * 3)
