from collections import deque
import re

def isPalindrome(s):
    strs = deque()

    for char in s:
        if char.isalnum():
            strs.append(char.lower())

    while len(strs) > 1:
        if strs.popleft() != strs.pop():
            return False

    return True

def isPalindrome2(s):
    s = s.lower()
    s = re.sub('[^a-z0-9]','',s)

    return s == s[::-1]

print(isPalindrome2("A man, a plan, a canal: Panama"))

print(isPalindrome2("race a car"))