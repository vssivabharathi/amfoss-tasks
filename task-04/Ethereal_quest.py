
xi = yi = zi = 0


for _ in range(int(input())):
    x, y, z = input( ).split()
    x = int(x)
    y = int(y)
    z = int(z)
    xi += x
    yi += y
    zi += z


if xi == yi == zi == 0:
    print("YES")
else:
    print("NO")
