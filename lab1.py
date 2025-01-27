"""
Question 1:
What makes an asymmetric scheme like RSA slower than its
symmetric alternatives such as AES? Explain. Also, what
information in the RSA key generator, encryption and
decryption algorithms an attacker may have access to?

Answer 1:
The Advanced Encryption Standard (AES) is faster than the
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
Despite RSA's larger key sizes, AES outperforms it in terms of speed.

The computational complexity of RSA relies on mathematical
operations involving the factorization of large prime numbers. 
AES is implemented with computer in mind where every operation
is a single cycle execution, while RSA is not computer optimized
but as a matematical concept instead.

Question 2:
How many numbers from 1 to n should be tested before
deciding if n is prime or not? Why?

Answer 2:

Question 3:
Alice wants to send m=15 to Bob. She gets Bob's public
key pk=(19,77) by visiting a public repository. If she
decides to use RSA for encryption, what would the
resulting cipher text be? (Show your calculation)

Answer 3:

"""


def func(a: int, b: int) -> int:
    """
    Return the sum of `a` and `b`
    """
    return a + b


def main():
    """
    The main function, running the project
    """
    print("Hello, world!")


if __name__ == "__main__":
    main()
