def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

# Generate a list of prime numbers from 1 to 50
prime_numbers = [num for num in range(1, 51) if is_prime(num)]

print(prime_numbers)


# Generate a list of prime numbers from 1 to 50 using list comprehension
prime_numbers = [
    num for num in range(2, 51)
    if all(num % i != 0 for i in range(2, int(num**0.5) + 1))
]

print(prime_numbers)
