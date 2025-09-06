# Enter your code here. Read input from STDIN. Print output to STDOUT
X = int(input())
A = set(map(int, input().split()))

N = int(input())
for n in range(N):
    cmd, num = input().split()
    B = set(map(int, input().split()))
    getattr(A, cmd)(B)
    
print(sum(A))
