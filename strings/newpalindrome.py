
# Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

# Example:

# "A man, a plan, a canal: Panama" is a palindrome.

# "race a car" is not a palindrome.

# Return 0 / 1 ( 0 for false, 1 for true ) for this problem                  

def isPalindrome(A):
        b=[]
        x=len(A)
        if len(A)==0:
            return 1
        else :
            i =len(A)-1
            while i>=0:
                if A[i].isalnum():
                    b.append(A[i])
                i-=1
        
            j=0
            c=[]
            while j<len(A):
                if A[j].isalnum():
                    c.append(A[j])
                j+=1
            b = [each_string.lower() for each_string in b]
            c = [each_string.lower() for each_string in c]
            
            if c==b:
                return 1
            else:
                return 0
            
str1=input("enter the string")
x=isPalindrome(str1)
if x==1:
    print("palindrome")
else:
    print("not palindrome")