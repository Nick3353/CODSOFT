import random
import string

pass_length = int (input("Enter the length of your password "))

if pass_length < 8:
	print("Password length has to be greater than 8")
else:
	pass_characters= string.ascii_letters +string.digits + string.punctuation
	
	password = ''.join(random.choices(pass_characters, k= pass_length))
	print(password)