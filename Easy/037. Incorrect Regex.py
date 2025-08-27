# Use Python 2 Only for this task...
import re

T = int(input())
for i in range(T):
  S = raw_input()
  try:
    re.compile(S)
    print(True)
  except re.error:
    print(False)
