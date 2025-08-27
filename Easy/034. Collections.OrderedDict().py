# Solution 1
from collections import OrderedDict

def netprice(N):
    dicti = OrderedDict()
    for i in range(N):
        name, price = input().strip().rsplit(' ', 1)
        price = int(price)
        if name in dicti:
            dicti[name] += price
        else:
            dicti[name] = price
    return dicti

N = int(input())
k = netprice(N)
for name, price in k.items():
    print(name, price)
    
# Solution 2
from collections import OrderedDict

N = int(input())
New_dict = OrderedDict()

for i in range(N):
    item_name, item_price = input().strip().rsplit(' ', 1)
    item_price = int(item_price)
    if item_name in New_dict:
      New_dict[item_name] += item_price
    else:
      New_dict[item_name] = item_price
      
for item, price in New_dict.items():
      print (item, price)
