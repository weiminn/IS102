# lab2b_main.py
# Do not submit this file
# You may modify this file for testing purposes, 
# but your final lab2b.py must be able to run with the original lab2b_main.py.

from lab2b import *
import random
import time

NO_OF_REPETITIONS = 500000                      # change this if you want to reduce the number of times exist is called (line 18 of lab2b.py)
DATA_FILE_NAME = "employees_birthyear_1mil.csv" # change the data file name if you want to use another data file
                                                # BUT the test cases below are valid only for employees_birthyear_1mil.csv

# (1) ----- prepare data ------
employee_with_birthyear_list = []
# the following statements read all the IDs from the data CSV file into 
# employee_with_birthyear_list. You don't have to know these statements  work.
print("Reading data from " + DATA_FILE_NAME + " now ...")
with open("data/" + DATA_FILE_NAME, "r") as file:
  for line in file:
    line = line.rstrip("\n")
    id = int(line.split(",")[0])
    year = int(line.split(",")[1])
    employee_with_birthyear_list.append([id,year])

# (2) ----- correctness testing code ------
# ONLY works with employees_birthyear_1mil.csv!!!!!
start_time = time.time()
employee_with_birthyear_list = perform_once(employee_with_birthyear_list)
error = False

# test case #1: birth year: 1949. IDs: [101, 201, 1999632, 1999649]
result = get_IDs_with_birthyear(1949, employee_with_birthyear_list)
if sorted(result) != [101, 201, 1999632, 1999649]:
  error = True
  print("Error: Test case 1 failed. Your get_IDs_with_birthyear function returned a wrong value when called with 1949")

# test case #2: birth year: 2006. IDs: [104, 357256, 833786, 833789, 1999588]
if not error:
  result = get_IDs_with_birthyear(2006, employee_with_birthyear_list)
  if sorted(result) != [104, 357256, 833786, 833789, 1999588]:
    error = True
    print("Error: Test case 2 failed. Your get_IDs_with_birthyear function returned a wrong value when called with 2006")
  
# test case #3: birth year: 2015. IDs: []
if not error:
  result = get_IDs_with_birthyear(2015, employee_with_birthyear_list)
  if result != []:
    error = True
    print("Error: Test case 3 failed. Your get_IDs_with_birthyear function returned a wrong value when called with 2015")

# test case #4: birth year: 1975. There should be 3614 IDs in the returned set
if not error:
  result = get_IDs_with_birthyear(1975, employee_with_birthyear_list)
  if len(result) != 18221:
    error = True
    print("Error: Test case 4 failed. Your get_IDs_with_birthyear function returned a wrong value when called with 1975")

# test case #5: birth year: 1970. There should be 3599 IDs in the returned set
if not error: 
  result = get_IDs_with_birthyear(1970, employee_with_birthyear_list)
  if len(result) != 18312:
    error = True
    print("Error: Test case 5 failed. Your get_IDs_with_birthyear function returned a wrong value when called with 1970")

# (3) ----- performance testing code ------
# generate random numbers
# Get output from student's answer          
for i in range(NO_OF_REPETITIONS):
  random_year = random.randint(0,55) + 1950  # generate random year between 1950 and 2005
  get_IDs_with_birthyear(random_year, employee_with_birthyear_list) # results not checked
            
time_taken = time.time() - start_time
print("Stopping timer...")
print("Execution time " + str(time_taken) + " seconds.")    # display time lapsed

# (4) ----- show results ----- 
if not error:
  print("Results are correct! - you may upload lab2b.py to the submission server")
else:
  print("Your get_IDs_with_birthyear function is not correctly written :-(")
