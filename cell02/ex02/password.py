#!/usr/bin/env python3
password = "Python is awesome"
entered = input().strip()
if password == entered:
    print("ACCESS GRANTED")
else:
    print("ACCESS DENIED")
