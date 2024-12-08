# Challenge:
#  Write a function to check if two strings are anagrams 
#(contain the same characters in the same frequency).
# Instructions:
# Input: Two strings (e.g., "listen" and "silent").
# Output: A boolean (True or False) indicating if the strings are anagrams.
# Test Cases:
# assert are_anagrams("listen", "silent") == True
# assert are_anagrams("hello", "world") == False
# assert are_anagrams("triangle", "integral") == True

def are_anagrams(s1, s2):

    return sorted(s1) == sorted(s2)

assert are_anagrams("listen", "silent") == True
assert are_anagrams("hello", "world") == False
assert are_anagrams("triangle", "integral") == True

print("All test passed succsefully")