#Upto 10 steps
n=int(input("Enter a number:"))
i=1
for i in range(1,11):
    a=i*n
    print(f"{n} x {i}={a}")
    i+=1
    