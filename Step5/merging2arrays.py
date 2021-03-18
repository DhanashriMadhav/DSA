def merge(arr1,arr2,m,n):
    union=[]
    i=0
    j=0
    while i<m and j<n:
        if arr1[i]<arr2[j]:
            union.append(arr1[i])
            i+=1
        elif arr1[i]>arr2[j]:
            union.append(arr2[j])
            j+=1
        else:

            union.append(arr1[i])
            i+=1
            j+=1
    while i<m:
        union.append(arr1[i])
        i+=1
    while j<n:
        union.append(arr2[j])
        j+=1

    print(arr1)
    print(arr2)
    print (union)
len1=int (input("enter the size of array 1"))
arr1=[int(input(" enter the elements of array")) for each in range(len1)]
len2=int(input("enter the size of the array2"))
arr2=[int(input(" enter the elements of array")) for each in range(len2)]

merge(arr1,arr2,len1,len2)