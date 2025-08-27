# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations

S, K = input().split()

for i in range(1, int(K)+1):
  for j in combinations(sorted(S), i):
    print(''.join(j))
