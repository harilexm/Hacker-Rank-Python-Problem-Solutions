# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
S = input()
pattern = re.findall(r'(?<=[^aeiouAEIOU])([aeiouAEIOU]{2,})(?=[^aeiouAEIOU])', S)
if pattern:
    for item in pattern:
        print(item)
else:
    print(-1)