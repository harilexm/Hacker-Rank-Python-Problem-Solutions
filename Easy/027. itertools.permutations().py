from itertools import permutations

S, K = input().split()
for item in sorted(permutations(S, int(K))):
  print (''.join(item))
