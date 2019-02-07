# lab3_main.py
# Do not submit this file
# You may modify this file for testing purposes, 
# but your final lab3.py must be able to run with the original lab3_main.py.

from lab3 import *
from lab3_utility import *
import time
import copy

# (1) ----- prepare data ------
print("")
file_name = input("Enter name of CSV file in data folder to read from (e.g. case1.csv) :")

# read from file_name and store in followers
# the following statements read the tweeter info from the CSV file into 
# the followers variable. You don't have to know these statements work.
print("(1) Reading data from " + file_name + " now...")
followers = read_file(file_name)

# make a clone of the original followers. 
# original_followers will be used for calculating the score later using get_unique_followers.
# this is important just in case the select_tweeters method modifies the values in followers passed in!!
followers_clone = copy.deepcopy(followers)

# uncomment the next statement if you want
# print("Read the following data from " + file_name + ":" + str(followers))

# (2) ----- run the test case ------
print("\n(2) Starting timer...")
print("Calling your select_tweeters function now using followers read from " + file_name)
start_time = time.time()
selected = select_tweeters(followers) # calls your function 
time_taken = time.time() - start_time
print("Stopping timer...")
print("Execution time " + str(time_taken) + " seconds.")    # display time lapsed

# (3) ----- correctness testing code ------ 
print("\n(3) Checking your answer...")
print("Your select_tweeters function returned this: " + str(selected))
error_message = get_error_message(selected)

if error_message == None:
  print("Your function returned a valid answer - you may upload lab2a.py to the submission server")
  reached_audience = get_unique_followers (selected, followers_clone)
  quality_score = len(reached_audience)
  print("The following users will get the advertisement : " + str(reached_audience))
  print("Quality score for this question is the number of unique users who will get the advertisement. A higher quality score is better.")
  print("Quality score : " + str(quality_score))
else:
  print("Your function is not correctly written :-(")
  print(error_message)
  

