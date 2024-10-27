# Write a function that takes a maximum bound and returns all primes up to and including the maximum bound.

# For example:
# 11 => [2, 3, 5, 7, 11]

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5)+ 1):
        if num % i == 0:
            return False
        return True
    
def primes_up_to(max_bound):
    primes = []
    for num in range(2, max_bound + 1):
        if is_prime(num):
            primes.append(num)
    return primes
        

print(primes_up_to(11))