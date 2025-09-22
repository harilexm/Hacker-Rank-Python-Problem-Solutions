T = int(input())
for i in range(T):
    N= input()
    if ('.') in N:
        try:
            N= float(N)
            print(True)
        except:
            print(False)
    else:
        print(False)
