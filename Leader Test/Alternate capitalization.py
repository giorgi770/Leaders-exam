def capitalize(s):
    even = ''.join([letter.capitalize() if i % 2 == 0 else letter for i, letter in enumerate(s)])
    odd = ''.join([letter.capitalize() if i % 2 == 1 else letter for i, letter in enumerate(s)])
    return [even, odd]