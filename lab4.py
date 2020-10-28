from math import inf
start = 1.4
end = 2.2
step= 0.025

y = start

biggestD = -inf
smallestD = inf 

ds = []

print(" ------- -------")
print("|   y   |   d   |")
print(" ------- -------")

while y <= end:
    d = y**5 - 7.9 * y**4 + 24.49 * y**3 - 37.074 * y**2 + 27.512 * y - 8.0042
    print("| {:2.3f} | {:2.3f} |".format(y, d))
    ds.append(d)
    if d > biggestD:
        biggestD = d
    if d < smallestD:
        smallestD = d
    y += step

print(" ------- -------\n")

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
            padding = ' ' * (index - 1)
            values = "{}{:1.3f}\t|{}x\n".format(values, start + i * step, padding)
            break;
        

print(numberHeader)
print(lineHeader + '-> y')
print(values + '\t˅\n\tx')

    
