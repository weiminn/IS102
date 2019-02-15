def factorial(n):
    if (n <= 1):
        return n
    else :
        return n * factorial(n-1)

# print('factorial: ',factorial(3))

def fibonacci(arr, i, n):
    if (len(arr) < n):
        if(i == 1):
            return fibonacci([1], i+1, n)
        if(i == 2):
            return fibonacci([1, 1], i+1, n)
        else:
            toAdd = arr[len(arr)-1] + arr[len(arr)-2]
            arr.append(toAdd)
            # print(toAdd)
            return fibonacci(arr, i+1, n)
    else:
        return arr

# print('fibonacci', fibonacci([], 1, 100))

def isPalindrome(s):
    if len(s) > 1:
        if(s[0] == s[len(s)-1]):
            isPalindrome(s[1:len(s)-1])
        else:
            return False
    return True
print(isPalindrome("ffaff"))