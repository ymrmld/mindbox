from math import pi, sqrt
from summa import sum_arg


def Square(*args):
    if int(sum_arg(*args)) == 3:
        for i in args:
            if type(i) == int or type(i) == float:
                continue
            else:
                raise ValueError('значения должны быть вещественными.')
        p = (args[0] + args[1] + args[2])/2
        if p > args[0] > 0 and p > args[1] > 0 and p > args[2] > 0:

            if (args[0] * args[0] + args[1] * args[1] == args[2] * args[2]):
                S = (p - args[0]) * (p - args[1])
                return f'S(прямоугольного треугольника) = {S}'
            elif (args[2] * args[2] + args[1] * args[1] == args[0] * args[0]):
                S = (p - args[2]) * (p - args[1])
                return f'S(прямоугольного треугольника) = {S}'
            elif (args[0] * args[0] + args[2] * args[2] == args[1] * args[1]):
                S = (p - args[0]) * (p - args[2])
                return f'S(прямоугольного треугольника) = {S}'
            else:
                S = sqrt(p * (p - args[0]) * (p - args[1]) * (p - args[2]))
                return f'S(треугольника) = {S}'
        raise ValueError('такого треугольника не существует.')

    if int(sum_arg(*args)) == 1:
        if (type(args[0]) == int or type(args[0]) == float) and args[0] > 0:
            S = pi * args[0] * args[0]
            return f'S(круга) = {S}'
        raise ValueError('радиус должен быть больше 0')

print(Square(1, 1, 1))
print(Square(1))
