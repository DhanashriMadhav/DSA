openbrackets = ["[","{","("]
closebrackets = ["]","}",")"]
  
def check(str):
    stack = []
    for i in str:
        if i in openbrackets:
            stack.append(i)
        elif i in closebrackets:
            pos = closebrackets.index(i)
            if ((len(stack) > 0) and
                (openbrackets[pos] == stack[len(stack)-1])):
                stack.pop()
            else:
                return "Unbalanced"
    if len(stack) == 0:
        return "Balanced"
    else:
        return "Unbalanced"
  
str=input("enter the string")
print(str,"-", check(str))
  
