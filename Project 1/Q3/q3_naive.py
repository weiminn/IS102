# q3.py
# Name:
# Section: 

# TODO: fill ttsum
# nums is a list of integers (e.g. [3, 0, 1, 0, -1, -2, 0])
# t is the target sum (e.g. 0)

# nums = [3, 0, 1, 0, -1, -2, 0]
def ttsum(nums, t):
  # your code here
  arr = []

  for f in range(len(nums)):
    for s in range(f, len(nums)):
      if nums[f]+nums[s] == t:
        if f != s:
          arr.append([f,s])

  for f in range(len(nums)):
    for s in range(f, len(nums)):
      for trd in range(s, len(nums)):
        if nums[f]+nums[s]+nums[trd] == t:
          if f != s != trd:
            arr.append([f,s,trd])
  # print(arr)
  return arr