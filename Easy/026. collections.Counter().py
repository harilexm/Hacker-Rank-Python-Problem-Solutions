from collections import Counter

X = int(input())
size_ava = list(map(int, input().split()))
N = int(input())
customer = Counter(size_ava)

total = 0
for i in range(N):
  size_ava, price = map(int, input().split())
  if customer[size_ava] > 0:
    total += price
    customer[size_ava] -= 1
print (total)
