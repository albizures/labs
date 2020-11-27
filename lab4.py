# Альбисурес дель Валье Хосе Альфредо
# ИУ7-15Б
# четвертая лаборатория

from math import inf
start = float(input("start: "))
end = float(input("end: "))
step = float(input("step: "))

y = start

biggestValue = -inf
smallestValue = inf

print(" ----------------------"*2)
print("|{:^22}|{:^22}|".format("y", "d"))
print(" ----------------------"*2)


values = []
while y <= end:
    d = y**5 - 7.9 * y**4 + 24.49 * y**3 - 37.074 * y**2 + 27.512 * y - 8.0042
    print("|{:^22.4f}|{:^22.4f}|".format(y, d))
    values.append({
        'y': y,
        'd': d,
    })
    if d > biggestValue:
        biggestValue = d
    if d < smallestValue:
        smallestValue = d
    y += step

print(" ----------------------"*2, '\n')

ticks = int(input("Amout of ticks: "))

total = abs(smallestValue - biggestValue)
steps = 80
pointRange = total / steps
inBetweenTicks = steps // ticks

print(inBetweenTicks)
rangeStep = total / steps

points = []
numberHeader = '{:^7}'.format("")
lineHeader = '{:^11}'.format("")
rows = ""

for index in range(0, steps + 2):
    num = smallestValue + pointRange * index
    points.append(num)

    if index % inBetweenTicks == 0 and index < steps:
        sNum = '{:^10.2f}'.format(num)
        numberHeader += sNum + (' ' * (inBetweenTicks - len(sNum)))
        lineHeader += '|'
    else:
        lineHeader += '-'
lineHeader += '> y'

for value in values:
    y = value['y']
    d = value['d']
    rows = values = "{}{:>10.3f} ".format(rows, y)
    for index, point in enumerate(points):
        if len(points) - 1 != index:
            nextPoint = points[index + 1]
            if point <= d < nextPoint:
                rows += '*'
            elif point <= 0 < nextPoint:
                print(point, nextPoint)
                rows += '|'
            else:
                rows += ' '
    rows += '\n'


print(numberHeader)
print(lineHeader)
print(rows)
