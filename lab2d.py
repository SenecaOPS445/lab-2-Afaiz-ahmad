#!/usr/bin/env python3

'''
This program will prompt the user for input data
Author: Ali Ahmad Faiz Ahmad (Afaiz-ahmad)
'''

import sys

if len(sys.argv) != 3:
    print(f"Usage: {sys.argv[0]} name age")
    sys.exit()

name = sys.argv[1]
age = int(sys.argv[2])

print('Hi ' + name + ', you are ' + str(age) + ' years old.')




