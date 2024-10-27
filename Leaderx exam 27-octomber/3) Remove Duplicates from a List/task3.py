# Create a program that receives a list and removes duplicate elements while maintaining the original order.
# Examples:
# [1, 2, 2, 3, 4, 4, 5] --> [1, 2, 3, 4, 5]
# ['a', 'b', 'a', 'c'] --> ['a', 'b', 'c']

def remove_duplicate_from_list(items):
    result = []
    for element in items:
        if element not in result:
            result.append(element)
    return result
        
print(remove_duplicate_from_list([1, 2, 3, 4, 4, 5]))
print(remove_duplicate_from_list(['a', 'b', 'a', 'c']))