R, C = list(map(int, input().split()))

Rg, Cg, Rp, Cp = list(map(int, input().split()))

room_list = []

P = 0

answer = 0

for _ in range(R):
    room_list.append(list(input()))

for i in range(R):
    for j in range(C):
        if room_list[i][j] == "P":
            P += 1

if P != Rp * Cp:
    answer = 1

print(answer)
