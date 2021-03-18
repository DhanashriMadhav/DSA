def maxno(arr1,m):
    maximum=0
    for i in range(m):
        if arr1[i]>maximum:
            maximum=arr1[i]
    return print("maximum no is ",maximum)

def minno(arr1,m):
    minimum=arr1[0]
    for i in range(m):
        if arr1[i]<minimum:
            minimum=arr1[i]
    return print("minimum no is ",minimum)

len1=int (input("enter the size of array 1"))
arr1=[int(input(" enter the elements of array")) for each in range(len1)]
maxno(arr1,len1)
minno(arr1,len1)