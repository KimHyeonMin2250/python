N = int(input())

for i in range(1,N+1,1):
    for j in range(0,N-i,1):
        print(" ",end = '')
    print("*"*i)