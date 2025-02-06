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

Answer 2:
If a number n has a divisor greater than or equal to sqrt(n), the
other divisor must be smaller than or equal to sqrt(n), so we only
need to check up to sqrt(n). A prime number has exactly two positive
divisors: 1 and itself.

ex. sqrt(28) ≈ 5.3
If any number between 2 and sqrt(28) divides 28 exactly, then 28 is not a prime.
28/2 = 14, 28/4 = 7 - They are integers, therefore 28 is not a prime number.


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


# Task 1
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


# Task 2
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
    """Find greatest common divisor"""
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
        # Check if the float returned is actually an integer
        if result % 1 == 0:
            list_e.append(int(result))
        divider_e += 1
        if divider_e > abs(e):
            break

    while True:
        result = abs(n) / divider_n
        # Check if the float returned is actually an integer
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


# Task 3
def phi(n):
    """Euler phi"""
    if n <= 0:
        raise ValueError("Incorrect n value, n must be 1 or greater")
    coprimes = 1
    for i in range(2, n):
        if gcd(i, n) == 1:
            coprimes += 1
    return coprimes


# Task 4
def modular_inverse(e, n):
    """Find secret key (d, n) from public key (e, n).

    Refer to Lab 1_RSA Toolbox_lab manual.pdf, page 5.
    d = e**-1 mod Ф (N)
    """
    modulus_n = phi(n)
    inverse_e = eea(e, modulus_n)
    d = inverse_e % modulus_n
    return d


def get_action():
    """Get an action from the user; it repeats by default"""
    action = "repeat"

    try:
        print("1. is_prime")
        print("2. eea")
        print("3. phi")
        print("4. inverse")
        print("5. exit")
        task = int(input("Pick a task: "))
        # Python doesn't have good enums :(
        if task == 1:
            action = "is_prime"
        if task == 2:
            action = "eea"
        if task == 3:
            action = "phi"
        if task == 4:
            action = "inverse"
        if task == 5:
            action = "exit"
    except ValueError:
        print("You should enter an integer")

    return action


def main():
    """
    The main function, running the interactive version
    of the project
    """
    running = True
    while running:
        action = get_action()

        if action == "exit":
            running = False
        elif action == "is_prime":
            try:
                number = int(input("Enter a number to see if it's prime: "))
                print(number, "is" if is_prime(number) else "is not", "prime")
            except ValueError as e:
                print(e)
        elif action == "eea":
            try:
                e = int(input("Enter e: "))
                n = int(input("Enter n: "))
                print(eea(e, n))
            except ValueError:
                print(e)
        elif action == "phi":
            try:
                number = int(
                    input("Enter a number to calculate Euler's totient function on: ")
                )
                print(phi(number))
            except ValueError as e:
                print(e)
        elif action == "inverse":
            try:
                e = int(input("Enter e: "))
                n = int(input("Enter n: "))
                print(modular_inverse(e, n))
            except ValueError as e:
                print(e)


if __name__ == "__main__":
    main()
