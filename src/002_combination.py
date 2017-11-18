from scipy.special import comb
from itertools import combinations

result = comb(3, 2)

print('Combination (3,2) = ', result)

print(list(combinations([1, 2, 3], 2)))