a = list(map(int,input().split()))

def sum_N(N):
    sum=0
    for i in range (0,len(a)):
        sum = a[i]+sum
    N = sum
    return N

print(sum_N(a))