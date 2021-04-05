def remove(str):
    if not str:
        return ""
    elif len(str)==1:
        return str
    elif str[0]==str[1]:
        return remove(str[1:])
    else:
        return str[0]+remove(str[1:])

str = input('enter the string')
print(remove(str))