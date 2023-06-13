# 이진 트리용 노드
# 연결 리스트로 구현해서 메모리 문제 해결

class Tnode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    # 세가지 순회 방식이 있다 (전위 / 중위 / 후위)
    # 전위 순회 방식
    def preorder(self):
        if self.data is not None:
            print(self.data, end='')
            preorder(self.left)
            preorder(self.right)
    
    def inorder(n):
        if n is not None:
            inorder(n.left)
            print(n.data, end=' ')
            inorder(n.right)
    
    def postorder(n):
        if n is not None:
            postorder(n.left)
            postorder(n.right)
            print(n.data, end=' ')

alex = Tnode(1)

alex.inorder()