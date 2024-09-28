#Baffoe Nicholas
#Basic calculator
#taking inputs and saving it into num1 and num2 respectively.
num1 = int(input ("what is  your first  number: "))
num2 = int (input ("what is your second number : "))
operation = input("Enter your operation( /,+,-,%  :")
#if statement to check conditions and printout
if operation == '+':
	print(num1 + num2)
elif operation == '/':
	print(num1 / num2)
elif operation == '*':
	print(num1 * num2)
elif operation == '-':
	print(num1 - num2)
elif operation == '%':
	print(num1 % num2)
else:
	print("Enter a valid basic operator")
