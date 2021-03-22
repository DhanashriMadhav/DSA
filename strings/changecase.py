# change the case of string

def changeuppercase(str1):
    str2=""
    for i in str1:
        if ord(i)>=97 and ord(i)<=122:
            str2+=chr(ord(i)-32)
        else:
            str2+=i
    return(str2)

def changelowercase(str1):
    str2=""
    for i in str1:
        if ord(i)>=65 and ord(i)<=90:
            str2+=chr(ord(i)+32)
        else:
            str2+=i
    return(str2)
str1=input("enter the string")
print(changeuppercase(str1))
print(changelowercase(str1))
# def uppercase(str_data):
#     result = ''
#     for char in str_data:
#         if ord(char) >= 65:
#             result += chr(ord(char) - 32)
#     return result
# print(uppercase('abcdé--#λ'))