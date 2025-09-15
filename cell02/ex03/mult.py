num1 = int(input('Enter the first number: \n'))
num2 = int(input('Enter the second number: \n'))
print(f"{num1} x {num2} = {num1*num2}")
if (num1*num2)<0:
    print("The result is negative.")
elif (num1*num2==0):
    print("The result is positive and negative.")
else:
    print("the result is positive")