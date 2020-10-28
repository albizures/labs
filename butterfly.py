
x = float(input('введите x: '))
y = float(input('введите y: '))

insideFromTop = False
insideFromBottom = False

if -9 <= x <= -1:
	fg = (-(x + 9)**2) / 8 + 8

	if fg > y:
		insideFromTop = True

	if x <= -8:
		fg = 7 * (x + 8)**2 + 1
	else:
		fg = ((x + 1)**2) / 49

	insideFromBottom = fg < y

if 1 <= x <= 9:
	fg = (-(x - 9)**2) / 8 + 8
	if fg > y:
		insideFromTop = True

	if 8 <= x:
		fg = 7 * (x - 8)**2 + 1
	else:
		fg = ((x - 1)**2) / 49

	insideFromBottom = fg < y

if insideFromTop and insideFromBottom:
	print('внутри')
else:
	print('снаружи')
