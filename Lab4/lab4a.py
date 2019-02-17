# Name:
# Section:
 
# lab4(a)

# Takes in an integer and returns the sum of all its digits as an integer
# this method does NOT have to handle negative numbers (i.e. i will always be >=0)
# this method must be recursive (i.e. it will call itself)
# Refer to hints in the requirements doc.
def sum_of_digits(i):
  if(len(str(i)) == 1):
    return int(str(i)[0])
  else:
    return int(str(i)[0]) + sum_of_digits(int(str(i)[1:]))

# print(str(sum_of_digits(334)))
  