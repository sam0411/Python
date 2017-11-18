from scipy.special import perm
from itertools import permutations

result = perm(3, 2)

print('Permutation (3,2) = ', result)

print(list(permutations([1, 2, 3], 2)))