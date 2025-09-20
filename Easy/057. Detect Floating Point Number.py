T = int(input())

for i in range(T):
    N = input()
    try:
        if N == float(N):
            print(True)
    except:
        print(False)