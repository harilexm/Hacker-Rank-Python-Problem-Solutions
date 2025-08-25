# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import namedtuple

def tablesave(n, fields):
    total = 0
    for i in range(n):
        students = namedtuple('i', fields)
        IDs, Marks, Name, Class = input().split()
        z = students(IDs, Marks, Name, Class)
        total += int(z.MARKS)
    return total

n = int(input())
fields = input().split()

k = tablesave(n, fields)
print('{:.2f}'.format(k/n))
