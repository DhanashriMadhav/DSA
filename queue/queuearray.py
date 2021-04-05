queue = []
def addqueue(*a):
    for i in a:
        queue.append(i)
    return queue

def pop(queue):
    while len(queue)>0:
        print("poped element of the queue ",queue.pop(0))
    

print(addqueue(1,2,3,4,5,6,7,8))
pop(queue)