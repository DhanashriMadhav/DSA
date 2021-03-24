def lower(arr1,row,col):
    for i in range(0,row):
        for j in range(0,col):
            if i<j:
                print(0,end=" ")
            else:
                print(arr1[i][j],end=" ")
        print()

def upper(arr1,row,col):
    for i in range(0,row):
        for j in range(0,col):
            if i>j:
                print(0,end=" ")
            else:
                print(arr1[i][j],end=" ")
        print()

row = int(input("enter the length of array"))
col = int(input("entet the length of each element"))
print("enter the elements of the array")
arr1=[]
for i in range (0,row):
    i=[]
    for j in  range(0,col):
        x=int(input("enter the elements"))
        i.append(x)
    arr1.append(i)
print(lower(arr1,row,col))
print(upper(arr1,row,col))
