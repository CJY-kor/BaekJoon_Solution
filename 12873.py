N = int(input())
people = []
temp = -1

for _ in range(N):
    people.append(_+1)

for i in range(1, N):
    temp = ((i*i*i - (i-1)*(i-1)*(i-1)) % len(people) + temp) % len(people)
    print(people[temp])
    del people[temp]
    temp -= 1

print(people[0])


