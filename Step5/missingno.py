def missingno(arr1,m):
    n=arr1[-1]
    totalsum=n*(n+1)/2
    sum=0
    for i in range (m):
        sum+=arr1[i]
    return print("the missing no is ",totalsum-sum)
    
len1=int (input("enter the size of array 1"))
arr1=[int(input(" enter the elements of array")) for each in range(len1)]

missingno(arr1,len1)