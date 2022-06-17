#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sympy import randprime, isprime

# --- IMPLEMENTATION GOES HERE ---------------------------------------------
#  Student helpers (functions, constants, etc.) can be defined here, if needed

VOTES_MAP = {
    'YES': 1,
    'NO': 0
}


# --------------------------------------------------------------------------


def uoc_bezout(a, b):
    """
    Implements the Euclides Algorithm for finding the Bezout Identity:
    \lambda * a + \mu * b = d
    (See Theorem 2 and 3)

    :param a: integer value.
    :param b: integer value.
    :return: lambda and mu values
    """

    lamb = 1
    mu = 1
    # --- IMPLEMENTATION GOES HERE ---
    # a = 1*a + 0*b
    (r1, x1, y1) = (a, 1, 0)
    # b = 0*a + 1*b
    (r2, x2, y2) = (b, 0, 1)

    while r2 != 0:
        # dividing r1 by r2 to get r3:
        # r1 = q3*r2 + r3
        q3 = r1 // r2
        r3 = r1 % r2

        # r3 = r1 - q3*r2
        #    = x1*a + y1*b - q3*(x2*a + y2*b)
        #    = (x1 - q3*x2)*a + (y1 - q3*y2)*b
        x3 = (x1 - q3 * x2)
        y3 = (y1 - q3 * y2)

        # next step r1 will be our current r2
        # and r2 will be our current r3
        (r1, x1, y1) = (r2, x2, y2)
        (r2, x2, y2) = (r3, x3, y3)

    (lamb, mu) = (x1, y1)
    # --------------------------------

    return (lamb, mu)


def uoc_crt(a1, n1, a2, n2):
    """
    Implements the Chines remainder theorem using the uoc_bezout()
    function for solving the modular system:
    x = a1 mod n1
    x = a2 mod n2
    (See Theorem 7)

    :param a1: the 'a1' value of the modular system.
    :param n1: the 'n1' value of the modular system.
    :param a2: the 'a2' value of the modular system.
    :param n2: the 'n2' value of the modular system.
    :return: the 'x' value
    """

    x = 1
    # --- IMPLEMENTATION GOES HERE ---
    r = uoc_bezout(n1, n2)
    x = (r[1] * n2 * a1 + r[0] * n1 * a2) % (n1 * n2)
    # --------------------------------

    return x


def uoc_genkey(lamb):
    """
    Generate a random key for the proposed cryptosystem.

    :param lamb: lambda parameter
    :return: key values (N, d, p, q)
    """

    N, d, p, q = 1, 1, 1, 1

    # --- IMPLEMENTATION GOES HERE ---
    a = 1
    p = randprime(a, lamb)
    q = randprime(a, lamb)
    N = p * q
    phi_euler = (p - 1) * (q - 1)

    # d = 1 mod N
    # d = 0 mod (p-1)(q-1)

    d = uoc_crt(1, N, 0, phi_euler)

    # --------------------------------

    return (N, d, p, q)


def uoc_encrypt(m, N):
    """
    Encrypt the message using the proposed cryptosystem.

    :param m: integer containing the message to encrypt
    :return: the encrypted message
    """

    c = 1
    # --- IMPLEMENTATION GOES HERE ---
    # c = (1 + N)^m · r^N mod N^2
    mod = pow(N, 2)
    r = randprime(1, N)
    c = pow(1 + N, m, mod) * pow(r, N, mod) % mod
    # --------------------------------

    return c


def uoc_decrypt(c, d, N):
    """
    Decrypt the message using the proposed cryptosystem.

    :param c: integer containing the message to decrypt
    :return: the decrypted message
    """

    m = 1

    # --- IMPLEMENTATION GOES HERE ---
    # m = (c^d mod N^2) - 1 / N
    mod = pow(N, 2)
    b = (pow(c, d, mod) - 1) % mod
    m = round(b // N)
    # --------------------------------

    return m


def uoc_vote(votes, N):
    """
    Encrypt the votes using the proposed cryptosystem.

    :param votes: list of "YES", "NO" votes
    :return: encrypted votes
    """

    c = 1

    # --- IMPLEMENTATION GOES HERE ---
    for i in range(len(votes)):
        vote = (VOTES_MAP[votes[i]])
        c *= uoc_encrypt(vote, N)
    # --------------------------------

    return c


def uoc_vote_count(c, d, N):
    """
    Count the votes using the proposed cryptosystem.

    :param votes: list of "YES", "NO" votes
    :return: encrypted votes
    """

    count = 1

    # --- IMPLEMENTATION GOES HERE ---
    c0 = uoc_encrypt(0, N)
    c1 = c0 * c % pow(N, 2)
    count = uoc_decrypt(c1, d, N)
    # --------------------------------

    return count
