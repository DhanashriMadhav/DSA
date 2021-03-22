def vowcon(str1):
    vowels=0
    consonants=0
    for i in str1:
        if i in ("i","o","u","a","e","A","I","E","O","U"):
            vowels+=1
        else:
            consonants+=1
    print("no of vowels = ",vowels,"no of consonants = ",consonants)

str1=input("enter the string")
vowcon(str1)