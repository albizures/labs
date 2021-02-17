from math import sqrt, pow

X1, Y1 = map(float, input("Введите координаты точки А: ").split(","))
X2, Y2 = map(float, input("Введите координаты точки B: ").split(","))
X3, Y3 = map(float, input("Введите координаты точки C: ").split(","))

d1 = sqrt(pow((X2 - X1), 2) + pow((Y2 - Y1), 2))
d2 = sqrt(pow((X3 - X2), 2) + pow((Y3 - Y2), 2))
d3 = sqrt(pow((X1 - X3), 2) + pow((Y1 - Y3), 2))

print("Длина стороны d1= {:.7}".format(d1))
print("Длина стороны d2= {:.7}".format(d2))
print("Длина стороны d3= {:.7}".format(d3))

if (d1 > d2 and d1 > d3 and d1**2 > (d2**2+d3**2)) or (d2 > d3 and d2 > d1 and d2**2 > (d3**2+d1**2)) or (d3 > d2 and d1 > d1 and d3**2 > (d2**2+d1**2)):  # Проверяем тупоугольный ли треугольник
    print("Треугольник является тупоугольным")
else:
    print("Треугольник не является тупоугольным")

X0, Y0 = map(float, input("Введите координаты точки которую хотите проверить: ").split(","))  # Вводим координаты точки которую нужно проверить
a = float((X1 - X0)*(Y2 - Y1) - (X2 - X1)*(Y1 - Y0))
b = float((X2 - X0)*(Y3 - Y2) - (X3 - X2)*(Y2 - Y0))
c = float((X3 - X0)*(Y1 - Y3) - (X1 - X3)*(Y3 - Y0))

if(a >= 0 and b >= 0 and c >= 0) or (a <= 0 and b <= 0 and c <= 0):  # Проверка условий
    print("Точка находится внутри треугольника")
else:
    print("Точка не находится внутри треугольника")
