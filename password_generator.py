import string
import random

characters = string.ascii_letters+string.digits+'@#$%*&?!'
characters = ''.join(characters)
lower_case_letters = string.ascii_lowercase
upper_case_letters = string.ascii_uppercase
digits = string.digits
symbols = '@#$%*&?!'

password = []

password_length = int(input('How many characters is your password? '))
lower_case_num = int(input('How many lower case characters do you want? '))
upper_case_num = int(input('How many upper case characters do you want? '))
digit_num = int(input('How many digits do you want? '))
symbols_num = int(input('How many symbols do you want? '))

if password_length < (lower_case_num + upper_case_num + digit_num + symbols_num):
    print('ERROR: Sum of Specifications Greater Than Passoword Length')

for i in range(lower_case_num):
    password.append(random.choice(lower_case_letters))

for i in range(upper_case_num):
    password.append(random.choice(upper_case_letters))

for i in range(digit_num):
    password.append(random.choice(digits))

for i in range(symbols_num):
    password.append(random.choice(symbols))

if len(password) < password_length:
    for i in range(password_length-len(password)):
        password.append(random.choice(characters))

random.shuffle(password)
password = ''.join(password)

print(password)