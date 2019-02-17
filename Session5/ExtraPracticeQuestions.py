def repeatString(s, n):
    if n > 0:
        return s + repeatString(s, n-1)
    else:
        return ''

# print(repeatString('Apple', 5))

def sum(n):
    if n > 0:
        return n + sum(n-1)
    else:
        return 0

# print(sum(8))

def reverse(a):
    if len(a) == 0:
        return []
    else:
        return [a[len(a)-1]] + reverse(a[:len(a)-1])

# print(reverse([1, 2, 3, 4]))
