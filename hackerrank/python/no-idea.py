"""
no-idea: https://www.hackerrank.com/challenges/no-idea/problem
"""

def strings_to_int(strings):
    """Convert list of strings into list of ints"""
    return [ int(num) for num in strings ]

def list_to_set(l):
    """Concert list to set"""
    return { v for v in l }

def distinct_num_counts(data):
    """Return the dict with count of each distinct value in data"""
    result = {}
    for num in data:
        try:
            result[num] += 1
        except KeyError:
            result[num] = 1
    return result

def sum_counts(values, data):
    """Return int sum of values found in data"""
    sum = 0
    for num in values:
        try:
            sum += data[num]
        except KeyError:
            pass
    return sum

N, M = strings_to_int(input().strip().split())
print("N", N)
print("M", M)
DATA = distinct_num_counts(strings_to_int(input().strip().split()))
A = list_to_set(strings_to_int(input().strip().split()))
B = list_to_set(strings_to_int(input().strip().split()))

print(sum_counts(A, DATA) - sum_counts(B, DATA))
