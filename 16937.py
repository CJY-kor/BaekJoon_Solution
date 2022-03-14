h, w = list(map(int, input().split()))
n = int(input())
stickers = []
temp_answer = 0
answer = 0

for _ in range(n):
    stickers.append(list(map(int, input().split())))


def if_match(sticker1, sticker2, h, w):
    if (sticker2[0] > h or sticker2[1] > w) and (sticker2[0] > w or sticker2[1] > h):
        return 0

    if sticker1[0] <= (h - min(sticker2)) and sticker1[1] <= w:
        return sticker1[0] * sticker1[1] + sticker2[0]*sticker2[1]
    elif sticker1[1] <= (h - min(sticker2)) and sticker1[0] <= w:
        return sticker1[0] * sticker1[1] + sticker2[0] * sticker2[1]
    elif sticker1[0] <= (w - min(sticker2)) and sticker1[1] <= h:
        return sticker1[0] * sticker1[1] + sticker2[0] * sticker2[1]
    elif sticker1[1] <= (w - min(sticker2)) and sticker1[0] <= h:
        return sticker1[0] * sticker1[1] + sticker2[0] * sticker2[1]
    else:
        return 0


for i in range(n):
    for j in range(i+1, n):
        temp_answer = if_match(stickers[i], stickers[j], h, w)
        if answer < temp_answer:
            answer = temp_answer

print(answer)

