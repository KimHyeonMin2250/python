N = int(input())


for i in range(N):
    sum = 0
    cnt = 0
    score = list(map(int,input().split()))
    for j in range(1,len(score)):
        sum += score[j]

    for j in range(1,len(score)):
        if(score[j]>sum/score[0]):
            cnt += 1
        else:
            continue

    
    print("{:.3f}%".format(cnt/(len(score)-1)*100,3))