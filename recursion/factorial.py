def factorial(num):
    if num == 1:
        return num
    else :
        return num*factorial(num-1)

num = int(input("enter the no"))
print(factorial(num))    