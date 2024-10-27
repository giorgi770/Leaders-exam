# Create a program that receives a non-negative integer and returns its factorial. The factorial of a number n is the product of all positive integers from 1 to n. By definition, the factorial of 0 is 1.
# Examples:
# 5 --> 120
# 0 --> 1

def calculate_factorial(number):
    factorial_result = 1
    for i in range(1, number + 1):
        factorial_result *= i
    return factorial_result

print(calculate_factorial(5))
print(calculate_factorial(0))