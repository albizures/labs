from math import inf
start = float(input("start: "))
end = float(input("end: "))
step = float(input("step: "))

y = start

biggestD = -inf
smallestD = inf

ds = []

print(" ----------------------"*2)
print("|{:^22}|{:^22}|".format("y", "d"))
print(" ----------------------"*2)

while y <= end:
    d = y**5 - 7.9 * y**4 + 24.49 * y**3 - 37.074 * y**2 + 27.512 * y - 8.0042
    print("|{:^22.4f}|{:^22.4f}|".format(y, d))
    ds.append(d)
    if d > biggestD:
        biggestD = d
    if d < smallestD:
        smallestD = d
    y += step

print(" ----------------------"*2, '\n')

dRange = abs(biggestD - smallestD)
steps = 80
markEach = steps // 4
dStep = dRange / steps
numberHeader = '{:^7}'.format("")
lineHeader = '{:^11}'.format("")
values = ''
points = []

for index in range(0, steps + 1):
    num = smallestD + dStep * index
    points.append(num)
    if index % markEach == 0:
        sNum = '{:^10.1f}'.format(num)
        numberHeader += sNum + (' ' * (markEach - len(sNum)))
        lineHeader += '|'
    else:
        lineHeader += '-'


for i, d in enumerate(ds):
    for index, num in enumerate(points):
        nextNum = smallestD + dStep * (index + 1)
        if d >= num and d <= nextNum:
            padding = ' ' * index
            values = "{}{:>10.3f} |{}*\n".format(
                values, start + i * step, padding)
            break


print(numberHeader)
print(lineHeader + '-> y')
print(values + '{:>12}\n{:>12}'.format("˅", "x"))
