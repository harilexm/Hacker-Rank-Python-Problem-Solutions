# Enter your code here. Read input from STDIN. Print output to STDOUT
N_stamps = int(input())

S = set()
for i in range(N_stamps):
    Country = input().strip()
    B = S.add(Country)
    
print (len(S))
    
