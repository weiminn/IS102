# Name: Wei Minn
# Section: G5

# lab2a

# INSTRUCTIONS: 
# Refer to the code in lab2a_main.py (line 41) - perform_once() will be called one time before 
# exist() is called many times. You may modify this function if desired, or leave it as it is.
def perform_once(employee_list):
  # This function takes in employee_list and returns the same employee_list for now.
  return employee_list

# INSTRUCTIONS: 
# This method is a fully functioning method that uses sequential search to search for the id in employee_list.
# This method returns True (if this ID exists), or False otherwise.
# Modify this method so that it uses a superior algorithm that performs significantly faster.

# def exist(id, employee_list):
#   for i in range(0, len(employee_list)):
#     if employee_list[i] == id:
#       return True
      
#   return False  # not found
def exist(x, a):
  "User a binary search to find x in list a"
  lower = -1
  upper = len(a)
  
  while upper > lower + 1:
    mid = (lower + upper) // 2
#   print_bsearch_brackets(a, lower, mid, upper)

    if a[mid] == x:   
      return True    # found it!! Return index
    
    if x < a[mid]:
      upper = mid   # discard right side
    else:
      lower = mid   # discard left side           

  return False  # completed while loop; no match found 


# def exist(id, employee_list):
#   if(len(employee_list) > 1):
#       mid = int((len(employee_list)/2))
#       if employee_list[mid] == id:
#           return True
#       elif id < employee_list[mid]:
#           n_arr = employee_list[0:mid]
#           exist(id, n_arr)
#       elif id > employee_list[mid]:
#           n_arr = employee_list[mid+1:]
#           exist(id, n_arr)
#       return False
#   else:
#       if len(employee_list) != 0:
#           if employee_list[0] == id:
#               return True