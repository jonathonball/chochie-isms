if __name__ == '__main__':
    data = [ {'name': input(), 'score': float(input())} for thing in range(int(input())) ]
    scores = set([ thing['score'] for thing in data ])
    next_largest = sorted( list( set(scores) - set( [ min(scores) ] ) ) )[0]
    results = []
    for thing in data:
        if thing['score'] == next_largest:
            results.append(thing['name'])
    for name in sorted(results):
        print(name)
