name = input("Enter your name:")
age = int(input("And enyter your age: "))

print('Welcome to park!')

if age < 4:
    price = 0
elif age < 18:
    price = 25

else:
    price = 40

print(f"{name}, you need to pay ${price} to enter the park! Get your ticket from kassa. ")
