#!/bin/python3

import math
import os
import random
import re
import sys

def sorted_by_index(things, index):
    return sorted(things, key=lambda things: things[index])

def cast_list_to_str(things):
    return [str(thing) for thing in things]

if __name__ == '__main__':
    nm = input().split()
    n = int(nm[0])
    m = int(nm[1])
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))
    k = int(input())
    result = sorted_by_index(arr, k)
    for row in result:
        print(" ".join(cast_list_to_str(row)))
