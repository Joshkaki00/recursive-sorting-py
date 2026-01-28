#!python


def is_sorted(items):
    """Return a boolean indicating whether given items are in sorted order.
    Running time: O(n) - we iterate through the list once in the worst case.
    Memory usage: O(1) - only using a few variables regardless of input size."""
    # Check that all adjacent pairs of items are in order
    for i in range(len(items) - 1):
        if items[i] > items[i + 1]:
            return False
    return True


def bubble_sort(items):
    """Sort given items by swapping adjacent out-of-order pairs (bubble up).
    Running time: O(n^2) worst/average case - nested loops where outer runs n times 
    and inner runs up to n times. O(n) best case when already sorted.
    Memory usage: O(1) - sorts in place with only a few variables."""
    # Repeat until all items are in sorted order
    for i in range(len(items) - 1):
        swapped = False
        # Swap adjacent items that are out of order
        for j in range(len(items) - 1 - i):
            if items[j] > items[j + 1]:
                items[j], items[j + 1] = items[j + 1], items[j]
                swapped = True
        # If no swaps were made, list is sorted
        if not swapped:
            break


def selection_sort(items):
    """Sort given items by finding minimum item, swapping it with first
    unsorted item, and repeating until all items are in sorted order.
    Running time: O(n^2) in all cases - always performs n passes and each pass
    examines remaining unsorted items.
    Memory usage: O(1) - sorts in place with only a few variables."""
    # Repeat until all items are in sorted order
    for i in range(len(items) - 1):
        # Find minimum item in unsorted items
        min_index = i
        for j in range(i + 1, len(items)):
            if items[j] < items[min_index]:
                min_index = j
        # Swap minimum item with first unsorted item
        if min_index != i:
            items[i], items[min_index] = items[min_index], items[i]


def insertion_sort(items):
    """Sort given items by taking each item and inserting it in sorted order
    into a new list which is initially empty.
    Running time: O(n^2) worst/average case - for each item we may need to compare
    with all previously sorted items. O(n) best case when already sorted.
    Memory usage: O(1) - sorts in place with only a few variables."""
    # Repeat until all items are in sorted order
    for i in range(1, len(items)):
        # Insert items[i] into sorted position in items[0...i]
        current = items[i]
        j = i - 1
        # Shift larger items to the right
        while j >= 0 and items[j] > current:
            items[j + 1] = items[j]
            j -= 1
        # Insert current item in the correct position
        items[j + 1] = current
