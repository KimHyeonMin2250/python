N = int(input())
hansu = 0

for i in range(1,N+1) :
    if i<=99:
        hansu += 1
    else:
        Ns = list(map(int,str(i)))
        if Ns[0] - Ns[1] == Ns[1] - Ns[2] :
            hansu += 1

print(hansu)
