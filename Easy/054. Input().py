# Solution: 1
x, k = map(int, input().split())
P = input().strip()

result = eval(P)
if result == k:
    print(True)
else:
    print (False)

# Solution: 2
x, k = map(int, input().split())
print (eval(input()) == k)
