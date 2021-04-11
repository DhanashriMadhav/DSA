from queue import Queue
class BinaryTreeNode:
  def __init__(self, data):
    self.data = data
    self.leftChild = None
    self.rightChild=None
     
def insert(root,newValue):
  
        root=BinaryTreeNode(newValue)
        return root
    if newValue<root.data:
        root.leftChild=insert(root.leftChild,newValue)
    else:
        root.rightChild=insert(root.rightChild,newValue)
    return root
def levelorder(root):
    if root==None:
        return
    Q=Queue()
    Q.put(root)
    while(not Q.empty()):
        node=Q.get()
        if node==None:
            continue
        print(node.data)
        Q.put(node.leftChild)
        Q.put(node.rightChild)
     
root= insert(None,15)
insert(root,10)
insert(root,25)
insert(root,6)
insert(root,14)
insert(root,20)
insert(root,60)
print("Printing the level order traversal of the binary tree.")
levelorder(root)
