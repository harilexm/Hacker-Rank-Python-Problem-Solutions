if __name__ == '__main__':
    n = int(input().strip())
    #check n is odd
    if n % 2 == 1:
        print ('Weird')
    #check n is even & between range 2 to 5.
    elif n % 2 == 0 and 2 <= n <= 5:
        print ('Not Weird')
    #check n is even & between range 6 to 20.
    elif n % 2 == 0 and 6 <= n <= 20:
        print ('Weird')
    #check n is even & greater then 20.
    elif n % 2 == 0 and n > 20:
        print ('Not Weird')
