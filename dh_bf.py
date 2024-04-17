import random
from sympy.ntheory import factorint, isprime
from Crypto.Util.number import getPrime
import time


# Generate a prime number with a given number of bits.
def generate_prime(bits):
    return getPrime(bits)


# Find a primitive root for a given prime number.
def find_primitive_root(prime):
    if not isprime(prime):
        raise ValueError("Number must be prime.")

    p_minus_1 = prime - 1
    factors = factorint(p_minus_1)  # Factor p-1 to find primitive roots.

    for g in range(2, prime):  # Test potential primitive roots g.
        if all(pow(g, p_minus_1 // factor, prime) != 1 for factor in factors):
            return g  # Return g if it is a primitive root.
    return None  # Return None if no primitive root is found.


# Perform the Diffie-Hellman key exchange setup.
def diffie_hellman_key_exchange(p, g):
    a = random.randint(1, p - 1)  # Select a private key a randomly.
    A = pow(g, a, p)  # Calculate public key A as g^a mod p.
    return a, A


# Brute force to find the private key given a public key.
def brute_force_dh(p, g, A):
    k = 1
    start_time = time.perf_counter_ns()  # Start timing.
    while pow(g, k, p) != A:
        k += 1  # Increment k until g^k mod p equals A.
    end_time = time.perf_counter_ns()  # Stop timing.
    return k, end_time - start_time  # Return the discovered key and time taken.


# Main loop to test keys of various sizes.
for bits in range(10, 33, 2):
    p = generate_prime(bits)  # Generate prime of size 'bits'.
    g = find_primitive_root(p)  # Find a primitive root for prime p.
    if g is None:
        print(f"No primitive root found for prime of {bits} bits: {p}")
        continue
    a, A = diffie_hellman_key_exchange(p, g)  # Perform key exchange.
    _, time_taken = brute_force_dh(p, g, A)  # Attempt to break DH exchange.
    print(f"{bits}-bit prime: {p}, Primitive root: {g}")
    print(f"DH public key: {A}, Time taken for brute force: {time_taken} nanoseconds")
