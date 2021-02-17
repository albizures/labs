from math import pow, sqrt

a = float(input('Введите сторону тетраэдра: '))
if a <= 0:
    print("Сторона не может быть отрицательной или нулевой")
else:
    v = ((sqrt(2)) / 12) * pow(a, 3)
    s = pow(a, 2) * sqrt(3)
    h = a * sqrt(2/3)
    r = a * (sqrt(6)/12)
    R = a * (sqrt(6)/4)
    print("Обьём тетраэдра: {:.7g}".format(v))
    print("Площадь поверхности: {:.7g}".format(s))
    print("Радиус описанной сферы: {:.7g}".format(R))
    print("Радиус вписанной сферы: {:.7g}".format(r))
    print("Высота тетраэра: {:.7g}".format(h))
