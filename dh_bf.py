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


# Alice creates 'a'.
def diffie_hellman_key_exchange(p, g):
    a = random.randint(1, p - 1)  # Select a private key a randomly.
    A = pow(g, a, p)  # Calculate public key A as g^a mod p.
    return a, A


# Charlie's brute force attempt to figure out 'a'.
def brute_force_dh(p, g, A):
    k = 1
    start_time = time.perf_counter_ns()  # Start timing.
    while pow(g, k, p) != A:
        k += 1  # Increment k until g^k mod p equals A.
    end_time = time.perf_counter_ns()  # Stop timing.
    return k, end_time - start_time  # Return the discovered key and time taken.


# Loop through specified bit sizes and perform tests.
for bits in range(10, 31, 5):
    total_time = 0
    valid_trials = 0
    for trial in range(10):
        p = generate_prime(bits)
        g = find_primitive_root(p)
        if g is None:
            continue  # Skip if no primitive root is found.
        _, A = diffie_hellman_key_exchange(p, g)
        _, time_taken_ns = brute_force_dh(p, g, A)
        total_time += time_taken_ns
        valid_trials += 1

    if valid_trials > 0:
        average_time_ns = total_time / valid_trials
        print(
            f"{bits}-bit prime, Average time taken for brute force over {valid_trials} trials: {average_time_ns:,.0f} nanoseconds")
    else:
        print(f"No valid trials for {bits}-bit primes due to lack of primitive roots.")
