# q2b_main.py
# do NOT submit this file. Run it to test your solution. 
from q2b import *

# the following functions are used for answer checking  
# test case functions return True (if successful) or False (if failed)

# --------------------------------------------  
# test case 1
def test_case1():
  m = [[3, 0, 2, 18],[-1, 1, 3, 4],[-2, -3, 18, 7]]
  expected_answer = 216
  
  if sv_recursive(m) == expected_answer:
    return True
  else:
    return False  

# --------------------------------------------  
def test_case2():
  m = [[6, 1, -1, 3],[7, 7, 7, 8],[-1, -1, 0, 10]]
  expected_answer = 179
  
  if sv_recursive(m) == expected_answer:
    return True
  else:
    return False  

# --------------------------------------------  
def test_case3():
  m = [[10, 5, -1, -2, -5], [1, 2, 3, 4, 6], [0, 4, 3, 2, 1]]
  expected_answer = 132
  
  if sv_recursive(m) == expected_answer:
    return True
  else:
    return False 
# --------------------------------------------  

# actual code that runs 
print("Test case 1 returned : ", end="")
print(test_case1())
print("Test case 2 returned : ", end="")
print(test_case2())
print("Test case 3 returned : ", end="")
print(test_case3()) 
