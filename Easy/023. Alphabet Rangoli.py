import string
def print_rangoli(size):
    # your code goes here
    alpha = string.ascii_lowercase
    s = []
    for i in range(size):
        s.append(('-'.join(alpha[size-1:i:-1] + alpha[i:size])).center(size*4-3, '-'))
  
    print ('\n'.join(s[::-1]+s[1:]))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
