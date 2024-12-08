# Challenge:
#  Write a function to find the common elements between two lists.
# Instructions:
# Input: Two lists of integers (e.g., [1, 2, 3] and [2, 3, 4]).
# Output: A list of integers representing the intersection (e.g., [2, 3]).
# Test Cases:
# assert find_intersection([1, 2, 3], [2, 3, 4]) == [2, 3]
# assert find_intersection([1, 1, 2], [1, 3]) == [1]
# assert find_intersection([], [1, 2]) == []

def find_intersection(list1, list2):

    return list(set(list1) & set(list2))

assert find_intersection([1, 2, 3], [2, 3, 4]) == [2, 3]
assert find_intersection([1, 1, 2], [1, 3]) == [1]
assert find_intersection([], [1, 2]) == []

print("All test passed succsefully")