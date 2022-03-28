# 22/03/14
import sys
input = sys.stdin.readline()

n = int(input())

def make_equation(n):
    if n < 16 or n > 46 or n == 17:
        print('impossible')
    else:
        a, b, c, d, e, f = 1, 1, 1, 1, 1, 1
        temp = n - 16

