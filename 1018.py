def check_chess(chess_list):
    start_B = 0
    start_W = 0

    for i in range(8):
        for j in range(8):
            if chess_list[i][j] == 'B' and (i+j) % 2 == 0:
                start_B += 1
            elif chess_list[i][j] == 'W' and (i+j) % 2 == 1:
                start_B += 1

    for i in range(8):
        for j in range(8):
            if chess_list[i][j] == 'W' and (i+j) % 2 == 0:
                start_W += 1
            elif chess_list[i][j] == 'B' and (i+j) % 2 == 1:
                start_W += 1

    return min(start_W, start_B)

n, m = list(map(int, input().split()))

chess = []

for _ in range(n):
    chess.append(list(input()))

answer = 10000
temp_answer = 10000

for i in range(n-7):
    for j in range(m-7):
        temp_answer = check_chess(list(row[j:j+8] for row in chess[i:i+8]))
        if answer > temp_answer:
            answer = temp_answer

print(answer)

