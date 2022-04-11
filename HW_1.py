def main():
    """
    설명 : 이 함수는 배열의 주요기능들을 구현한 함수들이 실행되는 함수이다.
    여기서는 's', 'i', 'd', 'q' 를 입력하면 각각 배열의
    'search', 'insert', 'delete', 'quit' 를 수행한다.
    """

    main_list = [0 for _ in range(100)]
    main_input = ''
    main_value = 0
    size = 0

    print("s, i, d, q 중 하나를 입력하세요.")

    while True:
        for _ in main_list:
            if _ != 0:
                print(_, end=' ')
        print()
        main_input = input()

        if main_input == 's':
            print("search 할 값을 입력하세요.")
            main_value = int(input())
            print(srch(main_value, main_list))

        elif main_input == 'i':
            print("insert 할 값을 입력하세요.")
            main_value = int(input())
            insrt(main_value, main_list, size)
            size += 1

        elif main_input == 'd':
            print("delete 할 값을 입력하세요.")
            main_value = int(input())
            print(dlte(main_value, main_list, size))
            size -= 1

        elif main_input == 'q':
            break
        else:
            print("s, i, d, q 중 하나를 입력하세요.")


def insrt(value, list, size):
    """

    :param value: list에 추가할 값이다.
    :param list: 배열을 입력 받는다.
    :return:
    """
    list[size] = value


def srch(value, list):
    """

    :param value: 확인할 값을 입력받는다.
    :param list: 배열을 입력 받는다.
    :return: 배열에 value 값이 존재하면 "value is exist"를 출력
    없을 경우에는 "value is not exist를 출력한다.
    """
    for _ in list:
        if _ == value:
            return "value is exist"
    return "value is not exist"


def dlte(value, list, size):
    """

    :param value: 지울 값을 입력받는다.
    :param list: 배열을 입력받는다.
    :param size: 배열의 사이즈를 입력받는다.
    :return: 배열에 delete 할 값이 있을경우 "deleted"를 출력
    없을 경우에는 "not deleted"를 출력
    """
    for i in range(size):
        if list[i] == value:
            list[i] = list[size-1]
            list[size-1] = 0
            return "deleted"
    return "not deleted"


def bianry_srch(value, list, size):
    s, e = 0, size - 1
    m = int((s + e) / 2)

    while s <= e:
        m = int((s + e) / 2)
        if list[m] == value:
            return "value is exist"
        elif list[m] > value:
            e = m - 1
        else:
            s = m + 1
    return "value is not exist"


def binary_insrt(value, list, size):
    left, right = 0, size-1

    while left <= right:
        m = int((left + right) / 2)
        if list[m] == value:
            left = m
            right = m
            break
        elif list[m] > value:
            right = m - 1
        else:
            left = m + 1

    for i in range(size-1, right-1, -1):
        list[i+1] = list[i]
    list[right] = value


main()