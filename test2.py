def min_swaps_and_gaps(original_list):
    # Create a list of tuples containing the original values and their indices
    indexed_list = list(enumerate(original_list))

    # Sort the indexed list based on the values
    indexed_list.sort(key=lambda x: x[1])

    # Initialize a variable to keep track of swaps
    swaps = 0

    # Iterate through the sorted list to find the minimum number of swaps
    for i in range(len(indexed_list)):
        # Check if the current element is at its correct position
        while indexed_list[i][0] != i:
            # Swap the current element with the one at its correct position
            indexed_list[i], indexed_list[indexed_list[i][0]] = (
                indexed_list[indexed_list[i][0]],
                indexed_list[i],
            )
            swaps += 1

    # Calculate the gaps between consecutive elements in the sorted list
    gaps = [indexed_list[i][0] - i for i in range(len(indexed_list))]

    return swaps, gaps


# Example usage:
original_list = [3, 4, 2, 5, 1]
swaps, gaps = min_swaps_and_gaps(original_list)

print("Original List:", original_list)
print("Sorted List with Gaps:", gaps)
print("Minimum Swaps:", swaps)
