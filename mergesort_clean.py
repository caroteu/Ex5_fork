import numpy as np

#this is a comment
def plot_list(my_list):
    x = range(len(my_list))
    plt.bar(x, my_list)
    plt.show()

#this is a different comment

def copy_remaining(i, main_list, j, sub_list):
    while j < len(sub_list):
        main_list[i] = sub_list[j]
        j += 1
        i += 1
    return i


def merge_sort(my_list):
    if len(my_list) > 1:
        mid = len(my_list) // 2
        left = my_list[:mid]
        right = my_list[mid:]

        # Recursive call on each half
        merge_sort(left)
        merge_sort(right)

        # Two iterators for traversing the two halves
        l = 0
        r = 0

        # Iterator for the main list
        i = 0

        while l < len(left) and r < len(right):
            if left[l] <= right[r]:
                # The value from the left half has been used
                my_list[i] = left[l]
                # Move the iterator forward
                l += 1
            else:
                my_list[i] = right[r]
                r += 1
            # Move to the next slot
            i += 1

        # For all the remaining values
        i = copy_remaining(i, my_list, l, left)
        copy_remaining(i, my_list, r, right)


import matplotlib.pyplot as plt

my_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
plot_list(my_list)
merge_sort(my_list)
plot_list(my_list)
