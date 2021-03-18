def maxdiff(arr, n): 
    diff = []
    for i in range (0, n-1): 
        dif = arr[i+1] - arr[i] 
        diff.append(dif)     
    max_diff = diff[0] 
    for i in range(1, n-1): 
        if (diff[i-1] > 0): 
            diff[i] += diff[i-1] 
        if (max_diff < diff[i]): 
            max_diff = diff[i]   
    return max_diff
size_of_array = int(input("enter the array size "))
arr1=[int(input()) for each in range(size_of_array)]
print(maxdiff(arr1,size_of_array))