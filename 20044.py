n = int(input())

numbers = list(map(int, input().split()))
answer = 2000000
temp_answer = 0


def find_min(number_list):
    temp_min = min(number_list)
    temp_max = max(number_list)
    for i in number_list:
        if i == temp_min:
            number_list.remove(temp_min)
            number_list.remove(temp_max)
            return temp_min + temp_max


for _ in range(n):
    temp_answer = find_min(numbers)
    if temp_answer < answer:
        answer = temp_answer

print(answer)