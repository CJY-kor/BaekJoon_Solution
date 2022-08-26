class Node:  # 각 노드를 대표하는 클래스를 구현
    def __init__(self, value, height, left = None, right = None):  # node를 구분하기 위해 value를 그리고 오른쪽 좌측 노드의 정보를 받는다.
        self.value = value
        self.height = height
        self.left = left
        self.right = right


class AvlTree:
    def __init__(self):  # root 변수를 초기화 한다.
        self.root = None

    def height(self, n):  # node의 height를 반환한다.
        if n == None:
            return 0
        return n.height

    def put(self, value):  # put_node 함수를 이용하여 node를 추가한다.
        self.root = self.put_node(self.root, value)

    def put_node(self, n, value):
        if n == None:  # 해당 위치에 자리가 없다면 Node class를 선언하여 넣는다.
            return Node(value, 1)
        if n.value > value:  # 부모의 value 보다 넣을 값이 작다면 왼쪽 가지에 값을 넣는다.
            n.left = self.put_node(n.left, value)
        elif n.value < value:  # 부모의 value 보다 넣을 값이 크다면 오른쪽 가지에 값을 넣는다.
            n.right = self.put_node(n.right, value)
        n.height = max(self.height(n.left), self.height(n.right))+1  # 값을 넣고 나서 높이를 보정해준다.
        return self.balance(n)  # 노드를 넣은 뒤 balance 작업을 해준다.

    def balance(self, n):  # tree의 불균형을 잡는 작업.

        if self.bf(n) > 1:  # 왼쪽 서브트리 불균형
            if self.bf(n.left) < 0:  # 노드 n의 왼쪽 자식의 오른쪽 서브트리가 높은 경우
                n.left = self.rotate_left(n.left) # LR
            n = self.rotate_right(n)  # LL

        elif self.bf(n) < -1:  # 오른쪽 서브트리 불균형
            if self.bf(n.right) > 0:  # 노드 n의 오른쪽 자식의 왼쪽 서브트리가 높은 경우
                n.right = self.rotate_right(n.right)  #RL
            n = self.rotate_left(n)  #RR

        return n

    def bf(self, n):
        return self.height(n.left)-self.height(n.right)

    def rotate_right(self, n): #오른쪽 회전
        x = n.left
        n.left = x.right
        x.right = n
        n.height = max(self.height(n.left), self.height(n.right)) + 1
        x.height = max(self.height(x.left), self.height(x.right)) + 1
        return x

    def rotate_left(self, n): #왼쪽 회전
        x = n.right
        n.right = x.left
        x.left = n
        n.height = max(self.height(n.left), self.height(n.right)) + 1
        x.height = max(self.height(x.left), self.height(x.right)) + 1
        return x

    def print_value(self, n):
        if n.left:
            self.print_value(n.left)
        print('  ' * n.height, str(n.value))
        if n.right:
            self.print_value(n.right)


def main():
    """
    설명 : 이 함수는 배열의 주요기능들을 구현한 함수들이 실행되는 함수이다.
    여기서는 's', 'i', 'd', 'q' 를 입력하면 각각 배열의
    'search', 'insert', 'delete', 'quit' 를 수행한다.
    """

    print("s, i, d, q 중 하나를 입력하세요.")

    avl = AvlTree()

    while True:
        main_input = input()

        if main_input == 's':
            print("search 할 값을 입력하세요.")
            main_value = int(input())

        elif main_input == 'i':
            print("insert 할 값을 입력하세요.")
            main_value = int(input())
            avl.put(main_value)
            avl.print_value(avl.root)

        elif main_input == 'd':
            print("delete 할 값을 입력하세요.")
            main_value = int(input())

        elif main_input == 'q':
            break
        else:
            print("s, i, d, q 중 하나를 입력하세요.")


main()


