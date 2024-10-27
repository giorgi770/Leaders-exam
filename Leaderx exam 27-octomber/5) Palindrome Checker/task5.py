# Create a program that checks if a given string is a palindrome (reads the same forward and backward). The function should ignore spaces, punctuation, and capitalization.
# Examples:
# "A man a plan a canal Panama" --> True
# "Hello" --> False

import re

def is_palindrome(text):
    cleaned_text = re.sub(r'[^A-Za-z0-9]', '', text).lower()
    return cleaned_text == cleaned_text[::-1]

print(is_palindrome("A man a plan a canal Panama"))
print(is_palindrome("Hello"))