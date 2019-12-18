# https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem?h_r=next-challenge&h_v=zen

if __name__ == '__main__':
    n = int(input())
    arr = [i for i in map(int, input().split())]

# hacker version
print( sorted( list( set(arr) - set( [ max(arr) ] ) ) )[-1] )
