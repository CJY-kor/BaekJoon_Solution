N = int(input())
rod_list = []
checker = 0
answer = 0


for _ in range(N):
    rod_list.append(int(input()))

for _ in range(N):
    temp_rod = rod_list.pop()
    print(temp_rod)
    if temp_rod > checker:
        checker = temp_rod
        answer += 1

print(answer)
