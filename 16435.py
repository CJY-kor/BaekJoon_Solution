n, m = list(map(int, input().split()))
m = [m]

numbers = list(map(int, input().split()))


def grow(number_list, m):
    for i in number_list:
        if i <= m[0]:
            m[0] += 1
            number_list.remove(i)


for _ in range(n):
    grow(numbers, m)

print(m[0])