from string import ascii_lowercase
import itertools

n = int(input().strip())
data = [ char for char in input().strip().split(" ") ]
k = int(input().strip())
print("data: ", [ [i, j] for i, j in enumerate(data) ])
indexes = range(len(data))
combinations = itertools.combinations(indexes, k)
total_a = 0
total = 0
for combination in combinations:
    print(combination)
    total += 1
    has_a = False
    for index in range(k):
        if data[combination[index]] == "a":
            has_a = True
    if has_a:
        total_a += 1

result = total_a / total
print(result)
