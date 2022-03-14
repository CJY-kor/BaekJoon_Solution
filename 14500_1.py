h, w = list(map(int, input().split()))
paper = []
temp_answer = 0
answer = 0

for _ in range(h):
    paper.append(list(map(int, input().split())))


def check_paper(paper, i, j, h, w, checker, direction):

    if checker == 4:
        return 0

    if i < 0 or i >= h or j < 0 or j >= w:
        return 0

    if direction == 1:
        return paper[i][j] + max(check_paper(paper, i+1, j, h, w, checker+1, 2), check_paper(paper, i, j-1, h, w, checker+1, 3), check_paper(paper, i-1, j, h, w, checker+1, 4))

    if direction == 2:
        return paper[i][j] + max(check_paper(paper, i, j+1, h, w, checker+1, 1), check_paper(paper, i, j-1, h, w, checker+1, 3), check_paper(paper, i-1, j, h, w, checker+1, 4))

    if direction == 3:
        return paper[i][j] + max(check_paper(paper, i+1, j, h, w, checker+1, 2), check_paper(paper, i, j+1, h, w, checker+1, 1), check_paper(paper, i-1, j, h, w, checker+1, 4))

    if direction == 4:
        return paper[i][j] + max(check_paper(paper, i+1, j, h, w, checker+1, 2), check_paper(paper, i, j-1, h, w, checker+1, 3), check_paper(paper, i, j+1, h, w, checker+1, 1))


for i in range(h):
    for j in range(w):
        temp_answer = check_paper(paper, i, j, h, w, 0, 3)
        if answer < temp_answer:
            answer = temp_answer

print(answer)