#!/usr/bin/env python3
first = int(input("Give me the first number: "))
second = int(input("Give me the second number: "))
print("Thank you!")
print(f"{first} + {second} = {first + second}")
print(f"{first} - {second} = {first - second}")
print(f"{first} / {second} = {"Error" if not second else first * second}")
print(f"{first} * {second} = {first * second}")