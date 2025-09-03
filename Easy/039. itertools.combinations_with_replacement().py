# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations_with_replacement

S, k = input().strip().split()
k = int(k)

Final = sorted(combinations_with_replacement(sorted(S), k))
for i in Final:
  print (''.join(i))
