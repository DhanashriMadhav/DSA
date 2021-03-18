def missingelement(arr1, len1): 
    b=[0]*((arr1[-1])+1)
    m=len(b)
    for i in range(len1):
        b[arr1[i]]=1
    for i in range(m):
        if b[i]==0:
            print(i)
len1=int (input("enter the size of array 1"))
arr1=[int(input(" enter the elements of array")) for each in range(len1)]

missingelement(arr1, len1) 
 