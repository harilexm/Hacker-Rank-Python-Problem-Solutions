# Enter your code here. Read input from STDIN. Print output to STDOUT
a = int(input())
b = int(input())

total = divmod(a, b)
for nums in total:
    print(nums)
    
print(total)
