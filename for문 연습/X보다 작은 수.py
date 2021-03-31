j,z = map(int,input().split())
N = list(map(int, input().split()))
for i in range(j):
    if(N[i]>z):
        print(N[i],end=' ')
