a, b, c = input().split()
a = float(a)
b = float(b)
c = float(c)
D = (b ** 2) - (4 * a * c)
if a == 0:
    if b == 0 and c == 0:
        print(-1)
    if b == 0 and c != 0:
        print(0)
    if b != 0:
        x = -c / b
        print(1)
        print(round(x, 6))
else:
    if D > 0:
        x1 = ((-b) - (D ** 0.5)) / (2 * a)
        x2 = ((-b) + (D ** 0.5)) / (2 * a)
        if x1 < x2:
            x2, x1 = x1, x2
        print(2)
        print(round(x2, 6))
        print(round(x1, 6))

    elif D == 0:
        x = (-b) / (2 * a)
        print(1)
        print(round(x, 6))
    elif D < 0:
        print(0)



