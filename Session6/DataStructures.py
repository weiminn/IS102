from queue import *
from pythonds import Stack

def isPalindrome2q(s):
    q = Queue()
    for letter in s:
        q.put(letter)
    i = len(s)-1
    while i >= 0:
        if s[i] != q.get():
            return False
        i -= 1
    return True

# print(isPalindrome('madsssddam'))

def isPalindrome1s(s):
    stack = Stack()
    for letter in s:
        stack.push(letter)
    for i in s:
        if i != stack.pop():
            return False
    return True

# print(isPalindrome1s('madsssddam'))
# print(isPalindrome1s('madsssdam'))