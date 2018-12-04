#randompassword
import random

chars = 'abcdefghijklmnopqrstuvxyz1234567890!@*&%$'

password = ''
for c in range(10):
    password += random.choice(chars)
print(password)

