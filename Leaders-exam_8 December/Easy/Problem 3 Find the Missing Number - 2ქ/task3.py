# Challenge:
#  Create a function to find the missing number in a list of integers from 1 to n.
# Instructions:
# Input: A list of integers from 1 to n with one number missing (e.g., [1, 2, 4, 5]).
# Output: The missing number (e.g., 3 in this case).
# Test Cases:
# assert find_missing_number([1, 2, 4, 5]) == 3
# assert find_missing_number([3, 5, 6, 1, 2]) == 4
# assert find_missing_number([2]) == []


def find_missing_number(numbers):
    n = len(numbers) + 1

    expected_sum = n * (n + 1)

    actual_sum = sum(numbers)

    missing_number = expected_sum - actual_sum

    return missing_number if missing_number > 0 else []

assert find_missing_number([1, 2, 4, 5]) == 3
assert find_missing_number([3, 5, 6, 1, 2]) == 4
assert find_missing_number([2]) == []

print("All tests passed succesufully")