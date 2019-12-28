# fields = ["name", "math", "physics", "chemistry"]

# for _ in range(int(input())):
#     raw = input().split()
#     data = { raw[0]: { fields[i]:raw[i] for i in range(1, 4) } }
from functools import reduce

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    print("{:0.2f}".format(reduce(lambda x,y: x+y, student_marks[query_name]) / 3 ))
