from pythonds import Stack

class QueueS:
    s1 = Stack()
    s2 = Stack()

    def __init__(self):
        print('Stack Q initiated')

    def nQ(self, x):
        self.s1.push(x)

    def dQ(self):
        while not self.s1.isEmpty():
            self.s2.push(self.s1.pop())

        toReturn = self.s2.pop()
        
        while not self.s2.isEmpty():
            self.s1.push(self.s2.pop())

        return toReturn

sq = QueueS()
sq.nQ(1)
sq.nQ(2)
sq.nQ(3)

print(sq.dQ(), sq.dQ(), sq.dQ())
