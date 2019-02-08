def pt(n, k):
    if n == 0:
        return 1
    elif k == 0 or k == n:
        return 1
    else:
        return pt(n - 1, k - 1) + pt( n - 1, k)

print(pt(4, 2))