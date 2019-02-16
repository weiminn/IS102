from pythonds import Stack

def dijkstra(a, b):
    s = Stack()
    while a!=b:
        if a > b:
            s.push(b)
            a = a-s.pop()
        elif b > a:
            s.push(a)
            b = b-s.pop()
    return a, b

print(dijkstra(26, 32))