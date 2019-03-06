# q3.py
# Name: Wei Minn
# Section: G5

# TODO: fill ttsum
# nums is a list of integers (e.g. [3, 0, 1, 0, -1, -2, 0])
# t is the target sum (e.g. 0)

# nums = [3, 0, 1, 0, -1, -2, 0]
def ttsum(nums, sum):
  table = dict()
  arr = []
    
  for i in range(0, len(nums)): 
    if nums[i] not in table:
      table[nums[i]] = [i]
    else:
      table[nums[i]] += [i]

  for i in range(0, len(nums)):
    sub = sum - nums[i]
    if sub in table:
      for s in table[sub]:
        if s > i:
          arr.append([i, s])

  for i in range(0, len(nums)):
    sub = sum - nums[i]
    for j in range(i+1, len(nums)):
      sub2 = sub - nums[j]
      if sub2 in table:
          for s in table[sub2]:
            if s > j:
              arr.append([i, j, s])
  return arr