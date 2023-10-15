import random 

elements ="+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

pass_lenght = int(input("Podaj długość hasła "))

password = ""

for i in range (pass_lenght):
    password += random.choice(elements)

print(password)
