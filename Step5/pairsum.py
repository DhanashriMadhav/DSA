def pairsum(list1,sum):
    list1.sort()
    max_no=len(list1)-1
    min_no=0
    while min_no<max_no:
        if list1[min_no]+list1[max_no]==sum:
            print("pair found",list1[max_no],list1[min_no])
        if list1[min_no]+list1[max_no]<sum:
            min_no+=1
        else:
            max_no-=1
num=int(input("how many element you want in list"))
list1=[int(input("enter the no")) for each in range(num)]
sum=int(input("enter the number for sum"))
pairsum(list1,sum)