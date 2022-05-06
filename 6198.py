import sys
input = sys.stdin.readline

n = int(input())
result = 0
stack = [0]
sequence = []

for _ in range(n):
    sequence.append(int(input()))

for i in range(n):
    while stack != [] and stack[-1] <= sequence[i]:
        stack.pop()
    stack.append(sequence[i])
    result += len(stack)-1
print(result)