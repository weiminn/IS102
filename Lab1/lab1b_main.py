# lab1b_main.py
# Do not submit this file

# You may modify this file for testing purposes, 
# but your final lab1b.py must be able to run with the original lab1b_main.py.

from lab1b import weight_category
import time

# run the 5 test cases
startTime = time.time()
answer1 = weight_category(71, 168)     # test case 1. should return "overweight" 25.156
answer2 = weight_category(103, 200)    # test case 2. should return "overweight" 25.75
answer3 = weight_category(25, 100)     # test case 3. should return "normal" 25
answer4 = weight_category(65.3, 171)   # test case 4. should return "normal" 22.332
answer5 = weight_category(63, 185.1)   # test case 5. should return "underweight" 18.388
print("Execution time " + str(time.time()-startTime) + " seconds.") # display time lapsed

# show results of test cases

# test case 1
if answer1=="overweight":
  print("Test case 1 is correct")
else:
  print("Test case 1 is wrong")
  print("Test case 1: Your method is expected to return 'overweight'.")
  print("Test case 1: However it returned this instead: " + str(answer1))   

# test case 2
if answer2=="overweight":
  print("Test case 2 is correct")
else:
  print("Test case 2 is wrong")
  print("Test case 2: Your method is expected to return 'overweight'.")
  print("Test case 2: However it returned this instead: " + str(answer2)) 

# test case 3
if answer3=="normal":
  print("Test case 3 is correct")
else:
  print("Test case 3 is wrong")
  print("Test case 3: Your method is expected to return 'normal'.")
  print("Test case 3: However it returned this instead: " + str(answer3))

# test case 4
if answer4=="normal":
  print("Test case 4 is correct")
else:
  print("Test case 4 is wrong")
  print("Test case 4: Your method is expected to return 'normal'." )
  print("Test case 4: However it returned this instead: " + str(answer4))

# test case 5
if answer5=="underweight":
  print("Test case 5 is correct")
else:
  print("Test case 5 is wrong")
  print("Test case 5: Your method is expected to return 'underweight'." )
  print("Test case 5: However it returned this instead: " + str(answer5)) 

print()
print("Ensure that all 5 test cases are correct before submitting Your solution to the Submission Server")
