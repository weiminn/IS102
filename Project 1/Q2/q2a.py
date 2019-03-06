# q2a.py
# Name: Wei Minn
# Section: G5

from collections import deque
# TODO: fill sv_iterative
# m is a matrix represented by a 2D list of integers. e.g. m = [[3, 0, 2, 18],[-1, 1, 3, 4],[-2, -3, 18, 7]]
# This function returns the Special Value of the matrix passed in.
def sv_iterative(m):
  # your code here
  total = 0
  q = deque()
  for i in range(len(m[0])-1):
    q.append(1)

  for i in range(len(m)):
    last = 1
    for j in range(len(m[i])):
      if i == 0 or j == 0:
        total += (m[i][j] * 1)
      else:
        times = q.popleft() + last
        total += (m[i][j] * times)
        q.append(times)
        last = times

  return total