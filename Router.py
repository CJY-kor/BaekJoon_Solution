N = int(input())

temp = 0

temp_list = []

while temp != -1:
    temp = int(input())
    if temp == 0:
        del temp_list[0]
    elif temp != -1:
        temp_list.append(temp)

for _ in temp_list:
    print(str(_)+" ", end='')


