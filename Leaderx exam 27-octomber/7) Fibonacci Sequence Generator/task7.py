# Create a program that receives an integer n and returns the first n numbers in the Fibonacci sequence. The sequence starts with 0 and 1, and each subsequent number is the sum of the previous two.
# Examples:
# 5 --> [0, 1, 1, 2, 3]
# 7 --> [0, 1, 1, 2, 3, 5, 8]

def fibonacci_sequence(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return[0, 1]
    
    sequence = [0, 1]
    for i in range(2, n):
        next_number = sequence[i - 1] + sequence[i - 2]
        sequence.append(next_number)

    return sequence
    
print(fibonacci_sequence(5))
print(fibonacci_sequence(7))