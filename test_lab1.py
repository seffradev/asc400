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


# Task 2
def modular_inverse(a,b):
    kvot= []
    rester= [a,b]
    new_a= a
    new_b= b

    while rester[-1] != 0:
        kvot.append(new_b//new_a)
        rester.append(new_b % new_a)
        new_b = new_a
        new_a= rester[-1]

    if(rester[-2] != 1):
        raise ValueError(f"{a} och {b} är inte relativt prima")



    xList = [0]
    yList = [1]
    for item in reversed(kvot):
        x = yList[-1] - item * xList[-1]
        y = xList[-1]
        xList.append(x)
        yList.append(y)

    return xList[-1] % b


