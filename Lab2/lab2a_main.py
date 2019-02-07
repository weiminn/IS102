# lab2a_main.py
# Do not submit this file
# You may modify this file for testing purposes, 
# but your final lab2a.py must be able to run with the original lab2a_main.py.

from lab2a import *
import random
import time

NO_OF_REPETITIONS = 500000            # change this if you want to reduce the number of times exist() is called (line 17 of lab2a.py)
DATA_FILE_NAME = "employees_100.csv" # change the data file name to "employees_1mil.csv" if you want to use the larger data set 

# (1) ----- prepare data ------
employee_list = []
# the following statements read all the IDs from the data CSV file into 
# employee_list. You don't have to know these statements  work.
print("Reading data from " + DATA_FILE_NAME + " now ...")
with open("data/" + DATA_FILE_NAME, "r") as file:
  for line in file:
    line = line.rstrip("\n")
    id = int(line.split(",")[0])
    employee_list.append(id)

     
# make a clone of employee_list. This clone employee_list_clone will be used for correctness testing later
employee_list_clone = list(employee_list)

# (2) ----- performance testing code ------
# generate random numbers
print("Generating random numbers now...")
random_numbers = []

for i in range(NO_OF_REPETITIONS):
  random_numbers.append(random.randint(0,2001000)) # generate a random employee ID between 0 and 2001000

# run the test cases
print("Starting timer...")
print("Calling your perform_once function now...")
start_time = time.time()
employee_list = perform_once(employee_list)

results = []                # used to store all your results for later
print("Calling your exist function " + str(NO_OF_REPETITIONS) + " times now...")
for i in range(NO_OF_REPETITIONS):
  result = exist(random_numbers[i], employee_list)   # the correctness of result is not checked here
  results.append(result)  # insert your result into the results array for correctness checking later

time_taken = time.time() - start_time
print("Stopping timer...")
print("Execution time " + str(time_taken) + " seconds.")    # display time lapsed

# (3) ----- correctness testing code ------ 
# only the first 100 results are checked. assumption is that if the first 100 are correct, everything else is correct
print("Checking the first 100 results now...")

all_correct = True
for i in range(min(100, NO_OF_REPETITIONS)):
  if results[i] != (random_numbers[i] in employee_list_clone):
    print("ERROR in your result when searching for employee ID " + str(random_numbers[i]))
    all_correct = False

# # (4) ----- show results ----- 
if all_correct:
  print("Results are correct! - you may upload lab2a.py to the submission server")
else:
  print("Your exist function is not correctly written :-(")
