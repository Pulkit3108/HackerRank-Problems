def average(array):
    a=set(array)
    s=sum(a)
    x=len(a)
    avg=s/x
    return(avg)

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
