def merge_and_count_inversions(arr):
    if len(arr) <= 1:
        return arr, 0

    mid = len(arr) // 2
    left, inv_left = merge_and_count_inversions(arr[:mid])
    right, inv_right = merge_and_count_inversions(arr[mid:])
    merged, inv_merge = merge(left, right)

    return merged, inv_left + inv_right + inv_merge


def merge(left, right):
    merged = []
    inversions = 0
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            inversions += len(left) - i
            j += 1

    merged.extend(left[i:])
    merged.extend(right[j:])

    return merged, inversions


def min_switches_to_sort_boxes(N, boxes):
    _, min_switches = merge_and_count_inversions(list(enumerate(boxes, 1)))
    return min_switches


# Input
N = int(input())
boxes = list(map(int, input().split()))

# Output
result = min_switches_to_sort_boxes(N, boxes)
print(result)
