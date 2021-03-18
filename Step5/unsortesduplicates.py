def unsorted(arr1,m):
    hash=[]
    for i in range(m):
        if arr1[i] not in hash:
            hash.append(arr1[i])
        else:
            print("duplicate element ",arr1[i])

len1=int (input("enter the size of array 1"))
arr1=[int(input(" enter the elements of array")) for each in range(len1)]
unsorted(arr1,len1)