import sys

def secondmax(arr,arraysize):
    if arraysize < 2:
        print("size of array shoulb be atleast two")
        return
    if arraysize == 2:
        if arr[0]==arr[1]:
            print("both the no are same")
            return    
    Max = arr[0]
    sec_max = arr[0]
    for i in range(0,arraysize):
        if arr[i] > Max:
            sec_max=Max
            Max=arr[i]
        elif arr[i]<Max and arr[i]>sec_max:
            sec_max = arr[i]
    return print("the secondmax no is  ",sec_max)

def secondmin(arr,arraysize):
    if arraysize < 2:
        print("size of array shoulb be atleast two")
        return
    if arraysize == 2:
        if arr[0]==arr[1]:
            print("both the no are same")
            return    
    Min = sys.maxsize
    sec_min = sys.maxsize
    for i in range(0,arraysize):
        if arr[i] < Min:
            sec_min=Min
            Min=arr[i]
        elif arr[i]> Min and arr[i]<sec_min:
            sec_min = arr[i]
    if (sec_min == sys.maxsize):
        return print("no seconmin no ")
    else:
        return print("the secondmin no is  ",sec_min)


size_of_array = int(input("enter the array size "))
arr1=[int(input()) for each in range(size_of_array)]
secondmax(arr1,size_of_array)
secondmin(arr1,size_of_array)