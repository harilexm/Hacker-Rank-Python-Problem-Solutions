# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter

K = int(input())
rooms = list(map(int, input().split()))

count = Counter(rooms)
for room, freq in count.items():
    if freq == 1:
        print (room)
