"""
A test file to run in CI and with `pytest`.
"""

import pytest
from lab1 import (
    is_prime,
    gcd,
    euler_phi,
    eea,
    task_3,
    public_to_private_key,
    public_to_private_key_alt_1,
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
    Task 2 alt 2
    Test gcd function.
    """
    assert gcd(48, 18) == 6
    assert gcd(101, 103) == 1
    assert gcd(-48, 18) == 6
    assert gcd(0, 7) == 7


def test_eea():
    """
    Task 2 alt 2
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


def test_task_3():
    """
    Task 3 alt 1
    Test euler phi alt 1 function.
    """
    # Edge cases
    # with pytest.raises(ValueError):
    #    task_3(0)
    assert task_3(1) == 1  # Only 1 is coprime with itself

    # Prime numbers (φ(p) = p - 1)
    assert task_3(2) == 1
    assert task_3(5) == 4
    assert task_3(7) == 6
    assert task_3(11) == 10
    assert task_3(13) == 12
    assert task_3(17) == 16
    assert task_3(101) == 100  # Large prime number

    # Powers of prime numbers (φ(p^k) = p^k - p^(k-1))
    assert task_3(4) == 2  # 2²
    assert task_3(8) == 4  # 2³
    assert task_3(9) == 6  # 3²
    assert task_3(16) == 8  # 2⁴
    assert task_3(1024) == 512  # 2¹⁰

    # Product of two distinct prime numbers (φ(mn) = φ(m)φ(n))
    assert task_3(10) == 4  # 2 * 5
    assert task_3(14) == 6  # 2 * 7
    assert task_3(15) == 8  # 3 * 5
    assert task_3(21) == 12  # 3 * 7
    assert task_3(22) == 10  # 2 * 11
    assert task_3(35) == 24  # 5 * 7
    assert task_3(77) == 60  # 7 * 11

    # More composite numbers
    assert task_3(12) == 4  # 2² * 3
    assert task_3(20) == 8  # 2² * 5
    assert task_3(30) == 8  # 2 * 3 * 5


def test_euler_phi():
    """
    Task 3 alt 2
    Test euler phi alt 2 function
    """
    # Edge cases
    assert euler_phi(0) == 0  # May be undefined, but assuming it returns 0
    assert euler_phi(1) == 1  # Only 1 is coprime with itself

    # Prime numbers (φ(p) = p - 1)
    assert euler_phi(2) == 1
    assert euler_phi(5) == 4
    assert euler_phi(7) == 6
    assert euler_phi(11) == 10
    assert euler_phi(13) == 12
    assert euler_phi(17) == 16
    assert euler_phi(101) == 100  # Large prime number

    # Powers of prime numbers (φ(p^k) = p^k - p^(k-1))
    assert euler_phi(4) == 2  # 2²
    assert euler_phi(8) == 4  # 2³
    assert euler_phi(9) == 6  # 3²
    assert euler_phi(16) == 8  # 2⁴
    assert euler_phi(1024) == 512  # 2¹⁰

    # Product of two distinct prime numbers (φ(mn) = φ(m)φ(n))
    assert euler_phi(10) == 4  # 2 * 5
    assert euler_phi(14) == 6  # 2 * 7
    assert euler_phi(15) == 8  # 3 * 5
    assert euler_phi(21) == 12  # 3 * 7
    assert euler_phi(22) == 10  # 2 * 11
    assert euler_phi(35) == 24  # 5 * 7
    assert euler_phi(77) == 60  # 7 * 11

    # More composite numbers
    assert euler_phi(12) == 4  # 2² * 3
    assert euler_phi(20) == 8  # 2² * 5
    assert euler_phi(30) == 8  # 2 * 3 * 5


def test_public_to_private_key_alt_1():
    """
    Task 4 alt 1
    Test public to private key alt 1 function.
    """
    assert public_to_private_key_alt_1(7, 143) == 103
    assert public_to_private_key_alt_1(5, 323) == 173
    assert public_to_private_key_alt_1(3, 667) == 411
    assert public_to_private_key_alt_1(17, 187) == 113
    assert public_to_private_key_alt_1(1, 77) == 1
    assert public_to_private_key_alt_1(13, 299) == 61
    with pytest.raises(ValueError):
        public_to_private_key_alt_1(11, 391)


def test_public_to_private_key():
    """
    Task 4 alt 2
    Test public to private key alt 2 function.
    """
    assert public_to_private_key(7, 143) == 103
    assert public_to_private_key(5, 323) == 173
    assert public_to_private_key(3, 667) == 411
    assert public_to_private_key(17, 187) == 113
    assert public_to_private_key(1, 77) == 1
    assert public_to_private_key(13, 299) == 61
    with pytest.raises(ValueError):
        public_to_private_key(11, 391)
