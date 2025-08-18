# Solution: 1
def print_formatted(number):
    # your code goes here
    pad = number.bit_length()
    for i in range(1, number + 1):
        print (f'{i:{pad}d} {i:{pad}o} {i:{pad}X} {i:{pad}b}' )

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)

# Solution: 2
def print_formatted(number):
    # your code goes here
    pad = number.bit_length()
    for i in range(1, number + 1):
        deci = str(i)
        octa = oct(i)[2:]
        hexa = hex(i)[2:].upper()
        bina = bin(i)[2:]
        print (deci.rjust(pad), octa.rjust(pad), hexa.rjust(pad), bina.rjust(pad))
    
if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
