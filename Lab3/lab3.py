# Name: Wei Minn
# Section: G22

# lab3

def iSet(arr):
    i = 1
    while i < len(arr):
        j = i
        while (len(list(set(arr[j]))) < len(list(set(arr[j-1])))) and j >= 0:
            print(arr[j], arr[j-1])
            temp = arr[j-1]
            arr[j-1] = arr[j]
            arr[j] = temp
            j -= 1
        i += 1
    return arr

def select_tweeters(followers):
  # currently, this function always returns the first five users
  # obviously this arbitrary selection will result in a lousy quality score even though it's a "correct" answer :-/
  # print(followers)
  followers = iSet(followers)
  # print(followers)
  return [followers.index(followers[len(followers)-1]), followers.index(followers[len(followers)-2]), followers.index(followers[len(followers)-3]), followers.index(followers[len(followers)-4]), followers.index(followers[len(followers)-5])]
  # return [0, 1, 2,3, 4]