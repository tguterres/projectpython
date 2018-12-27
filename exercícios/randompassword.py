#randompassword
import random

chars = 'abcdefghijklmnopqrstuvxyz1234567890!@*&%$'
password = ' '

for c in range(12):
    password += random.choice(chars)
print(password)

