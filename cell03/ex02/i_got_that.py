#!/usr/bin/env python3
first_run = True
while True:
    prompt = "What you gotta say?" if first_run else "I got that! Anything else?"
    value = input(f"{prompt} : ").strip()
    if value == "STOP":
        break
    first_run = False