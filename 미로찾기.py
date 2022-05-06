m, n = list(map(int, input().split()))  # 행 m 열 n 입력받음

mazeMap = [[1 for col in range(n+2)] for row in range(m+2)]  # out of range 를 고려해서 maze 이중배열 선언

for row in range(1, m+1):  # maze를 입력 받음
    mazeMap[row][1:n+1] = list(map(int, input().split()))

Stack = []


def find():
    i = j = 1  # 현재 위치 초기화
    next_ij = [[0, 1], [-1, 1], [-1, 0], [-1, -1], [0, -1], [1, -1], [1, 0], [1, 1]]  # 다음 8칸을 미리저장
    while True:
        if i == m and j == n:
            return 1

        temp_i = temp_j = -100
        mazeMap[i][j] = '*'
        for next_i, next_j in next_ij:
            if mazeMap[i+next_i][j+next_j] == 0:  #처음으로 0인게 발견되면 다음 부분을 실행
                temp_i = i + next_i
                temp_j = j + next_j
                print(temp_i, temp_j)
                break

        if temp_i != -100:  # 주변에 0이 있을 경우
            Stack.append([i, j])
            i = temp_i
            j = temp_j
            mazeMap[i][j] = '*'
        else:  # 주변에 0이 없을 경우
            if len(Stack) == 0:
                return -1
            mazeMap[i][j] = 'X'
            i, j = Stack.pop()


find()
for _ in mazeMap:
    print(_)



