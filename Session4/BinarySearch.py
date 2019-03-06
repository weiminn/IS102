def bSearch(arr, low, high, n):

  mid = int((low + high)/2)

  print (mid, arr[mid])

  if n > arr[mid]:
    if(low < mid):
      return bSearch(arr, mid+1, high, n)
    else:
      return str("not found")
  elif n < arr[mid]:
    if(low < mid):
      return bSearch(arr, low, mid-1, n)
    else:
      return str("not found")
  else:
    return str("Found at " +  str(mid))

_arr = [4, 10, 22, 35, 36, 57, 65, 71, 79, 83, 87, 89, 90, 91, 93]

# result = bSearch(_arr, 0, len(_arr)-1, 35)
# print(result)