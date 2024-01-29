from itertools import permutations

original_list = [3, 4, 2, 5, 1]

# Get all permutations of the original list
all_permutations = list(permutations(original_list))

# Print the permutations
for perm in all_permutations:
    print(perm)
