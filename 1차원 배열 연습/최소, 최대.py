N = int(input())

A = list(map(int,input().split()))

max_value = A[0]
min_value = A[0]

for num in A:
    if num > max_value:
        max_value = num
    if num < min_value:
        min_value = num

print(min_value, max_value)