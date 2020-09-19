# Strong Password Detection
# Write a function that uses regular expressions to make sure the password
# string it is passed is strong.
# A strong password is defined as one that is at
# least eight characters long, contains both uppercase and lowercase charac-
# ters, and has at least one digit. You may need to test the string against mul-
# tiple regex patterns to validate its strength.
import re

strongRegex = re.compile(r'[a-zA-Z0-9-`!@#$%^&*?/]+')

user_input = input('Enter a password: ')
strongReturn = ''.join(strongRegex.findall(user_input))
if strongReturn.isalnum() or (strongReturn.isupper() or strongReturn.islower()) or (strongReturn.isalpha() or strongReturn.isdigit()):
    print('you entered a weak pssword')
elif strongReturn.isascii():
    print('strong password')


