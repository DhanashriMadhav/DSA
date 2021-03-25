# Find if Given number is power of 2 or not.
# More specifically, find if given number can be expressed as 2^k where k >= 1.

# Input:

# number length can be more than 64, which mean number can be greater than 2 ^ 64 (out of long long range)
# Output:

# return 1 if the number is a power of 2 else return 0

# Example:

# Input : 128
# Output : 1

def power(A):
        if len(A)==0:
            return 0
        A=int(A)
        if A==0 or A== 1:
            return 0
        else:
            while (A!=1):
                A/=2
                if(A % 2 != 0 and A != 1):
                    return 0
            else:
                return 1
num = input("enter the no")
x=power(num)
if x == 1:
    print("it is a power of 2")
else:
    print("it is not power of 2")
