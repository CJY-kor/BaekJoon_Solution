n = int(input())

numbers = list(map(int, input().split()))
answer = 0


def sum_two(number_list):
    temp_max1 = max(number_list)
    number_list.remove(temp_max1)
    temp_max2 = max(number_list)
    number_list.remove(temp_max2)

    number_list.append(temp_max1 + temp_max2)
    return temp_max1 * temp_max2


for _ in range(n-1):
    answer += sum_two(numbers)

print(answer)