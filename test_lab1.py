"""
A test file to run in CI and with `pytest`.
"""

from lab1 import func
from lab1 import is_prime


def test_func():
    """
    A simple test. Remove me when interesting things exist.
    """
    assert func(2, 3) == 5


def test_is_prime():
    assert not is_prime(1)  # 1 is not prime
    assert is_prime(2)      # 2 is smallest prime
    assert is_prime(17)     # Prime number
    assert not is_prime(18) # Composite number, can be factored into smaller numbers
    assert is_prime(97)     # Larger prime number
    assert not is_prime(100)    # Larger composite number
    # edge cases
    assert not is_prime(0)
    assert not is_prime(-1)
    assert not is_prime(-4)
    assert not is_prime(-17)
