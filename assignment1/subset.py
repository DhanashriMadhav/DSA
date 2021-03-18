def Subset(list1,list2,list1_len,list2_len) : 
    count=0
    dic={} 
    for i in range(list1_len): 
        if list1[i] not in dic: 
            dic[list1[i]] = 0
        dic[list1[i]] += 1
    for i in range(list2_len):  
        if list2[i] not in dic: 
            count += 1
            break  
        else : 
            dic[list2[i]] -= 1
              
            if (dic[list2[i]] == 0): 
                dic.pop(list2[i]) 
    return count  
      

size_of_array1 = int(input("enter the array size 1"))
arr1=[int(input()) for each in range(size_of_array1)]
size_of_array2 = int(input("enter the array size "))
arr2=[int(input()) for each in range(size_of_array2)]
  
status = Subset(arr1, arr2, size_of_array1, size_of_array2)
if status==0:
    print("arr2[] is subset of arr1[] ") 
else: 
    print("arr2[] is not a subset of arr1[]") 