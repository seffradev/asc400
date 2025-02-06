"""
A test file to run in CI and with `pytest`.
"""

import pytest
from lab1 import (
    is_prime,
    gcd,
    eea,
    phi,
    modular_inverse,
)


def test_is_prime():
    """
    Task 1
    Test cases for the is_prime function.
    """
    assert not is_prime(1)  # 1 is not prime
    assert is_prime(2)  # 2 is smallest prime
    assert is_prime(17)  # Prime number
    assert not is_prime(18)  # Composite number, can be factored into smaller numbers
    assert is_prime(97)  # Larger prime number
    assert not is_prime(100)  # Larger composite number
    # edge cases
    assert not is_prime(0)
    assert not is_prime(-1)
    assert not is_prime(-4)
    assert not is_prime(-17)
    assert not is_prime(-2.1)
    assert not is_prime(9.1)
    assert not is_prime(5.1)
    assert not is_prime(2.1)


def test_gcd():
    """
    Task 2
    Test gcd function.
    """
    assert gcd(48, 18) == 6
    assert gcd(101, 103) == 1
    assert gcd(-48, 18) == 6
    assert gcd(0, 7) == 7


def test_eea():
    """
    Task 2
    Test Extended Euclidean algorithm function.
    """
    assert eea(3, 20) == 7
    assert eea(3, 11) == 4
    assert eea(7, 40) == 23
    assert eea(17, 3120) == 2753
    assert eea(3, 11) == 4
    assert eea(9, 26) == 3
    assert eea(10, 17) == 12
    assert eea(15, 28) == 15
    assert eea(12, 31) == 13
    assert eea(35, 64) == 11
    with pytest.raises(ValueError):
        eea(5, 15)


def test_phi():
    """
    Task 3
    Test euler phi function.
    """
    # Edge cases
    with pytest.raises(ValueError):
        phi(0)
    with pytest.raises(ValueError):
        phi(-1)
    with pytest.raises(ValueError):
        phi(-4565)

    assert phi(1) == 1  # Only 1 is coprime with itself

    # Prime numbers (φ(p) = p - 1)
    assert phi(2) == 1
    assert phi(5) == 4
    assert phi(7) == 6
    assert phi(11) == 10
    assert phi(13) == 12
    assert phi(17) == 16
    assert phi(101) == 100  # Large prime number

    # Powers of prime numbers (φ(p^k) = p^k - p^(k-1))
    assert phi(4) == 2  # 2²
    assert phi(8) == 4  # 2³
    assert phi(9) == 6  # 3²
    assert phi(27) == 18  # 3³
    assert phi(81) == 54  # 3⁴
    assert phi(16) == 8  # 2⁴
    assert phi(1024) == 512  # 2¹⁰

    # Product of two distinct prime numbers (φ(mn) = φ(m)φ(n))
    assert phi(10) == 4  # 2 * 5
    assert phi(14) == 6  # 2 * 7
    assert phi(15) == 8  # 3 * 5
    assert phi(21) == 12  # 3 * 7
    assert phi(22) == 10  # 2 * 11
    assert phi(35) == 24  # 5 * 7
    assert phi(77) == 60  # 7 * 11

    # Product of powers of two distinct prime numbers
    # (φ(m**a * n**b) = m**(a-1)*(m-1)*n**(b-1)*(n-1))
    assert phi(108) == 36  # 2² * 3³
    assert phi(8575) == 5880  # 5² * 7³

    # More composite numbers (φ(ab) = (a-1)(b-1))
    assert phi(12) == 4  # 2² * 3
    assert phi(20) == 8  # 2² * 5
    assert phi(30) == 8  # 2 * 3 * 5


def test_modular_inverse():
    """
    Task 4
    Test modular inverse function.
    """
    assert modular_inverse(-1, 143) == 1
    assert modular_inverse(7, 143) == 103
    assert modular_inverse(5, 323) == 173
    assert modular_inverse(3, 667) == 411
    assert modular_inverse(17, 187) == 113
    assert modular_inverse(1, 77) == 1
    assert modular_inverse(13, 299) == 61
    with pytest.raises(ValueError):
        modular_inverse(11, 391)
    with pytest.raises(ValueError):
        modular_inverse(11, -391)
    with pytest.raises(ValueError):
        modular_inverse(11.1, 391)
    with pytest.raises(ValueError):
        modular_inverse(11, 391)
