l=int(input("enter lower range:"))
u=int(input("enter upper range:"))
print("Prime numbers within given range are........:\n")
for i in range(l,u+1):#Range exclude uper limit
    if i>1:#negative numbers are not prime
        for j in range(2,i):
            if (i%j)==0:
                break
        else:
            print(i)