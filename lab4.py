from math import inf
start = int(input("start: "))
end = int(input("end: "))
step = int(input("step: "))

y = start

biggestD = -inf
smallestD = inf

ds = []

print(" ---------------------------- "*2)
print("|\ty\t|\td\t|")
print(" ---------------------------- "*2)

while y <= end:
    d = y**5 - 7.9 * y**4 + 24.49 * y**3 - 37.074 * y**2 + 27.512 * y - 8.0042
    print("|{:^30f}|{:^30:1.3f}|".format(y, d))
    ds.append(d)
    if d > biggestD:
        biggestD = d
    if d < smallestD:
        smallestD = d
    y += step

print(" -----------------------------"*2, '\n')

dRange = abs(biggestD - smallestD)
steps = 60
markEach = steps // 4
dStep = dRange / steps
numberHeader = '\t'
lineHeader = '\t'
values = ''
points = []

for index in range(0, steps + 1):
    num = smallestD + dStep * index
    points.append(num)
    if index % markEach == 0:
        sNum = '{:1.3f}'.format(num)
        numberHeader += sNum + (' ' * (markEach - len(sNum)))
        lineHeader += '|'
    else:
        lineHeader += '-'


for i, d in enumerate(ds):
    for index, num in enumerate(points):
        nextNum = smallestD + dStep * (index + 1)
        if d >= num and d <= nextNum:
            padding = ' ' * index
            values = "{}{:1.3f}\t|{}*\n".format(
                values, start + i * step, padding)
            break


print(numberHeader)
print(lineHeader + '-> y')
print(values + '\t˅\n\tx')
