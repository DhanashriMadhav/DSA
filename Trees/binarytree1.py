class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
        
def inorder(root):
 
    if root is None:
        return
 
    inorder(root.left)
    print(root.data, end=' ')
    inorder(root.right)
 
def createTree(parent):
 
    dict = {}
 
    for i in range(len(parent)):
        dict[i] = Node(i)
    root = None

    for i, e in enumerate(parent):
        if e == -1:
            root = dict[i]
        else:
            ptr = dict[e]
            if ptr.left:
                ptr.right = dict[i]
            else:
                ptr.left = dict[i]
    return root
parent = [] 
size=int(input("enter the size of the array"))
for i in range (size):
  num=int(input("enter the value of node"))
  parent.append(num) 
root = createTree(parent)
inorder(root)
 

