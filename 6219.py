import math
import sys
input = sys.stdin.readline


def is_prime_num(n):
    for i in range(2, int(math.sqrt(n))+1): # n의 제곱근을 정수화 시켜준 후 + 1
        if n % i == 0:
            return False

    return True


A, B, D = list(map(int, input().split()))
D = str(D)

temp_number = list(range(A,B+1))
decimal_number = []

for i in temp_number:
    if is_prime_num(i) and D in str(i):
        decimal_number.append(i)

print(len(decimal_number))


