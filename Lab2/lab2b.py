# Name: Wei Minn
# Section: G5

# lab2b

# INSTRUCTIONS: 
# Refer to the code in lab2b_main.py - perform_once will be called one time before 
# exist is called many times. You may modify perform_once if desired, or keep it as it is.
def perform_once(employee_with_birthyear_list):
  # Write any code here if desired. Any code you do here will replace the original employee_list
  return employee_with_birthyear_list

  
# INSTRUCTIONS: 
# Write a function called get_IDs_with_birthyear that takes in a year (as an integer) and an array (employee_with_birthyear_list)
# It then returns an array of employee IDs (integers) that have matching birthyears.
# If there is no match, this function returns an empty array (i.e. []).
def get_IDs_with_birthyear(year, employee_with_birthyear_list):
  # for now, this function always returns an empty list
  _arr = []
  # employee_with_birthyear_list.sort(key=lambda x: x[1])
  # print(year)
  for em in employee_with_birthyear_list:
    # print em[1]
    if em[1] == year:
      _arr.append(em[0])
  # print _arr
  return _arr