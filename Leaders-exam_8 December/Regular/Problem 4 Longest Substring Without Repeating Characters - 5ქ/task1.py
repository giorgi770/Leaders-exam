# Challenge:
# Create a function that finds the length of the longest substring without repeating characters.
# Instructions:
# Input: A string (e.g., "abcabcbb").
# Output: An integer representing the length of the longest substring (e.g., 3 for "abc").
# Test Cases:
# assert longest_unique_substring("abcabcbb") == 3
# assert longest_unique_substring("bbbbb") == 1
# assert longest_unique_substring("") == 0
# assert longest_unique_substring("pwwkew") == 3

def longest_unique_substring(s):
    char_set = set()
    left = 0
    max_lenght = 0

    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left +=1

        char_set.add(s[right])
        max_lenght = max(max_lenght, right - left + 1)

    return max_lenght

assert longest_unique_substring("abcabcbb") == 3
assert longest_unique_substring("bbbbb") == 1
assert longest_unique_substring("") == 0
assert longest_unique_substring("pwwkew") == 3

print("All test passed succsefully")