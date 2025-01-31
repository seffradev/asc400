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
Despite RSA's larger key sizes, AES outperforms it in terms of speed.

The computational complexity of RSA relies on mathematical
operations involving the factorization of large prime numbers. 
AES is implemented with computer in mind where every operation
is a single cycle execution, while RSA is not computer optimized
but as a matematical concept instead.

b) The RSA algorithm shares the public key which enables encryption by others.
An attacker can observe the encrypted text and use the public key to perform an analysis.
RSA relies on well-known algorithms.


Question 2:
How many numbers from 1 to n should be tested before
deciding if n is prime or not? Why?

Answer 2:
You only need to test numbers from 2 to the square root of (n), inclusive (n).
A prime number has no divisor other than 1 and itself.
Therefore:
If n is divisible by a, then n = a*b, where a and b are factors of n.
If a is greater than the square root of n, then b must be less than sqrt(n)
This means that all factors (if they exist) are either less than or equal
to the sqrt(n) or paired with another factor greater than sqrt(n).
In short:
Numbers <= 1 are not prime.
2 is a prime number.
Even numbers greater than 2 are not prime.

Julia och Fredrik:

If a number n has a divisor greater than sqrt(n), the other divisor must
be smaller than sqrt(n), so we only need to check up to sqrt(n).
A prime number has exactly two positive divisors: 1 and itself.

ex. sqrt(28) ≈ 5.3
If any number between 2 and sqrt(28) divides 28 exactly, then 28 is not a prime.
28/2 = 14, 28/4 = 7 - There are integers, therefore 28 is not a primenumber.


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
    if n <= 1:  # Numbers less than or equal to 1 are not prime.
        return False
    if n == 2:  # 2 is a prime number.
        return True
    if n % 2 == 0:  # Eliminate even numbers greater than 2
        return False

    # Check divisors from 3 to sqrt(n) (inclusive)
    limit = int(n**0.5) + 1 # Calculate the integer sqrt(n)
    for i in range(3, limit, 2):    # Only test odd numbers
        if n % i == 0:
            return False
    return True


# Task 2
def modular_inverse(a, b):
    """Compute the modular inverse of a modulo b using the extended Euclidean algorithm."""
    if(a == 1):
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

# Task 3
def euler_phi(n):
    """Euler phi function"""
    phi = n
    if phi == 1:
        return 1
    devider = 2
    to_the_power_of_counter = 0
    list_p_q = []
    list_p_q_to_the_power_of = []
    loop = True

    while loop:
        answer = phi / devider
        if answer == 1:
            return 1
        if is_prime(devider):
            
            if answer % 1 == 0: #If answer is an integer.
                phi = answer
                to_the_power_of_counter += 1
                if is_prime(answer):
                    if answer == devider:
                        to_the_power_of_counter += 1
                        list_p_q.append(phi)
                        list_p_q_to_the_power_of.append(to_the_power_of_counter)
                        loop = False
                    else:
                        list_p_q.append(devider)
                        list_p_q_to_the_power_of.append(to_the_power_of_counter)
                        list_p_q.append(answer)
                        list_p_q_to_the_power_of.append(to_the_power_of_counter)
                        loop = False

            elif is_prime(phi):
                loop = False
                to_the_power_of_counter += 1
                list_p_q.append(devider)
                list_p_q_to_the_power_of.append(to_the_power_of_counter)
                list_p_q.append(phi)
                list_p_q_to_the_power_of.append(to_the_power_of_counter)
                to_the_power_of_counter = 0

            else:
                devider += 1
                if to_the_power_of_counter != 0:
                    list_p_q_to_the_power_of.append(to_the_power_of_counter)
                to_the_power_of_counter = 0
        else:
            devider += 1

    result_list = []
    result = 0

    if len(list_p_q) == 1:
        result = int(n * (1 - (1 / list_p_q[0])))
    elif list_p_q_to_the_power_of[0] == 1 and list_p_q_to_the_power_of[1] == 1:
        for pq in list_p_q:
            answer = pq - 1
            result_list.append(answer)
        result = result_list[0] * result_list[1]
    else:
        result = int(n * (1 - (1 / list_p_q[0])) * (1 - (1 / list_p_q[1])))
    
    return result

def task_3_gcd(a, b):
    rester = [a, b]
    new_a = a
    new_b = b

    while rester[-1] != 0:
        rester.append(new_b % new_a)
        new_b = new_a
        new_a = rester[-1]

    if(rester[-2] == 1):
        return 1

def task_3(n): 
    if(n <= 0):
        return ValueError("Incorrect n value, n must be 1 or more")
    antal_positiva_tal= 1
    for i in range(2, n):
        if task_3_gcd(i,n) == 1:
            antal_positiva_tal +=1
    return antal_positiva_tal

def main():
    """
    The main function, running the project
    """
    print("Hello, world!")

if __name__ == "__main__":
    main()
