def count_changes_to_sort(original_list, sorted_list):
    changes = 0
    for i in range(len(original_list)):
        if original_list[i] != sorted_list[i]:
            changes += 1

    return changes


# Input
N = int(input())
original_list = list(map(int, input().split()))

# Count changes and sort the list
sorted_list = sorted(original_list)
changes = count_changes_to_sort(original_list, sorted_list)

# Output
print(int(changes/2))