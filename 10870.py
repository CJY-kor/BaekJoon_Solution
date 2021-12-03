"""
문제
피보나치 수는 0과 1로 시작한다. 0번째 피보나치 수는 0이고, 1번째 피보나치 수는 1이다.
그 다음 2번째 부터는 바로 앞 두 피보나치 수의 합이 된다.

이를 식으로 써보면 Fn = Fn-1 + Fn-2 (n ≥ 2)가 된다.

n=17일때 까지 피보나치 수를 써보면 다음과 같다.

0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597

n이 주어졌을 때, n번째 피보나치 수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 n이 주어진다. n은 20보다 작거나 같은 자연수 또는 0이다.

출력
첫째 줄에 n번째 피보나치 수를 출력한다.
"""

"""
풀이
1. n을 입력 받는다. list 형태의 변수 numbers 를 0 ~ n 만큼의 index 로 초기화한다.

2. 피보나치 수를 계산하는 함수를 구현한다.
    피보나치 수를 계산하는 함수 (다이나믹 프로그래밍을 이용함)
    1) n을 입력 받는다.
    2) 0부터 n까지 다음 과정을 수행한다.
        - if i == 0
        numbers[i] = 0
        - if i == 1
        numbers[i] = 1
        - if numbers[i] == None
        numbers[i] = numbers[i-1] + numbers[i-2]

3. numbers[n] 출력  
"""

n = int(input())
numbers = [None for _ in range(n+1)]


def calculate_fib(n):

    for i in range(n+1):
        if i == 0:
            numbers[i] = 0
        elif i == 1:
            numbers[i] = 1
        elif numbers[i] is None:
            numbers[i] = numbers[i-1] + numbers[i-2]


calculate_fib(n)
print(numbers[n])
