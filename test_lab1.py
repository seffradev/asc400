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
    number = int(input("Enter an integer to check if it's prime: "))
    if is_prime(number):
        print(f"{number} is a prime number.")
    else:
        print(f"{number} is not a prime number.")


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


