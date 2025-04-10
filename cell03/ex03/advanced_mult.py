#!/usr/bin/env python3
import sys
if len(sys.argv) > 1:
    # ???
    print("none")
else:
    for i in range(11):
        print(f"Table de {i}:", end=" ")
        for j in range(11):
            print(i * j, end=" " if j < 10 else "\n")