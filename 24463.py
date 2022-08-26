n, m = list(map(int, input().split()))  #행 n, 열 m

mazemap = []  # out of range 를 고려해서 maze 이중배열 선언

for row in range(n):  # maze를 입력 받음
    mazemap.append(list(input()))

temp_mazemap = mazemap
queue = []


def find_bfs():
    global start
    global destination
    i, j = start
    m, n = destination
    next_ij = [[0, 1], [-1, 0], [0, -1], [1, 0]]  # 다음 4칸을 미리저장
    while True:
        if i == m and j == n:
            return 1

        temp_i = temp_j = -100
        temp_mazemap[i][j] = '*'
        for next_i, next_j in next_ij:
            if temp_mazemap[i+next_i][j+next_j] == '.':  #처음으로 .인게 발견되면 다음 부분을 실행
                temp_i = i + next_i
                temp_j = j + next_j
                queue.append([i, j])

        if temp_i != -100:  # 주변에 .이 있을 경우
            i = temp_i
            j = temp_j
            temp_mazemap[i][j] = '*'
        else:  # 주변에 .이 없을 경우
            if len(queue) == 0:
                return -1
            mazemap[i][j] = 'X'
            i, j = queue.pop(0)

temp_stack = []
for i in range(n):
    if mazemap
for _ in mazemap:
    print(_)
