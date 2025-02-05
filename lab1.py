"""
Question 1:
a) What makes an asymmetric scheme like RSA slower than its
symmetric alternatives such as AES? Explain.
b) Also, what information in the RSA key generator, encryption and
decryption algorithms an attacker may have access to?

Answer 1:
a) The Advanced Encryption Standard (AES) is faster than the
Rivest-Shamir-Adleman (RSA) algorithm, particularly when
encrypting large amounts of data. This performance difference
can be attributed to several factors, including algorithm
design, default key lengths, computational complexity,
and hardware support in modern CPUs.

AES and RSA differ fundamentally in their algorithmic
structures; AES is a symmetric encryption algorithm,
while RSA is an asymmetric one. RSA is characterized by its
use of larger key sizes, typically 1024 bits or more, compared
to AES, which commonly uses smaller key sizes, such as 256 bits.
The key size difference can intuitively lead to AES outperforming
RSA.

The computational complexity of RSA relies on mathematical
operations involving the factorization of large prime numbers.
AES is implemented with computer in mind where every operation
is a single cycle execution, while RSA is not computer optimized
but as a matematical concept instead. This makes AES easy to
implement at the hardware level meaning pure CPU instructions can
perform an encryption and decryption with AES, while RSA is too
complex.

b) The RSA algorithm shares the public key which enables encryption by others.
An attacker can observe the encrypted text and use the public key to perform an analysis.
RSA relies on well-known algorithms.


Question 2:
How many numbers from 1 to n should be tested before
deciding if n is prime or not? Why?

If a number n has a divisor greater than or equal to sqrt(n), the
other divisor must be smaller than or equal to sqrt(n), so we only
need to check up to sqrt(n). A prime number has exactly two positive
divisors: 1 and itself.

ex. sqrt(28) ≈ 5.3
If any number between 2 and sqrt(28) divides 28 exactly, then 28 is not a prime.
28/2 = 14, 28/4 = 7 - There are integers, therefore 28 is not a prime number.


Question 3:
Alice wants to send m=15 to Bob. She gets Bob's public
key pk=(19,77) by visiting a public repository. If she
decides to use RSA for encryption, what would the
resulting cipher text be? (Show your calculation)

Answer 3:

N=77
e=19

c = m**e mod N
c = 15**19 mod 77

19 = 0001 0011 = 2**0+2**1+2**4
19 = 1 + 2 + 16
c = 15**(1+2+16) mod 77


15**1 mod 77 = 15

15**2 mod 77 =
(15 * 15) mod 77 =
225 mod 77 = 71

15**4 mod 77 =
(71*71) mod 77 =
5041 mod 77 = 36

15**8 mod 77 =
(36*36) mod 77 =
1296 mod 77 = 64

15**16 mod 77 =
(64*64) mod 77 =
4096 mod 77 = 15

c = 15**19 mod 77 =
(15*71*15) mod 77 =
15975 mod 77 = 36

Answer: c = 36

Reference:
https://www.khanacademy.org/computing/computer-science/cryptography/modarithmetic/a/fast-modular-exponentiation

"""


# Task 1:
def is_prime(n):
    """Check if a given number is prime."""
    if not isinstance(n, int):
        return False
    if n <= 1:  # Numbers less than or equal to 1 are not prime.
        return False
    if n == 2:  # 2 is a prime number.
        return True
    if n % 2 == 0:  # Eliminate even numbers greater than 2
        return False

    # Check divisors from 3 to sqrt(n) (inclusive)
    limit = int(n**0.5) + 1  # Calculate the integer sqrt(n)
    for i in range(3, limit, 2):  # Only test odd numbers
        if n % i == 0:
            return False

    return True


# Task 2 alt 1
def modular_inverse(a, b):
    """Compute the modular inverse of a modulo b using the extended Euclidean algorithm."""
    if a == 1:
        return 1
    quotient = []
    remainders = [a, b]
    new_a = a
    new_b = b

    while remainders[-1] != 0:
        quotient.append(new_b // new_a)
        remainders.append(new_b % new_a)
        new_b = new_a
        new_a = remainders[-1]

    if remainders[-2] != 1:
        raise ValueError(f"{a} and {b} are not relatively prime")

    x_list = [0]
    y_list = [1]
    for item in reversed(quotient):
        x = y_list[-1] - item * x_list[-1]
        y = x_list[-1]
        x_list.append(x)
        y_list.append(y)

    return x_list[-1] % b


# Task 2 alt 2
def eea(e, n):
    """Extended Euclidean algorithm

    Refer to Lab1_ RSA toolbox.pdf, page 9.
    According to the reference, the greatest common divisor (GCD)
    must be calculated to find the modular inverse of e modulo N.

    GCD (e, Ф (N)) = 1
    inverse (i) = inverse (i-2) - (inverse (i-1) * quotient (i-1))
    """

    if gcd(e, n) != 1:
        raise ValueError("Not relative prime")

    new_n = n
    new_e = e
    inverse = [0, 1]
    quotient = [0]
    while new_e != 0:
        quotient.append(new_n // new_e)
        new_n, new_e = new_e, new_n % new_e
        inverse.append(inverse[-2] - (inverse[-1] * quotient[-1]))

    return inverse[-2] % n


def gcd(e, n):
    """Find gcd"""
    if e == 0:
        return n
    if n == 0:
        return e

    list_e = []
    list_n = []

    divider_e = 1
    divider_n = 1

    while True:
        result = abs(e) / divider_e
        if result % 1 == 0:
            list_e.append(int(result))
        divider_e += 1
        if divider_e > abs(e):
            break

    while True:
        result = abs(n) / divider_n
        if result % 1 == 0:
            list_n.append(int(result))
        divider_n += 1
        if divider_n > abs(n):
            break

    list_gcd = []

    for number_e in list_e:
        for number_n in list_n:
            if number_e == number_n:
                list_gcd.append(number_e)

    return max(list_gcd)


# Task 3 alt 1
def task_3_gcd(a, b):
    """
    GCD
    lab1.py:218:0: R1710: Either all return statements in
    a function should return an expression, or none of them should.
    (inconsistent-return-statements)
    """
    rester = [a, b]
    new_a = a
    new_b = b

    while rester[-1] != 0:
        rester.append(new_b % new_a)
        new_b = new_a
        new_a = rester[-1]

    if rester[-2] == 1:
        return 1


def task_3(n):
    """Euler phi
    with pytest.raises(ValueError):
        task_3(0)
    """
    if n <= 0:
        return ValueError("Incorrect n value, n must be 1 or more")
    antal_positiva_tal = 1
    for i in range(2, n):
        if task_3_gcd(i, n) == 1:
            antal_positiva_tal += 1
    return antal_positiva_tal


# Task 3 alt 2
def euler_phi(n):
    """Euler phi function
    Refer to Lab1_ RSA toolbox.pdf, page 4.
    "Find its prime factors and find the greatest common one"

    Refer to https://www.geeksforgeeks.org/eulers-totient-function/
    "If n is a prime number"
    "If n is a power of a prime p**k"
    "Multiplicative Property"
    "General formula"
    """
    if n <= 0:
        return 0
    if prime_factorization(n) == 1:
        return 1
    [list_p_q], [list_p_q_to_the_power_of] = prime_factorization(n)

    result_list = []
    result = 0

    if len(list_p_q) == 1:  # Rule: General formula
        result = int(n * (1 - (1 / list_p_q[0])))
    elif list_p_q_to_the_power_of[-2:] == [
        1,
        1,
    ]:  # Rule: n=p×q, two different prime numbers
        for pq in list_p_q:
            answer = pq - 1
            result_list.append(answer)
        result = result_list[-2] * result_list[-1]
    else:  # Rule: n = p**k, prime number to the power of k
        result = int(n * (1 - (1 / list_p_q[-2])) * (1 - (1 / list_p_q[-1])))

    return result


def prime_factorization(n):
    """Prime factorization
    Take the number and divide it by the smallest prime, 2.
    Check if the result is an integer and whether it is prime.
    If it is not an integer, divide the original number by the next prime.
    If it is an integer but not a prime, continue dividing by 2.
    When a prime factor is found, add it to the list along with the count
    of divisions to represent its exponent.
    """
    phi = n
    devider = 2
    to_the_power_of_counter = 0
    list_p_q = []
    list_p_q_to_the_power_of = []

    while True:
        answer = phi / devider
        if answer == 1 or phi == 1:
            return 1
        if is_prime(devider):
            to_the_power_of_counter += 1
            if answer % 1 == 0:  # If answer is an integer.
                phi = answer
                if is_prime(answer):
                    if answer == devider:
                        list_p_q.append(phi)
                        list_p_q_to_the_power_of.append(to_the_power_of_counter)
                        break

                    list_p_q.append(devider)
                    list_p_q_to_the_power_of.append(to_the_power_of_counter)
                    list_p_q.append(answer)
                    list_p_q_to_the_power_of.append(to_the_power_of_counter)
                    break

            elif is_prime(phi):  # Rule: n is prime number
                list_p_q.append(devider)
                list_p_q_to_the_power_of.append(to_the_power_of_counter)
                list_p_q.append(phi)
                list_p_q_to_the_power_of.append(to_the_power_of_counter)
                to_the_power_of_counter = 0
                break

            else:
                devider += 1
                if to_the_power_of_counter != 0:
                    list_p_q_to_the_power_of.append(to_the_power_of_counter)
                to_the_power_of_counter = 0
        else:
            devider += 1
    return [list_p_q], [list_p_q_to_the_power_of]


# Task 4, alt 1
def public_to_private_key_alt_1(e, n):
    """Find secret key (d, n) from public key (e, n).

    Refer to Lab 1_RSA Toolbox_lab manual.pdf, page 5.
    d = e**-1 mod Ф (N)
    """
    modulus_n = task_3(n)
    inverse_e = modular_inverse(e, modulus_n)
    d = inverse_e % modulus_n
    return d


# Task 4, alt 2
def public_to_private_key(e, n):
    """Find secret key (d, n) from public key (e, n).

    Refer to Lab 1_RSA Toolbox_lab manual.pdf, page 5.
    d = e**-1 mod Ф (N)
    """
    modulus_n = euler_phi(n)
    inverse_e = eea(e, modulus_n)
    d = inverse_e % modulus_n
    return d


# Main
def main():
    """
    The main function, running the project
    """
    print("Hello, world!")


if __name__ == "__main__":
    main()
