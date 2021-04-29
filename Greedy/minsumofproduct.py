def minValue(A, B, n):
    A.sort()
    B.sort()
    result = 0
    for i in range(n):
        result += (A[i] * B[n - i - 1])
 
    return result
size = int(input("enter the size of array"))
A = [int(input("enter the element")) for each in range(size)]
B = [int(input("enter the element")) for each in range(size)]
print minValue(A, B, size)
 
