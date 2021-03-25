# Given two numbers represented as strings, return multiplication of the numbers as a string.

#  Note: The numbers can be arbitrarily large and are non-negative.
# Note2: Your answer should not have leading zeroes. For example, 00 is not a valid answer. 
# For example,
# given strings "12", "10", your answer should be “120”.

def multiply(A, B):
        if len(A)==0 or len(B)==0:
            return 0
        m=int(A)
        n=int(B)
        return print(m*n)
A=input("enter the no")
B=input("enter the second no")
multiply(A,B)
