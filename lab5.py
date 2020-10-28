from math import inf
start = float(input("start: "))
end = float(input("end: "))
step = float(input("step: "))

y = start

biggestD = -inf
smallestD = inf


print(" ---------------------------- " * 3)
print("|\tN\t|\tt\t|\ts\t|")
print(" -----------------------------" * 3)

while y < end:
    y += step
    print("|\t{}\t|".format(y))


print(" -----------------------------" * 3)
