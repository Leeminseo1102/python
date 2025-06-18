class TreeNode() :
    def __init__ (self) :
        self.left = None
        self.data = None
        self.right = None

node1 = TreeNode()
node1.data = '라이엇'

node2 = TreeNode()
node2.data = '롤'
node1.left = node2

node3 = TreeNode()
node3.data = '발로란트'
node1.right = node3

node4 = TreeNode()
node4.data = '홍주'
node3.left = node4

node5 = TreeNode()
node5.data = '하성햄'
node3.right = node5



print(node1.data,end = ' ')
print()
print(node1.left.data,node1.right.data,end = ' ')
print()
print(node1.right.right.data,node1.right.left.data,end = ' ')
