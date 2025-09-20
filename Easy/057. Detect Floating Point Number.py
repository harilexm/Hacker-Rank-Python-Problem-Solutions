T = int(input("Enter number of test cases:"))

for i in range(T):
    N = input("Enter String")
    try:
        if N == float(N):
            print(True)
    except:
        print(False)