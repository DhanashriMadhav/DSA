
size = int(input("enter the size of the array"))
arr = [int(input("enter the elemet")) for each in range(size)]
 
print("The original list is : " + str(arr))
  
K = int(input("enter the element to be removed from each number"))
  
res = []
for ele in test_list:
  
    if list(set(str(ele)))[0] == str(K) and len(set(str(ele))) == 1:
        res.append('')
    else:
        res.append(int(''.join([el for el in str(ele) if int(el) != K])))
print("Modified List : " + str(res))
