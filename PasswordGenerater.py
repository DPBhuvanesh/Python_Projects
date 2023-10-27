import random

character = 'abcdefghijklmnopqrstuvwxyz0123456789@#$₹&^!()-_+=[];,\|ABCDEFGHIJKLMNOPQRSTUVWXYZ'

password_length = int(input('Length of password : '))
new_password = []

for i in range(password_length):
    pick = random.choice(character)
    new_password.append(pick)

final_password = ''.join(map(str, new_password))
print('Generated Password: ',final_password)