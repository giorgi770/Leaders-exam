# Create a program which receives a binary number and converts it to decimal.
# Examples:
# 10001 --> 17
# 1111 --> 15

def binary_to_decimal(binary_str):
    decimal = int(binary_str, 2)
    return decimal

print(binary_to_decimal("10001"))
print(binary_to_decimal("1111"))