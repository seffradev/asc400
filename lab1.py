"""
Question 1:
What makes an asymmetric scheme like RSA slower than its
symmetric alternatives such as AES? Explain. Also, what
information in the RSA key generator, encryption and
decryption algorithms an attacker may have access to?

Answer 1:
AES (Advanced Encryption Standard) is faster than RSA (Rivest-Shamir-Adleman)
especially when encryption large amounts of data, because of: algorithm design, default in key length,
computational complexity and hardware support in modern CPUs. Algoritm design has 
diffrent structures such as asymmetrical and symmetrical and RSA is a asymmetrical one.
RSA is known for its larger keys (usually 1024 bits) then AES which has smaller keys (usually 256 bits) but it calculate it faster.
The complexity for the RSA builds on matematical operations which involves factorization with big primnumbers.
AES is implemented with computer in mind where every operation is a single cycle execution, while RSA is not computer 
optimized but as a matematical concept instead.




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
