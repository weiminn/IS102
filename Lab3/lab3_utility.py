# lab3_utility.py
# Do not submit this file
# Do not modify this file as well. 

# Ensure that this file is in the same folder as lab3_main.py

# reads a CSV file and returns a 2D list of ints
# e.g. read_file("case1.csv") will return: [[2], [0, 3], [0, 1], [1, 2, 4, 5], [1, 6, 10], [], [7, 8], [], [], [8], [9]
def read_file(file_name):
  input = []
  with open("data/" + file_name, "r") as file:
    for line in file:
      line = line.rstrip("\n")
      current_list = line.split(",")
      index = int(current_list.pop(0))  # 1st element is the index. assumption: the index is always in sequence: 0, 1, 2,.... etc
      current_list = [int(i) for i in current_list]  # convert all elements from strings into ints 
      input.append(current_list)        # insert into list   
  return input

# takes in an answer (e.g. [1,5,3,6,8]. and returns either
# - an error message (string), or
# - None (meaning there is no error with syntax of answer). 
# answer must be a list of exactly 5 integers. 
def get_error_message(answer):
  if answer == None:
    return "Error : your function returned None. It should return a list of 5 integers."
  elif type(answer) is not list:
    return "Error : your function returned something other than a list. It should return a list of 5 integers."
  elif len(answer) != 5:
    return "Error : your function returned a list of fewer than, or more than 5 elements. It should return a list of exactly 5 integers."
  elif not all(isinstance(i, int) for i in answer):  # check if all elements in answer are int
    return "Error : your function returned a list of elements, but not all of them are integers. It should return a list of exactly 5 integers."
  else:
    return None  # no problem
    
 
# takes in 2 arguments:
#   - selected is an list of 5 integers (user IDs)
#   - followers is a 2D list of followers 
# returns an list of unique followers for the 5 selected users in sorted order (excluding the 5 selected users)
def get_unique_followers (selected, followers):
  f0 = followers[selected[0]] #f0 contains all the followers of the 1st selected user
  f1 = followers[selected[1]] #f1 contains all the followers of the 1st selected user
  f2 = followers[selected[2]] #f2 contains all the followers of the 1st selected user
  f3 = followers[selected[3]] #f3 contains all the followers of the 1st selected user
  f4 = followers[selected[4]] #f4 contains all the followers of the 1st selected user

  f  = list(set(f0 + f1 + f2 + f3 + f4))  # now combine all the lists and remove duplicates (casting to a set removes all duplicates)

  # remove the original 5 selected users; we don't want to consider them
  if selected[0] in f:
    f.remove(selected[0])
  if selected[1] in f:
    f.remove(selected[1])
  if selected[2] in f:
    f.remove(selected[2])
  if selected[3] in f:
    f.remove(selected[3])
  if selected[4] in f:
    f.remove(selected[4])

  return sorted(f)  # return a sorted version of f.
