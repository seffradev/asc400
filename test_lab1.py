"""
A test file to run in CI and with `pytest`.
"""

from lab1 import is_prime
from lab1 import euler_phi


def test_is_prime():
    """Test cases for the is_prime function."""
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

def test_euler_phi():
    """Test euler phi function"""
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
