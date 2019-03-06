# q3_main.py
# do NOT submit this file. Run it to test your solution. 
from q3 import *

# the following functions are used for answer checking  
# test case functions return True (if successful) or False (if failed)
# ------------------------------------
# test case 1
def test_case1():
  nums = [3, 0, 1, 0, -1, -2, 0]
  t = 0
  expected_answer = [[1, 3], [1, 6], [2, 4], [3, 6], [0, 4, 5], [1, 2, 4], [1, 3, 6], [2, 3, 4], [2, 4, 6]]

  your_answer = ttsum(nums, t) # calling your function 
  if sort_answer(your_answer) == expected_answer:
    return True
  else:
    return False

# ------------------------------------    
# test case 2
def test_case2():
  nums = [3, 0, 1, 0, -1, -2, 0]
  t = 2
  expected_answer = [[0, 4], [0, 1, 4], [0, 2, 5], [0, 3, 4], [0, 4, 6]] 

  your_answer = ttsum(nums, t) # calling your function 
  if sort_answer(your_answer) == expected_answer:
    return True
  else:
    return False

# ------------------------------------    
# test case 3
def test_case3():
  nums = [1, 2, 3, -1, -2, -3, 4, 5, 6, -4, -5, -6, 0]
  t = 5
  expected_answer = [[0, 6], [1, 2], [3, 8], [7, 12], [0, 3, 7], [0, 4, 8], [0, 6, 12], [1, 2, 12], [1, 3, 6], [1, 4, 7], [1, 5, 8], [2, 4, 6], [2, 5, 7], [2, 8, 9], [3, 8, 12], [6, 7, 9], [6, 8, 10], [7, 8, 11]]

  your_answer = ttsum(nums, t) # calling your function 
  if sort_answer(your_answer) == expected_answer:
    return True
  else:
    return False

# ------------------------------------    
# takes in an answer (e.g. [[1, 6], [2, 4], [0, 4, 5], [1, 3, 6], [1, 2, 4], [2, 3, 4], [2, 4, 6], [3, 1], [6, 3]])
# and returns the elements sorted in ascending order (e.g. [[1, 3], [1, 6], [2, 4], [3, 6], [0, 4, 5], [1, 2, 4], [1, 3, 6], [2, 3, 4], [2, 4, 6]])
# sorting criteria:
#   - all 2-member elements will be in front of 3-member elements
#   - within each inner list, integers will be sorted in ascending order. 
def sort_answer(answer):
  r2 = [] # list containing 2 members
  r3 = [] # list containing 3 members
  
  for s in answer:
    if type(s) is list and len(s) == 2:
      s.sort()   # sort inside, then append
      r2.append(s)
    elif type(s) is list and len(s) == 3:
      s.sort()   # sort inside, then append
      r3.append(s)
  
  r2.sort(key = lambda x: (x[0], x[1])) # sort by 1st, then 2nd element 
  r3.sort(key = lambda x: (x[0], x[1], x[2])) # sort by 1st, then 2nd element , then 3rd element
  return r2 + r3 

# ------------------------------------  
# actual code that runs 
print("Test case 1 returned : ", end="")
print(test_case1())
print("Test case 2 returned : ", end="")
print(test_case2())
print("Test case 3 returned : ", end="")
print(test_case3())  