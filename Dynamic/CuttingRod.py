min = -32767
 
def cutRod(price, n):
    val = [0 for x in range(n+1)]
    val[0] = 0
    for i in range(1, n+1):
        maxVal = min
        for j in range(i):
             maxVal = max(maxVal, price[j] + val[i-j-1])
        val[i] = maxVal
 
    return val[n]
 
size = int(input("enter the size of array"))
arr = [int(input("enter the proces")) for each in range(size)]
maxprice = (cutRod(arr, size))
print("Maximum price is ",maxprice )
