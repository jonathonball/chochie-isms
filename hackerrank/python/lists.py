if __name__ == '__main__':
    n = int(input())
    result = []
    for _ in range(n):
        operator, *operands = input().split()
        operands = [int(x) for x in operands]
        if (operator == 'insert'):
            result.insert(operands[0], operands[1])
        elif (operator == 'remove'):
            result.remove(operands[0])
        elif (operator == 'append'):
            result.append(operands[0])
        elif (operator == 'print'):
            print(result)
        elif (operator == 'sort'):
            result.sort()
        elif (operator == 'pop'):
            result.pop()
        else:
            result.reverse()

