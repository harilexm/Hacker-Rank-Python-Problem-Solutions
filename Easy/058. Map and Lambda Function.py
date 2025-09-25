cube = lambda x: pow(x, 3) # power of x to 3 times.

def fibonacci(n):
    # return a list of fibonacci numbers
    fib = list()
    a, b = 0, 1
    for _ in range(n):
        fib.append(a)
        a, b = b, a + b
        return fib
    
if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))