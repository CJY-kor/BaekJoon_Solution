import sys
input = sys.stdin.readline

N = int(input())

ring = list(map(int, input().split()))

def GCD(a, b):

    while b!= 0:
        remain = a % b
        a = b
        b = remain

    return a


target = ring.pop(0)


for i in range(N-1):
    num = GCD(target, ring[i])

    print('{}/{}'.format(target//num, ring[i]//num))
