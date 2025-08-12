# Solution 1
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    New_arr = sorted(set(arr))
    print(New_arr[-2])

# Solution 2
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    New_arr = set(arr)
    remove_max = New_arr.remove(max(New_arr))
    print (max(New_arr))
