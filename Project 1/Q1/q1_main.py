# q1_main.py
# do NOT submit this file. Run it to test your solution. 
from q1 import *

# the following function is used for answer checking  

# It calls your function 10000 times and shows the frequency that a particular number appears on your simulated die
# because of the random number generation, a slight variation in frequency is acceptable.
# For example, if loaded_die() has been properly written, the number 1 will appear ~50% of the time, 
# and the remaining numbers (2, 3, 4, 5, 6) will appear ~10% of the time. 
# A slight deviation is acceptable. For example, "1" has a frequency of 49.5-50.5% is fine.
# The frequencies for 0, 7, 8 and 9 should be 0%. 

# --------------------------------------------
# calls r6_loaded() 10000x, and print stats
def show_stats_r6_loaded():
  no_of_rolls = 10000
  
  count_list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  # keep track of the number of times 0 to 9 appear
  for i in range(0, no_of_rolls):
    roll = r6_loaded(); # call your function 
    
    if type(roll) is int and roll < 10 and roll > -1:
      count_list[roll] += 1
  
  # print stats
  for i in range(0, 10):
    print(str(i) + " appeared " + str(count_list[i]) + "/" + str(no_of_rolls) + " times (" + str(count_list[i]/no_of_rolls*100) + "%)")

# --------------------------------------------  
# actual code that runs 
print("Running show_stats_r6_loaded")
show_stats_r6_loaded()
