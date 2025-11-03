num1=int(input("Enter num1:"))
num2=int(input("Enter num2:"))
#Arithmetic Operators
print("Arithmetic operations:")
print("addition:",num1+num2)
print("Subtraction:",num1-num2)
print("Multiplication:",num1*num2)
print("Division:",num1/num2)
print("Floor Division:",num1//num2)

#Relational Operators
print("\n Relational Operations:")

print(num1 > num2)   
print(num1 < num2)  
print(num1 == num2)
print(num1 != num2) 
print(num1 >= num2)  
print(num1 <= num2)  

#Assignment Operators
print("\n Assignment operations:")
num1 += 1
print("Increment by 1:",num1)
num2 -= 1
print("Decrement by 1:",num2)
num1 *= 2
print("Multiply by 2:",num1)#num1 value updated
num2 /= 2
print("Divide by 2:",num2)

#Logical Operators
print("\n Logical operations:") 
print(num1>0 and num2>0)
print(num1<0 or num2>0)
print(not ( num1>0))

#Bitwise operators
print("\n Bit wise operations:")
print("AND:",num1&int(num2))#11->1;01,10,00->0 #bitwise AND is only works for integers
print("OR:",num1 | int(num2))#11,10,01->1 ;00->0
print("XOR:",num1^int(num2))#00, 11->1; 01, 10->0
print("NOT",~num1)
print("Left shift:",int(num1)<<1)#num*2
print("Right shift:",int(num2)>>1)#num2/2

#Ternary operators
print("\n ternary operations:")
minimum=num1 if num1<num2 else num2
print("Minimum value:",minimum)

#Membership operator
print("\n Membership operations:")
vowels=['a','e','i','o','u']
print('a' in  vowels)
print('b' not in vowels)

#Identity operators
print("\n Identity operations:")
print(num1 is num2)
print(num2 is not num1)
