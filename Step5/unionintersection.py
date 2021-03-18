def union(arr1,arr2,m,n):
    union1=[]
    for i in range(m):
        if arr1[i] not in union1:
            union1.append(arr1[i])
    for j in range(n):
        if arr2[j] not in union1:
            union1.append(arr2[j])
    print(union1)

def intersection(arr1,arr2,m,n):
    intersection1=[]
    for i in range(m):
        intersection1.append(arr1[i])
    for i in range(n):
        if arr2[i] in intersection1:
            print(arr2[i])

arr1_size=int(input("enter the size of array"))
arr1=[int(input("enter the element ")) for each in range( arr1_size)]
arr2_size=int(input("enter the size of array"))
arr2=[int(input("enter the element ")) for each in range( arr2_size)]
union(arr1,arr2,arr1_size,arr2_size)
intersection(arr1,arr2,arr1_size,arr2_size)