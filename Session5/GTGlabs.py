arr = [62, 77, 18, 48, 64, 45, 34, 88, 32, 33, 54, 53, 65, 23, 23, 12, 62, 77, 18, 48, 64, 45, 34, 88, 32, 33, 54, 53, 65, 23, 23, 12]

def findMax(_arr, i, max = 0):
    if _arr[i] > max:
        max = _arr[i]
        
    if i == len(_arr)-1:
        return max
    else:
        return findMax(_arr, i+1, max)

# print(findMax(arr, 0))

# Describe a recursive function for computing the nth Harmonic number,such that Hn = ∑n i=1 1/i
def harmonic(n):
    if(n == 1):
        return 1
    else:
        return (1/n) + harmonic(n-1)
print(harmonic(5))