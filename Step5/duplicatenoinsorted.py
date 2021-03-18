def duplicate(arr1,m):
    i=0
    while i<m-1:
        if arr1[i]!=arr1[i+1]:
            i+=1
        else :
            if arr1[i-1]!=arr1[i]:
                print(arr1[i])
                i+=1
            else:
                i+=1
len1=int (input("enter the size of array 1"))
arr1=[int(input(" enter the elements of array in ascending manner")) for each in range(len1)]    
duplicate(arr1,len1)
