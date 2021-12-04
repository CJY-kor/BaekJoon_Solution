"""
문제
재귀 호출만 생각하면 신이 난다! 아닌가요?

다음과 같은 재귀함수 w(a, b, c)가 있다.

if a <= 0 or b <= 0 or c <= 0, then w(a, b, c) returns:
    1

if a > 20 or b > 20 or c > 20, then w(a, b, c) returns:
    w(20, 20, 20)

if a < b and b < c, then w(a, b, c) returns:
    w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)

otherwise it returns:
    w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
위의 함수를 구현하는 것은 매우 쉽다. 하지만, 그대로 구현하면 값을 구하는데 매우 오랜 시간이 걸린다.
(예를 들면, a=15, b=15, c=15)

a, b, c가 주어졌을 때, w(a, b, c)를 출력하는 프로그램을 작성하시오.

입력
입력은 세 정수 a, b, c로 이루어져 있으며, 한 줄에 하나씩 주어진다.
입력의 마지막은 -1 -1 -1로 나타내며, 세 정수가 모두 -1인 경우는 입력의 마지막을 제외하면 없다.

출력
입력으로 주어진 각각의 a, b, c에 대해서, w(a, b, c)를 출력한다.
"""
"""
풀이 
동적 계획법을 이용한다. 즉 재귀를 사용하지 않고 List 자료형을 이용하여
각각의 사례를 List(numbers)에 채워넣는 방식으로 구현한다.

1. 입력값을 받는다. numbers 라는 list변수를 초기화한다.

2. w 함수를 구현한다.

if a < 0 or b < 0 or c < 0:
    return 1

if numbers[a][b][c] is None:

    if a <= 0 or b <= 0 or c <= 0, then w(a, b, c) returns:
        numbers[a][b][c] = 1
        1

    if a > 20 or b > 20 or c > 20, then w(a, b, c) returns:
        w(20, 20, 20)

    if a < b and b < c, then w(a, b, c) returns:
        numbers[a][b][c] = w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
        w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)

    otherwise it returns:
        numbers[a][b][c] = w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
        w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
        
else:
    
    return numbers[a][b][b]
    
3. 결과값을 출력한다.

index error 때문에 실제 코드와 풀이 사이에 차이가 생겼다.
"""


numbers = [[[None for _ in range(21)] for _ in range(21)] for _ in range(21)]  # 1


def w(x, y, z):  # 2

    if x <= 0 or y <= 0 or z <= 0:
        numbers[0][0][0] = 1
        return 1

    if x > 20 or y > 20 or z > 20:
        return w(20, 20, 20)

    if numbers[x][y][z] is None:

        if x < y < z:
            numbers[x][y][z] = w(x, y, z-1) + w(x, y-1, z-1) - w(x, y-1, z)
            return w(x, y, z-1) + w(x, y-1, z-1) - w(x, y-1, z)
        else:
            numbers[x][y][z] = w(x-1, y, z) + w(x-1, y-1, z) + w(x-1, y, z-1) - w(x-1, y-1, z-1)
            return w(x-1, y, z) + w(x-1, y-1, z) + w(x-1, y, z-1) - w(x-1, y-1, z-1)

    else:
        return numbers[x][y][z]


while True:
    a, b, c = list(map(int, input().split()))  # 1
    if a == -1 and b == -1 and c == -1:
        break
    print("w(%d, %d, %d) = %d" %(a, b, c, w(a, b, c)))

