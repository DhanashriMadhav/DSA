def count(list1):
    c0=0
    c1=0
    c2=0
    i=0
    while i < len(list1):
        if list1[i]==0:
            c0+=1
        elif list1[i]==1:
            c1+=1
        else:
            c2+=1
        i+=1
    j=0
    while (c0>0):
        list1[j]=0
        j+=1
        c0-=1
    while (c1>0):
        list1[j]=1
        j+=1
        c1-=1
    while (c2>0):
        list1[j]=2
        j+=1
        c2-=1

    return list1

size_of_array = int(input("enter the array size "))
arr1=[int(input("enter the elements between 0,1,2 ")) for each in range(size_of_array)]
print(count(arr1))