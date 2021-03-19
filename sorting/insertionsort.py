def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j] :
                arr[j + 1] = arr[j]
                j -= 1
        arr[j + 1] = key
    return print(arr)

len1=int(input("enter the size of the array"))
arr=[int(input("enter the elements")) for each in range(len1)]
insertionSort(arr)
