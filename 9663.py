def checkConstraint(depth):
    for i in range(depth):
        if row[i] == row[depth] or (depth-i) == abs(row[depth] - row[i]):
            return False
    return True


def dfs(depth):
    global answer
    if depth == N:
        answer += 1
    else:
        for column in range(N):
            row[depth] = column
            if checkConstraint(depth):
                dfs(depth+1)


N = int(input())

row = [0] * N
answer = 0
dfs(0)
print(answer)

