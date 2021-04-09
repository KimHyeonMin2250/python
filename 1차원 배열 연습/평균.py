N = int(input())

score = list(map(float,input().split()))

s= max(score)
for j in range(N):
    score[j]=score[j]/s*100

sum = sum(score)
print(sum/N)
