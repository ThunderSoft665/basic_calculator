#logical operator using or
#operator ==> or
#operand ==> variable ( first_number and second_number)
#values ==> 5 & 6
'''
first_number = 6
second_number= 5
if first_number or second_number:
 print("valid operation")

'''


# A simple calculator App.
#using 2 numbers only
print(''' **********
1. Addition
2. Substraction
3. Multiplication
4. Division
5. Exponential
6. Floor Division
**********''')


print("**********")
print("Enter two numbers to add: ")
print("*********")
first_number = float(input("first_number:\n>>> "))   #prompt the user to enter first number and store it.
second_number = float(input("second_number:\n>>> ")) #prompt the user to enter second number and store it.
sum = first_number + second_number
#print(sum) 
print(f"{first_number} + {second_number} = {sum:.2f}")


print("*********")
print("Enter two numbers to substract: ")
print("*********")
first_number = float(input("first_number:\n>>> "))   #prompt the user to enter first number and store it.
second_number = float(input("second_number:\n>>> ")) #prompt the user to enter second number and store it.
sub = first_number - second_number
#print(sub) 
print(f"{first_number} - {second_number} = {sub:.2f}")

print("*********")
print("Enter two numbers to multiply")
print("*********")
first_number = float(input("first_number:\n>>> "))   #prompt the user to enter first number and store it.
second_number = float(input("second_number:\n>>> ")) #prompt the user to enter second number and store it.
mul = first_number * second_number
#print(mul) 
print(f"{first_number} * {second_number} = {mul:.2f}")


print("**********")
print("Enter two numbers to divide")
print("*********")
first_number = float(input("first_number:\n>>> "))   #prompt the user to enter first number and store it.
second_number = float(input("second_number:\n>>> ")) #prompt the user to enter second number and store it.
div = first_number / second_number
#print(div) 
print(f"{first_number} / {second_number} = {div:.2f}")



print("**********")
print("Enter two numbers to exponent")
print("**********")
first_number = float(input("first_number:\n>>> "))   #prompt the user to enter first number and store it.
second_number = float(input("second_number:\n>>> ")) #prompt the user to enter second number and store it.
exp = first_number ** second_number
#print(sum) 
print(f"{first_number} ** {second_number} = {exp:.2f}")



print("**********")
print("Enter two numbers to floor division")
print("*********")
first_number = float(input("first_number:\n>>> "))   #prompt the user to enter first number and store it.
second_number = float(input("second_number:\n>>> ")) #prompt the user to enter second number and store it.
floor_div = first_number // second_number
#print(floor_div) 
print(f"{first_number} // {second_number} = {floor_div:.2f}")
  












