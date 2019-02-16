from pythonds import Stack

b = '[({])}'

def checkBalance(string):
    s = Stack()
    for c in string:
        if c in b:
            if b.index(c) < 3:
                s.push(c)
            else:
                if s.isEmpty():
                    return False
                else:
                    if s.pop() != b[b.index(c)-3]:
                        return False
    return True

print(checkBalance('[ ]]]a + { b / ( c - d ) + e / (f + g ) } - h ]'))