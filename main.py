# 1 -----------------
def check1():
    out = []
    for num in range(256, 4096):
        orig = str(hex(num))[2:]
        res1 = orig[-1]
        res2 = orig[:-1]
        res = res1 + res2
        if num / int(res, 16) == 3:
            out.append(num)
    print(sum(out))


# 2 ---------------

def check2():
    x = 0
    res = []
    while True:
        x += 1
        xc = x
        y, z = 0, 1
        while xc > 0:
            y += 1
            ost = (xc % 14)
            z *= ost
            xc //= 14
        if y == 4 and z == 56:
            return x


# y, z = 0, 1
# x = 23339
# xc = x
# while xc > 0:
#     y += 1
#     ost = (xc % 14)
#     z *= ost
#     xc //= 14
# print(y)
# print(z)
# print(check())

# 2+ -------------------------------
def func():
    out = []
    for a in range(14):
        for b in range(14):
            for c in range(14):
                for d in range(14):
                    if a * b * c * d == 56:
                        out.append([a, b, c, d])
    return out


# 8711 = 1+ 1*14 + 7*14**2 + 8*14**3
# 23339
# print(func())

# 3 -------------------------------------
def check3():
    out = []
    for N in range(1, 1000 + 1):
        k = 1
        all_time = 0
        for i in range(1, 1000):
            if i % N == 0:
                k = 1
                if i > 1:
                    all_time += 15
            elif i % 10 == 0:
                k += 1

            all_time += k

        out.append([N, all_time])
    print(out)
    print(sorted(out, key=lambda x: x[1]))
