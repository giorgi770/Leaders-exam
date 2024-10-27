# Create a program which receives a decimal number and converts it to binary.

# Examples:
# 17 --> 10001
# 15 --> 1111

def decimal_to_binary(decimal_num):
    binary = bin(decimal_num)[2:]
    return binary

print(decimal_to_binary(17))
print(decimal_to_binary(15))