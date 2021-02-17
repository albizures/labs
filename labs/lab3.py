
from math import sqrt, pow
print("Введите координаты трёх точек с запятой. координаты не могут быть равными или коллинеарными.")
Ax, Ay = map(int, input("Введите координаты точки А: ").split(","))  # Ввод координатов точки А
Bx, By = map(int, input("Введите координаты точки B: ").split(","))  # Ввод координатов точки В
Cx, Cy = map(int, input("Введите координаты точки C: ").split(","))  # Ввод координатов точки С

AB_x = Bx-Ax
BC_x = Cx-Bx
CA_x = Ax-Cx
AB_y = By-Ay
BC_y = Cy-By
CA_y = Ay-Cy

ab = abs(sqrt(pow((AB_x), 2) + pow((AB_y), 2)))
bc = abs(sqrt(pow((BC_x), 2) + pow((BC_y), 2)))
ac = abs(sqrt(pow((CA_x), 2) + pow((CA_y), 2)))

if ((ab + bc < ac) or (ab + ac < bc) or (bc + ac < ab)):
    print("Треугольник не существует")
else:
    print("Длина стороны AB= {:.7}".format(ab))
    print("Длина стороны BC= {:.7}".format(bc))
    print("Длина стороны AC= {:.7}".format(ac))

    if ab == max(ab, bc, ac):
        L = sqrt(bc * ac * ((bc+ac)**2-ab**2))/(bc + ac)
    elif bc == max(ab, bc, ac):
        L = sqrt(ab * ac * ((ab + ac)**2-bc**2))/(ab + ac)
    elif ac == max(ab, bc, ac):
        L = sqrt(bc*ab*((bc + ab)**2 - ac**2))/(bc + ab)
    print("Биссектриса L = {:5.4g}".format(L))

    if L == 0:
        print("Координаты являются коллинеарными, треугольник не существует")
    else:
        if ((ab > bc and ab > ac and (ab**2 > (bc**2 + ac**2) or abs(ab**2-(bc**2+ac**2) < 1e-5))) or (bc > ab and bc > ac and bc**2 > (ab**2+ac**2) or abs(bc**2-(ab**2+ac**2) < 1e-5))) or (ac > ab and ac > bc and (ac**2 > (bc**2+ab**2) or abs(ac**2-(bc**2+ab**2) < 1e-5))):  # Проверка на тупоугольный треугольник
            print("Треугольник является прямоугольным")
        else:
            print("Треугольник не является прямоугольным")

        Mx, My = map(float, input("Введите координаты точки которую хотите проверить: ").split(","))  # Ввод координатов точки которую нужно проверить
        a = float((Ax - Mx)*(By - Ay) - (Bx - Ax)*(Ay - My))
        b = float((Bx - Mx)*(Cy - By) - (Cx - Bx)*(By - My))
        c = float((Cx - Mx)*(Ay - Cy) - (Ax - Cx)*(Cy - My))

        if (a >= 0 and b >= 0 and c >= 0) or (a <= 0 and b <= 0 and c <= 0):  # Проверка на нахождения точки внутри или снаружи треугольника
            print("Точка находится внутри треугольника")

            AM_x = Mx - Ax
            BM_x = Mx - Bx
            CM_x = Mx - Cx
            AM_y = My - Ay
            BM_y = My - By
            CM_y = My - Cy

            AM_x = Mx - Ax
            AM_y = My - Ay
            BM_x = Mx - Bx
            BM_y = My - By
            CM_x = Mx - Cx
            CM_y = My - Cy

            AMxAB = (AM_x)*(AB_y) - (AM_y)*(AB_x)
            BMxBC = (BM_x)*(BC_y) - (BM_y)*(BC_x)
            CMxCA = (CM_x)*(CA_y) - (CM_y)*(CA_x)

            S_AMB = abs(AMxAB) / 2
            S_BMC = abs(BMxBC) / 2
            S_CMA = abs(CMxCA) / 2

            R_AB = 2*S_AMB / ab
            R_BC = 2*S_BMC / bc
            R_AC = 2*S_CMA / ac

            if R_AB >= R_BC and R_BC <= R_AC:
                print("Наименьшее расстояние между точкой и стороной: ", R_BC,)
            elif R_BC >= R_AB and R_AB <= R_AC:
                print("Наименьшее расстояние между точкой и стороной: ", R_AB,)
            elif R_AB >= R_AC and R_AC <= R_BC:
                print("Наименьшее расстояние между точкой и стороной: ", R_AC,)

        else:
            print("Точка не находится внутри треугольника")
