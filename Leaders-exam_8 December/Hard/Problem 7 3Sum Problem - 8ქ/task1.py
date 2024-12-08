# Challenge:
#  Find all unique triplets in an array that sum up to zero.
# Instructions:
# Input: A list of integers (e.g., [-1, 0, 1, 2, -1, -4]).
# Output: A list of unique triplets that sum to zero.
# Test Cases:
# assert three_sum([-1, 0, 1, 2, -1, -4]) == [[-1, -1, 2], [-1, 0, 1]]
# assert three_sum([0, 0, 0]) == [[0, 0, 0]]
# assert three_sum([1, 2, -2, -1]) == []

def three_sum(nums):
    nums.sort()
    triplets = []

    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        left, right = i + 1, len(nums) - 1

        while left < right:
            total = nums[i] + nums[left] + nums[right]

            if total < 0:
                left += 1
            elif total > 0:
                right -= 1
            else:
                triplets.append([nums[i], nums[left], nums[right]])

                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1

                left += 1
                right -= 1

    return triplets
    
assert three_sum([-1, 0, 1, 2, -1, -4]) == [[-1, -1, 2], [-1, 0, 1]]
assert three_sum([0, 0, 0]) == [[0, 0, 0]]
assert three_sum([1, 2, -2, -1]) == []
print("All test passed succsefully")