from itertools import permutations
def permut(str):
    return list(permutations(str, len(str)))

print(permut(input()))