from collections import deque
 
 
# Data structure to store a binary tree node
class Node:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
 
def inorderIterative(root):
 
    stack = deque()
 
    curr = root
 
    while stack or curr:
 
        if curr:
            stack.append(curr)
            curr = curr.left
        else:
            curr = stack.pop()
            print(curr.data, end=' ')
 
            curr = curr.right
 
 
if __name__ == '__main__':
 
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.right.left = Node(5)
    root.right.right = Node(6)
    root.right.left.left = Node(7)
    root.right.left.right = Node(8)
 
    inorderIterative(root)
 
