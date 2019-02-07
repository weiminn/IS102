# lab1a_main.py
# Do not submit this file

# You may modify this file for testing purposes, 
# but your final lab1a.py must be able to run with the original lab1a_main.py.

from lab1a import admit
import time

# run the 4 test cases
startTime = time.time()
answer1 = admit("M",22) # test case 1
answer2 = admit("M",23) # test case 2
answer3 = admit("F",17) # test case 3
answer4 = admit("F",18) # test case 4
print("Execution time " + str(time.time()-startTime) + " seconds.") # display time lapsed

# show results with 4 test cases

# check test case 1
if answer1 == False:
  print("Test case 1 is correct")
else:
  print("Test case 1 is wrong")
  print("Test case 1: Your method is expected to return False.")
  print("Test case 1: However it returned this instead: " + str(answer1))

# check test case 2
if answer2 == True:
  print("Test case 2 is correct")
else:
  print("Test case 2 is wrong")
  print("Test case 2: Your method is expected to return True.")
  print("Test case 2: However it returned this instead: " + str(answer2))

# check test case 3
if answer3 == False:
  print("Test case 3 is correct")
else:
  print("Test case 3 is wrong")
  print("Test case 3: Your method is expected to return False.")
  print("Test case 3: However it returned this instead: " + str(answer3))  

# check test case 4
if answer4 == True:
  print("Test case 4 is correct")
else:
  print("Test case 4 is wrong")
  print("Test case 4: Your method is expected to return True.")
  print("Test case 4: However it returned this instead: " + str(answer4)) 

print() # blank line
print("Ensure that all 4 test cases are correct before submitting Your solution to the Submission Server")
