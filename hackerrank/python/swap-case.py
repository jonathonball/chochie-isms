from string import ascii_lowercase, ascii_uppercase

INDEX_NOT_FOUND = -1

def _swap_case(c):
    index = ascii_uppercase.find(c)
    if index != INDEX_NOT_FOUND:
        return ascii_lowercase[index]
    index = ascii_lowercase.find(c)
    if index != INDEX_NOT_FOUND:
        return ascii_uppercase[index]
    raise ValueError("Expected ascii character")

def swap_case(s):
    return ''.join([ c for c in map(_swap_case, s) ])


