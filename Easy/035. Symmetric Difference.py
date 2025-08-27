# Solution 1
M = int(input())
a = set(map(int, input().strip().split()))
N = int(input())
b = set(map(int, input().strip().split()))

difference = sorted(a ^ b)
for values in difference:
    print(values)

# Solution 2
M = int(input())
a = set(map(int, input().split()))
N = int(input())
b = set(map(int, input().split()))

diff = a.symmetric_difference(b)
diff_sort = sorted(diff)

for item in diff_sort:
    print(item)
