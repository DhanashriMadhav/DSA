from binarytree import build
size= int(input("enter the no of nodes you want to add in the trees"))
nodes=[]
for i in range(size):
  num=int(input("enter the node value"))
  nodes.append(num)
 
binary_tree = build(nodes)

print('Binary tree from list :\n',
      binary_tree)
print('\nList from binary tree :', 
      binary_tree.values)
