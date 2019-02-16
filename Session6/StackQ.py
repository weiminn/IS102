from pythonds import Queue

class StackQ:
    q1 = Queue()

    def __init__(self):
        print('Stack Q initiated')

    def push(self, x):
        self.q1.enqueue(x)

    def pop(self):
        q2 = Queue()
        n = 0
        x = None

        while not self.q1.isEmpty():
            x = self.q1.dequeue()
            # print(x)
            q2.enqueue(x)
            n += 1
            
        for i in range(n-1):
            self.q1.enqueue(q2.dequeue())
            
        return x

sq = StackQ()
sq.push(1)
sq.push(2)
sq.push(3)
sq.push(4)
sq.push(5)

print(sq.pop())
print(sq.pop())
print(sq.pop())
print(sq.pop())
print(sq.pop())
