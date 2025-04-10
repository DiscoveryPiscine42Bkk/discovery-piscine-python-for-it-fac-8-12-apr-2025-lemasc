#!/usr/bin/env python3
print("Enter a number less than 25")
i = int(input())
n = 25
if i >= n:
    print("Error")
else:
    while i <= n:
        print(f"Inside the loop, my variable is {i}")
        i += 1