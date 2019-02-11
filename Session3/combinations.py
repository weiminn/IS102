def start(arr):
    "O(n) time"
    correct = ['ON', 'OFF', 'ON', 'OFF']
    n = len(correct)

    for i in range(n):
        if arr[i] != correct[i]:
            return False
    return True

# print(permutations(['ON', 'ON', 'ON', 'OFF']))

def combs():
    _arr = []
    for i in range(0,2):
        for j in range(0, 2):
            for k in range(0, 2):
                for l in range(0, 2):
                    _arr.append([i, j, k, l])
                    print(i, j, k, l)
combs()