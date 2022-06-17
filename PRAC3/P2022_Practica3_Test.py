#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
import unittest
from sympy import isprime

from P2022_Practica3_Skeleton import *


class Test_2_1a(unittest.TestCase):

    def test_1(self):
        r = uoc_bezout(5, 7)
        self.assertEqual(r, (3, -2))

    def test_2(self):
        r = uoc_bezout(123, 456)
        self.assertEqual(r, (-63, 17))

    def test_3(self):
        r = uoc_bezout(121, 982)
        self.assertEqual(r, (-211, 26))

    def test_4(self):
        r = uoc_bezout(1470, 1)
        self.assertEqual(r, (0, 1))

    def test_5(self):
        r = uoc_bezout(1470, 1470)
        self.assertEqual(r, (0, 1))

    def test_6(self):
        r = uoc_bezout(1470, 1478)
        self.assertEqual(r, (-185, 184))


class Test_2_1b(unittest.TestCase):

    def test_7(self):
        r = uoc_crt(2, 11, 4, 5)
        self.assertEqual(r, 24)

    def test_8(self):
        r = uoc_crt(12, 13, 17, 5)
        self.assertEqual(r, 12)

    def test_9(self):
        r = uoc_crt(19, 31, 10, 71)
        self.assertEqual(r, 81)

    def test_10(self):
        r = uoc_crt(5, 31, 9, 71)
        self.assertEqual(r, 222)


class Test_2_2(unittest.TestCase):

    def test_1(self):
        lamb = 2 ** 10
        N, d, p, q = uoc_genkey(lamb)
        self.assertLess(p, lamb)
        self.assertLess(q, lamb)
        self.assertEqual(True, isprime(p))
        self.assertEqual(True, isprime(q))
        self.assertEqual(d % N, 1)
        self.assertEqual(d % (p - 1) * (q - 1), 0)

    def test_2(self):
        lamb = 2 ** 128
        N, d, p, q = uoc_genkey(lamb)
        self.assertLess(p, lamb)
        self.assertLess(q, lamb)
        self.assertEqual(True, isprime(p))
        self.assertEqual(True, isprime(q))
        self.assertEqual(d % N, 1)
        self.assertEqual(d % (p - 1) * (q - 1), 0)

    def test_3(self):
        lamb = 2 ** 256
        N, d, p, q = uoc_genkey(lamb)
        self.assertLess(p, lamb)
        self.assertLess(q, lamb)
        self.assertEqual(True, isprime(p))
        self.assertEqual(True, isprime(q))
        self.assertEqual(d % N, 1)
        self.assertEqual(d % (p - 1) * (q - 1), 0)

    def test_4(self):
        lamb = 2 ** 512
        N, d, p, q = uoc_genkey(lamb)
        self.assertLess(p, lamb)
        self.assertLess(q, lamb)
        self.assertEqual(True, isprime(p))
        self.assertEqual(True, isprime(q))
        self.assertEqual(d % N, 1)
        self.assertEqual(d % (p - 1) * (q - 1), 0)


class Test_2_34(unittest.TestCase):

    def test_1(self):
        N, d, _, _ = uoc_genkey(2 ** 16)
        m = 2
        c = uoc_encrypt(m, N)
        m2 = uoc_decrypt(c, d, N)
        self.assertEqual(m, m2)

    def test_2(self):
        N, d, _, _ = uoc_genkey(2 ** 32)
        m = 71111
        c = uoc_encrypt(m, N)
        m2 = uoc_decrypt(c, d, N)
        self.assertEqual(m, m2)

    def test_3(self):
        N, d, _, _ = uoc_genkey(2 ** 128)
        m = 11111
        c = uoc_encrypt(m, N)
        m2 = uoc_decrypt(c, d, N)
        self.assertEqual(m, m2)

    def test_4(self):
        N, d, _, _ = uoc_genkey(2 ** 512)
        m = 123456789
        c = uoc_encrypt(m, N)
        m2 = uoc_decrypt(c, d, N)
        self.assertEqual(m, m2)

    def test_5(self):
        N, d, _, _ = uoc_genkey(2 ** 1024)
        m = 123456789123456789123456789123456789123456789123456789
        c = uoc_encrypt(m, N)
        m2 = uoc_decrypt(c, d, N)
        self.assertEqual(m, m2)


class Test_3_2(unittest.TestCase):

    def test_1(self):
        N, d, _, _ = uoc_genkey(2 ** 128)
        c_ = uoc_encrypt(5, N) * uoc_encrypt(2, N) * uoc_encrypt(25, N)
        c0 = uoc_encrypt(0, N)
        c1 = c0 * c_ % pow(N, 2)
        print(uoc_decrypt(c1, d, N))
        c = uoc_vote(["YES", "NO", "YES", "YES", "YES"], N)
        count = uoc_vote_count(c, d, N)
        self.assertEqual(count, 4)

    def test_2(self):
        N, d, _, _ = uoc_genkey(2 ** 128)
        c = uoc_vote(["YES", "YES", "YES", "YES", "YES"], N)
        count = uoc_vote_count(c, d, N)
        self.assertEqual(count, 5)

    def test_3(self):
        N, d, _, _ = uoc_genkey(2 ** 128)
        c = uoc_vote(["NO", "NO", "NO", "NO", "YES"], N)
        count = uoc_vote_count(c, d, N)
        self.assertEqual(count, 1)

    def test_4(self):
        N, d, _, _ = uoc_genkey(2 ** 128)
        c = uoc_vote(["NO", "NO", "NO", "NO", "NO"], N)
        count = uoc_vote_count(c, d, N)
        self.assertEqual(count, 0)


if __name__ == '__main__':

    # create a suite with all tests
    test_classes_to_run = [
        Test_2_1a,
        Test_2_1b,
        Test_2_2,
        Test_2_34,
        Test_3_2,
    ]
    loader = unittest.TestLoader()
    suites_list = []
    for test_class in test_classes_to_run:
        suite = loader.loadTestsFromTestCase(test_class)
        suites_list.append(suite)

    all_tests_suite = unittest.TestSuite(suites_list)

    # run the test suite with high verbosity
    runner = unittest.TextTestRunner(verbosity=2)
    results = runner.run(all_tests_suite)
