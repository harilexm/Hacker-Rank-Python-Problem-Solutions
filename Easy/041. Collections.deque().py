# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque

s = deque()
N = int(input())
for i in range(N):
    line = input().split()
    if line[0] == 'pop':
        s.pop()
    elif line[0] == 'append':
        s.append(int(line[1]))
    elif line[0] == 'popleft':
        s.popleft()
    elif line[0] == 'appendleft':
        s.appendleft(int(line[1]))
for i in s:
    print (i, end=' ')
