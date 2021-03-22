def wordcount(str1):
    count=0
    s=""
    i=0
    while i <len(str1):
        if (str1[i])==" ":
            s=""
            count+=1
        else:
            s+=str1[i]
        i+=1
    count+=1
    return count

str1=input("enter the sentense ")
print("the total no of words in the string are ",wordcount(str1))