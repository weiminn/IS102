def factorial(n):
    if (n <= 1):
        return n
    else :
        return n * factorial(n-1)

print('factorial: ',factorial(3))

def fibonacci(arr, n):
    if (n > 0):
        toAdd = arr[len(arr)-1] + arr[len(arr)-2]
        arr.append(toAdd)
        print(toAdd)
        return fibonacci(arr, n-1)
    else:
        return arr

print('fibonacci', fibonacci([0, 1], 100))