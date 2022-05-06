class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BST:
    def __init__(self, root):
        self.root = root

    def Insert(self, data):
        self.root = self.InsertP(self.root, data)
        return self.root is not None

    def InsertP(self, node, data):
        if node is None:
            node = Node(data)
        else:
            if data <= node.data:
                node.left = self.InsertP(node.left, data)
            else:
                node.right = self.InsertP(node.right, data)
        return node

    def Search(self, key):
        return self.SearchP(self.root, key)

    def SearchP(self, root, key):
        if root is None or root.data == key:
            return root is not None
        elif key < root.data:
            return self.SearchP(root.left, key)
        else:
            return self.SearchP(root.right, key)

    def Delete(self, key):
        self.root, deleted = self.deleteP(self.root, key)
        return deleted

    def deleteP(self, node, key):
        if node is None:
            return node, False

        deleted = False
        # 해당 노드가 삭제할 노드일 경우
        if key == node.data:
            deleted = True
            # 삭제할 노드가 자식이 두개일 경우
            if node.left and node.right:
                # 오른쪽 서브 트리에서 가장 왼쪽에 있는 노드를 찾고 교체
                parent, child = node, node.right
                while child.left is not None:
                    parent, child = child, child.left
                child.left = node.left
                if parent != node:
                    parent.left = child.right
                    child.right = node.right
                node = child
            # 자식 노드가 하나일 경우 해당 노드와 교체
            elif node.left or node.right:
                node = node.left or node.right
            # 자식 노드가 없을 경우 그냥 삭제
            else:
                node = None
        elif key < node.data:
            node.left, deleted = self.deleteP(node.left, key)
        else:
            node.right, deleted = self.deleteP(node.right, key)
        return node, deleted

def main():
    """
    설명 : 이 함수는 배열의 주요기능들을 구현한 함수들이 실행되는 함수이다.
    여기서는 's', 'i', 'd', 'q' 를 입력하면 각각 배열의
    'search', 'insert', 'delete', 'quit' 를 수행한다.
    """

    print("s, i, d, q 중 하나를 입력하세요.")

    root = Node
    bst = BST(root)
    bst.root.data = 999
    bst.root.left = None
    bst.root.right = None

    while True:
        main_input = input()


        if main_input == 's':
            print("search 할 값을 입력하세요.")
            main_value = int(input())
            print(bst.Search(main_value))

        elif main_input == 'i':
            print("insert 할 값을 입력하세요.")
            main_value = int(input())
            bst.Insert(main_value)

        elif main_input == 'd':
            print("delete 할 값을 입력하세요.")
            main_value = int(input())
            print(bst.Delete(main_value))

        elif main_input == 'q':
            break
        else:
            print("s, i, d, q 중 하나를 입력하세요.")


main()