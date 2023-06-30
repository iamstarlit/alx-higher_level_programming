#!/usr/bin/python3

def find_peak(list_of_integers):
    # Check if the list is empty
    if not list_of_integers:
        return None

    # Get the size of the list
    size = len(list_of_integers)

    # Check the edge cases for the first and last elements
    if size == 1 or list_of_integers[0] >= list_of_integers[1]:
        return list_of_integers[0]
    elif list_of_integers[size - 1] >= list_of_integers[size - 2]:
        return list_of_integers[size - 1]

    # Binary search for the peak
    left = 1
    right = size - 2
    while left <= right:
        mid = (left + right) // 2
        if list_of_integers[mid] >= list_of_integers[mid - 1] and
        list_of_integers[mid] >= list_of_integers[mid + 1]:
            return list_of_integers[mid]
        elif list_of_integers[mid] < list_of_integers[mid - 1]:
            right = mid - 1
        else:
            left = mid + 1

    return None
