def bubbleSort(arr): 
    n = len(arr) 

    for i in range(n): 

        for j in range(0, n-i-1): 

            if arr[j] > arr[j+1] : 
                arr[j], arr[j+1] = arr[j+1], arr[j] 
    return print(arr)

len1=int(input("enter the size of the array"))
arr=[int(input("enter the elements")) for each in range(len1)]
bubbleSort(arr) 
  