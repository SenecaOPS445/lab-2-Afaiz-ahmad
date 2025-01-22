#!/usr/bin/env python3 


# Author: Ali Ahmad Faiz Ahmad 
# Author ID: Afaiz-ahmad
# Date Created: 2025/01/21

import sys

if len(sys.argv) > 1:
    timer = int(sys.argv[1])

else:
    timer = 3

while timer > 0:
    print(timer)
    timer -= 1

print('blast off!')

