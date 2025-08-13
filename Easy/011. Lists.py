if __name__ == '__main__':
    N = int(input())
    A = []
    
    for _ in range(N):
        user_input = input().split()
        
        if user_input[0] == 'insert':
            A.insert(int(user_input[1]), int(user_input[2]))
        elif user_input[0] == 'print':
            print(A)
        elif user_input[0] == 'remove':
            A.remove(int(user_input[1]))
        elif user_input[0] == 'append':
            A.append(int(user_input[1]))
        elif user_input[0] == 'sort':
            A.sort()
        elif user_input[0] == 'pop':
            A.pop()
        elif user_input[0] == 'reverse':
            A.reverse()
