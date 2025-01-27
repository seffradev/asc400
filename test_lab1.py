"""
A test file to run in CI and with `pytest`.
"""

from lab1 import func


def test_func():
    """
    A simple test. Remove me when interesting things exist.
    """
    assert func(2, 3) == 5


# Task 1:
def is_prime(n):
    if n <= 1:  # Numbers less than or equal to 1 are not prime.
        return False
    if n == 2:  # 2 is a prime number.
        return True
    if n % 2 == 0:  # Eliminate even numbers greater than 2
        return False

    # Check divisors from 3 to sqrt(n) (inclusive)
    limit = int(n**0.5) + 1 # Calculate the integer sqrt(n)
    for i in range(3, limit, 2):    # Only test odd numbers
        if n % i == 0:
            return False
    return True