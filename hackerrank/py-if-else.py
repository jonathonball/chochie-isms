#!/bin/python3
# From https://www.hackerrank.com/challenges/py-if-else/problem?isFullScreen=true

import math
import os
import random
import re
import sys


if __name__ == '__main__':
    n = int(input().strip())
    if (n % 2):
        print("Weird")
    else:
        if (n >= 6) and (n <= 20):
            print("Weird")
        else:
            print ("Not Weird")

