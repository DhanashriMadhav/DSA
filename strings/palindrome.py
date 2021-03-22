def palindrome(str1,n):
    if n<=1:
        return 1
    else:
        i=0
        while i <= n//2:
            if str1[i]!=str1[((n-1)-i)]:
                return 0
            i+=1
        return 1
str1= input("enter the string")
result=palindrome(str1,len(str1))
if result == 0:
    print("not palindrome")
else:
    print("palindrome")
