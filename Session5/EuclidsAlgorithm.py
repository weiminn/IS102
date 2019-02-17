def euclid(a, b):
    if b == 0:
        return a
    else:
        t = b
        b = a%b
        a = t
        return euclid(a, b)


print(euclid(17, 34))