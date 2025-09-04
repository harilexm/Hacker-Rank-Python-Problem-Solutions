# Use python 3 instead of pypy3
s = map(int, input().strip().split())
s = set(s)
N = int(input())

for num in range(N):
    line = input().strip().split()
    if line == 'pop':
        s.pop()
    elif line[0] == 'remove':
        s.remove(int(line[1]))
    elif line[0] == 'discard':
        s.discard(int(line[1]))
print (sum(s))
