# https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem?h_r=next-challenge&h_v=zen

if __name__ == '__main__':
    n = int(input())
    arr = [i for i in map(int, input().split())]

# hacker version
# print( sorted( list( set(arr) - set( [ max(arr) ] ) ) )[-1] )

# Longer version
# first we put the largest number into a set containing the largest num
# then we get a list of the uniq numbers in the list
# then we subtract the set containing the largest number from the uniq numbers
# sort them, just in case there are negatives
# then whatever the new largest number is the answer
largest_number = set( [ max(arr) ] )
unique_numbers = set(arr)
unique_numbers_without_max = list(unique_numbers - largest_number)
unique_numbers_without_max.sort()
print(unique_numbers_without_max[-1])
