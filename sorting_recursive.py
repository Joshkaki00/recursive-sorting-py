#!python


def merge(items1, items2):
    """Merge given lists of items, each assumed to already be in sorted order,
    and return a new list containing all items in sorted order.
    Running time: O(n + m) where n and m are the lengths of items1 and items2.
    We iterate through each list once, comparing and appending elements.
    Memory usage: O(n + m) - we create a new list to store all merged items."""
    merged = []
    i, j = 0, 0
    
    # Repeat until one list is empty
    while i < len(items1) and j < len(items2):
        # Find minimum item in both lists and append it to new list
        if items1[i] <= items2[j]:
            merged.append(items1[i])
            i += 1
        else:
            merged.append(items2[j])
            j += 1
    
    # Append remaining items in non-empty list to new list
    while i < len(items1):
        merged.append(items1[i])
        i += 1
    
    while j < len(items2):
        merged.append(items2[j])
        j += 1
    
    return merged


def merge_sort(items):
    """Sort given items by splitting list into two approximately equal halves,
    sorting each recursively, and merging results into a list in sorted order.
    Running time: O(n log n) in all cases. We split the list log n times (tree depth),
    and merging at each level takes O(n) time.
    Memory usage: O(n) - we create new lists during merging, though recursion adds O(log n) 
    stack space."""
    # Check if list is so small it's already sorted (base case)
    if len(items) <= 1:
        return
    
    # Split items list into approximately equal halves
    mid = len(items) // 2
    left_half = items[:mid]
    right_half = items[mid:]
    
    # Sort each half by recursively calling merge sort
    merge_sort(left_half)
    merge_sort(right_half)
    
    # Merge sorted halves into one list in sorted order
    sorted_items = merge(left_half, right_half)
    
    # Copy sorted items back into original list
    for i in range(len(items)):
        items[i] = sorted_items[i]


def partition(items, low, high):
    """Return index `p` after in-place partitioning given items in range
    `[low...high]` by choosing a pivot (using the last element as pivot) from
    that range, moving pivot into index `p`, items less than pivot into range
    `[low...p-1]`, and items greater than pivot into range `[p+1...high]`.
    Running time: O(n) where n = high - low + 1. We iterate through all items once.
    Memory usage: O(1) - we sort in place with only a few variables."""
    # Choose a pivot - using last element as pivot (simple method)
    pivot = items[high]
    i = low - 1  # Index of smaller element
    
    # Loop through all items in range [low...high-1]
    for j in range(low, high):
        # Move items less than pivot into front of range [low...p-1]
        if items[j] <= pivot:
            i += 1
            items[i], items[j] = items[j], items[i]
    
    # Move pivot item into final position [p] and return index p
    i += 1
    items[i], items[high] = items[high], items[i]
    return i


def quick_sort(items, low=None, high=None):
    """Sort given items in place by partitioning items in range `[low...high]`
    around a pivot item and recursively sorting each remaining sublist range.
    Best case running time: O(n log n) when pivot divides list evenly each time.
    Worst case running time: O(n^2) when pivot is always smallest/largest (already sorted).
    Memory usage: O(log n) for recursion stack in best case, O(n) in worst case."""
    # Check if high and low range bounds have default values (not given)
    if low is None:
        low = 0
    if high is None:
        high = len(items) - 1
    
    # Check if list or range is so small it's already sorted (base case)
    if low < high:
        # Partition items in-place around a pivot and get index of pivot
        p = partition(items, low, high)
        
        # Sort each sublist range by recursively calling quick sort
        quick_sort(items, low, p - 1)  # Sort left sublist
        quick_sort(items, p + 1, high)  # Sort right sublist