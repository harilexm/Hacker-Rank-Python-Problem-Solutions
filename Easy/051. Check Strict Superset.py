# Enter your code here. Read input from STDIN. Print output to STDOUT
A = set(map(int, input().split()))
n = int(input())

final = True
for i in range(n):
    B = set(map(int, input().split()))
    if A.issuperset(B):
        continue
    else:
        final = False
        break
print(final)
