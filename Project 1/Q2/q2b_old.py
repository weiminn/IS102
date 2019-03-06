# q2b.py
# Name: Wei Minn
# Section: G5

# TODO: fill sv_recursive
# m is a matrix represented by a 2D list of integers. e.g. m = [[3, 0, 2, 18],[-1, 1, 3, 4],[-2, -3, 18, 7]]
# This function returns the Special Value of the matrix passed in.
_m = []
def sv_recursive(m):
  # your code here
  global _m
  _m = m[:]
  return value(0, 0)

def value(a, b):
  if(a >= len(_m) or b >= len(_m[0])):
    return 0
  else:
    return _m[a][b] + value(a+1, b) + value(a, b+1)
