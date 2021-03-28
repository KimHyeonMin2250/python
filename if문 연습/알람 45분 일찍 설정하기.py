H,M = input().split()

H=int(H)
M=int(M)
if(M>45):
    print(H,M-45)
elif(M<45):
    if(H == 0):
        print(23,60-(45-M))
    elif(H!=0):
        print(H-1,60-(45-M))
elif(M==45):
    print(H,0)