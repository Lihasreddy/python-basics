import random
chars = "abcdefghijklmnopqrstuvwxyz123456789"
password = ""
for i in range(8):
    password += random.choice(chars)

print("Generated Password:", password)
