# Enter your code here. Read input from STDIN. Print output to STDOUT
T = int(input())

for i in range(T):
    a, b = input().split()
    try:
        print (int(a)//int(b))
    except ZeroDivisionError as e:
        print('Error Code:', e)
    except ValueError as z:
        print('Error Code:', z)        
