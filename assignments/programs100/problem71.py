# Please write a binary search function which searches an item in a
# sorted list. The function should return the index of element to be
# searched in the list.
# Hints:
# Use if/elif to deal with conditions.

def binary_search(lst, num_to_search):
    # finding min, max indexes
    min_idx = 0
    max_idx = len(lst) - 1
    result = False

    while min_idx <= max_idx:
        mid_idx = (min_idx + max_idx) // 2
        if lst[mid_idx] == num_to_search:
            result = True
            break
        elif lst[mid_idx] > num_to_search:
            max_idx = mid_idx - 1
        elif lst[mid_idx] < num_to_search:
            min_idx = mid_idx + 1
    return result, mid_idx


res = binary_search([1, 2, 3, 4, 5, 6, 7], 5)
print(res)
if res[0]:
    print("Element found at index ", res[1])
else:
    print('Element not found')

# print(binary_search([1, 2, 3, 4, 5, 6, 7], 9))
