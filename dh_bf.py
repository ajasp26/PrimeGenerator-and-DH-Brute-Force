import random
from sympy.ntheory import factorint, isprime
from Crypto.Util.number import getPrime
import time


def generate_prime(bits):
    return getPrime(bits)


def find_primitive_root(prime):
    if not isprime(prime):
        raise ValueError("Number must be prime.")

    p_minus_1 = prime - 1
    factors = factorint(p_minus_1)

    for g in range(2, prime):
        if all(pow(g, p_minus_1 // factor, prime) != 1 for factor in factors):
            return g
    return None


def diffie_hellman_key_exchange(p, g):
    a = random.randint(1, p - 1)  # Choose random private key a
    A = pow(g, a, p)  # A = (g^a) % p
    return a, A


def brute_force_dh(p, g, A):
    k = 1
    start_time = time.perf_counter_ns()
    while pow(g, k, p) != A:
        k += 1
    end_time = time.perf_counter_ns()
    return k, end_time - start_time


for bits in range(10, 33, 2):
    p = generate_prime(bits)
    g = find_primitive_root(p)
    if g is None:
        print(f"No primitive root found for prime of {bits} bits: {p}")
        continue
    a, A = diffie_hellman_key_exchange(p, g)
    _, time_taken = brute_force_dh(p, g, A)
    print(f"{bits}-bit prime: {p}, Primitive root: {g}")
    print(f"DH public key: {A}, Time taken for brute force: {time_taken} nanoseconds")
