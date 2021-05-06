#VERTICAL CONCENTATION OF MATRIX
arr = [["Gfg", "good"], ["is", "for"], ["Best"]]
print("The original list : " + str(arr))
  

res = []
N = 0
while N != len(arr):
    temp = ''
    for idx in arr:
         
        try: temp = temp + idx[N]
        except IndexError: pass
    res.append(temp)
    N = N + 1
  
res = [ele for ele in res if ele]
  
print("List after column Concatenation : " + str(res))
