#!/usr/bin/env python3
age = int(input("Please tell me your age: "))
if age <= 0:
    print("Please enter a valid age!")
else:
    print(f"You are currently {age} years old.")
    for i in range(1,4):
        print(f"In {i * 10} years, you'll be {age + i * 10} years old.")