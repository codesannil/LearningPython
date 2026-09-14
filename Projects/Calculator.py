# Asking to user for the first Number
num1 = float(input("Enter the first number: "))


# Asking to user for the opreator
opreator = str(input("Enter the opreator(+-*/ more...)"))

# Asking to user for the second Number
num2 = float(input("Enter the second number: "))

# Opreator opreations 

if opreator == "+":
    result = num1 + num2
    print(f"{num1} {opreator} {num2} is {result}")

elif opreator == "-:":
    result = num1 - num2
    print(f"{num1} {opreator} {num2} is {result}")

elif opreator == "*":
    result = num1 * num2
    print(f"{num1} {opreator} {num2} is {result}")

elif opreator == "/":
    result = num1 / num2
    print(f"{num1} {opreator} {num2} is {result}")

elif opreator == "//":
    result = num1 // num2
    print(f"{num1} {opreator} {num2} is {result}")

elif opreator == "%:":
    result = num1 % num2
    print(f"{num1} {opreator} {num2} is {result}")

else:
    print(f"{opreator} is not a valid opreator")

















