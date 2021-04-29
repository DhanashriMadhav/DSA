def Activities(s, f,n ):
   n = len(f)
   print ("The selected activities are:")
   i = 0
   print (i,end=" ")
   for j in range(n):
         if s[j] >= f[i]:
            print (j,end=" ")
            i = j
size = int(input("enter the size of array"))
s = [int(input("enter the elements"))for each in range(size)]
f = [int(input("enter the elements"))for each in range(size)]
Activities(s, f,size)
