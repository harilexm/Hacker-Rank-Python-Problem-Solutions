# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
English_n = set(map(int, input().split()))
m = int(input())
French_m = set(map(int, input().split()))

total = English_n.union(French_m)

print(len(total))
