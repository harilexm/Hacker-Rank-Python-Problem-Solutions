# Solution 1
def mutate_string(string, position, character):
    l = list(string)
    l[position] = character
    return ''.join(l)

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)

# Solution 2
def mutate_string(string, position, character):
    new_string = string[:position]+character+string[position+1:]
    return new_string

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
