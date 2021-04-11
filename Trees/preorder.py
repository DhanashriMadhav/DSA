from collections import deque

def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
 
def preorderIterative(root):
 
    # return if the tree is empty
    if root is None:
        return
 
    stack = deque()
    stack.append(root)
 
   
    while stack:
 
        curr = stack.pop()
 
        print(curr.data, end=' ')
 
        if curr.right:
            stack.append(curr.right)
 
        if curr.left:
            stack.append(curr.left)
 
   
 
if __name__ == '__main__':

    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.right.left = Node(5)
    root.right.right = Node(6)
    root.right.left.left = Node(7)
    root.right.left.right = Node(8)
 
    preorderIterative(root)
 
