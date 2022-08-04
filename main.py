import random
chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_-.,?"
quantity_pwd = int(input("Amount of passwords: "))
length = int(input("Password length: "))

print("\nPossible passwords:")

for pwd in range(quantity_pwd):
    passwords = ""
    for c in range(length):
        passwords += random.choice(chars)
    print(passwords)
