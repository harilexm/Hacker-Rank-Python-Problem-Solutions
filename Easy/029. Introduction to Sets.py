def average(array):
    avg_arr = set(array)
    result_arr = sum(avg_arr)/len(avg_arr)
    return (f'{result_arr:.3f}')
    

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
