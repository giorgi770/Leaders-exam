# write the function is_anagram
def is_anagram(test, original):
    original = original.lower()
    test = test.lower()
    return sorted(test) == sorted(original)