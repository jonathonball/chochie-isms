def is_evenly_divisible(dividend, divisor):
    return not (dividend % divisor)

def is_leap(year):
    leap_year = False
    if (is_evenly_divisible(year, 4)):
        leap_year = True
        if (is_evenly_divisible(year, 100)):
            leap_year = False
            if (is_evenly_divisible(year, 400)):
                leap_year = True
    return leap_year

year = int(input())
