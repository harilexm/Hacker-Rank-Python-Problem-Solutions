N = int(input("Enter number of elements:"))
num = list(map(int, input().split()))
print (all(i >= 0 for i in num) and any(str(i) == str(i)[::-1] for i in num))