h, w = list(map(int, input().split()))
paper = []
temp_answer = 0
answer = 0

for _ in range(h):
    paper.append(list(map(int, input().split())))


def check_paper(paper, i, j, h, w):
    answer = 0
    temp_answer = 0

    if j + 4 <= w:
        temp_answer = paper[i][j] + paper[i][j+1] + paper[i][j+2] + paper[i][j+3]
        if answer < temp_answer:
            answer = temp_answer
    if i + 4 <= h:
        temp_answer = paper[i][j] + paper[i+1][j] + paper[i+2][j] + paper[i+3][j]
        if answer < temp_answer:
            answer = temp_answer
    if i + 2 <= h and j + 2 <= w:
        temp_answer = paper[i][j] + paper[i+1][j] + paper[i][j+1] + paper[i+1][j+1]
        if answer < temp_answer:
            answer = temp_answer
    if i + 3 <= h and j + 2 <= w:
        temp_answer = paper[i][j] + paper[i+1][j] + paper[i+2][j] + paper[i+2][j+1]
        if answer < temp_answer:
            answer = temp_answer
    if i + 3 <= h and j + 2 <= w:
        temp_answer = paper[i][j] + paper[i+1][j+1] + paper[i+2][j+1] + paper[i][j+1]
        if answer < temp_answer:
            answer = temp_answer
    if i + 2 <= h and j + 3 <= w:
        temp_answer = paper[i][j] + paper[i][j+1] + paper[i][j+2] + paper[i+1][j+2]
        if answer < temp_answer:
            answer = temp_answer
    if i + 2 <= h and j + 3 <= w:
        temp_answer = paper[i][j] + paper[i+1][j] + paper[i+1][j+1] + paper[i+1][j+2]
        if answer < temp_answer:
            answer = temp_answer
    if i + 3 <= h and j + 2 <= w:
        temp_answer = paper[i][j] + paper[i+1][j] + paper[i+1][j+1] + paper[i+2][j+1]
        if answer < temp_answer:
            answer = temp_answer
    if i + 2 <= h and j + 3 <= w:
        temp_answer = paper[i][j] + paper[i][j+1] + paper[i+1][j+1] + paper[i+1][j+2]
        if answer < temp_answer:
            answer = temp_answer
    if 3 <= i + 2 <= h and j + 3 <= w:
        temp_answer = paper[i][j] + paper[i][j+1] + paper[i-1][j+1] + paper[i-1][j+2]
        if answer < temp_answer:
            answer = temp_answer
    if 4 <= i + 2 <= h and j + 2 <= w:
        temp_answer = paper[i][j] + paper[i-1][j] + paper[i-1][j+1] + paper[i-2][j+1]
        if answer < temp_answer:
            answer = temp_answer
    if i + 2 <= h and j + 3 <= w:
        temp_answer = paper[i][j] + paper[i][j+1] + paper[i+1][j+1] + paper[i][j+2]
        if answer < temp_answer:
            answer = temp_answer
    if i + 3 <= h and j + 2 <= w:
        temp_answer = paper[i][j] + paper[i+1][j] + paper[i+1][j+1] + paper[i+2][j]
        if answer < temp_answer:
            answer = temp_answer
    if 3 <= i + 2 <= h and j + 3 <= w:
        temp_answer = paper[i][j] + paper[i][j+1] + paper[i-1][j+1] + paper[i][j+2]
        if answer < temp_answer:
            answer = temp_answer
    if i + 3 <= h and 3 <= j + 3 <= w:
        temp_answer = paper[i][j] + paper[i+1][j] + paper[i+1][j-1] + paper[i+2][j]
        if answer < temp_answer:
            answer = temp_answer

    return answer


for i in range(h):
    for j in range(w):
        temp_answer = check_paper(paper, i, j, h, w)
        if answer < temp_answer:
            answer = temp_answer

print(answer)
