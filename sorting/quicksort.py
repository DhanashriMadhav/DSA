def partition(arr1,low,high): 
	i = ( low-1 )		 
	pi = arr1[high]	 
	for j in range(low , high): 		
		if arr1[j] <= pi: 
			i = i+1
			arr1[i],arr1[j] = arr1[j],arr1[i] 
	arr1[i+1],arr1[high] = arr1[high],arr1[i+1] 
	return ( i+1 ) 

def quickSort(arr1,low,high): 
	if low < high: 
		pi = partition(arr1,low,high) 
		quickSort(arr1, low, pi-1) 
		quickSort(arr1, pi+1, high)
	
len1=int(input("enter the size of the arr1ay"))
arr1=[int(input("enter the elements")) for each in range(len1)]
print(quickSort(arr1,0,len1-1)) 
