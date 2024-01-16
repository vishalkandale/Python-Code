num1 = float(input("Enter the number 1 = "))
num2 = float(input("Enter the number 2 = "))

opration = input("Enter the opration (+,-,*,/) = ")

def add(num1,num2):
    return num1 + num2
def minus(num1,num2):
    return num1 - num2
def multiply(num1,num2):
    return num1 * num2
def divide(num1,num2):
    return num1/num2

if opration == "+":
    print(f"Addiition of {num1} & {num2} = {add(num1,num2)}")
elif opration == "-":
    print(f"Subtraction of {num1} & {num2} = {minus(num1,num2)}")
elif opration == "*":
    print(f"multiplication of {num1} & {num2} = {multiply(num1,num2)}")
elif opration == "/":
    print(f"division of {num1} & {num2} = {divide(num1,num2)}")
else:
    print("You have enter invalid opration")

