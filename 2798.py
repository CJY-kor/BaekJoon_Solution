n, m = list(map(int, input().split()))

numbers = list(map(int, input().split()))

answer = 0

for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            if answer < numbers[i] + numbers[j] + numbers[k] <= m:
                answer = numbers[i] + numbers[j] + numbers[k]

print(answer)