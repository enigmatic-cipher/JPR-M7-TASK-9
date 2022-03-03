"""
Given a String as input, count the number of a and b in the string. Use recursion. Do not use loops. Do a dry run for each test case.
Input-> "abcdefgh123"
Output-> 2
"""

def countAB(st):
  ln = len(st)
  if (ln==0):
    return 0 

  count = 0
  ch = st[0]
  if (ch=='a' or ch=='b'):
    count = count + 1
  return (count + countAB(st[1:]))

st = "abcdefgh123"
print(countAB(st))