#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
import unittest

from P2022_Practica2_Skeleton import *
#from P2022_Practica2_Solution_Skeleton import *


class Test_1_1(unittest.TestCase):

    def test_1(self):
        str1 = "00000000"
        str2 = "00000001"
        xor = uoc_xor(str1, str2)
        self.assertEqual(xor, "00000001")

    def test_2(self):
        str1 = "10101010"
        str2 = "01010101"
        xor = uoc_xor(str1, str2)
        self.assertEqual(xor, "11111111")

    def test_3(self):
        str1 = "11101010"
        str2 = "01010111"
        xor = uoc_xor(str1, str2)
        self.assertEqual(xor, "10111101")


class Test_1_2(unittest.TestCase):

    def test_1(self):
        x = uoc_congruential_generator(2, 5, 13, 2)
        self.assertEqual(x, 9)

    def test_2(self):
        x = uoc_congruential_generator(5, 7, 2**16, 7)
        self.assertEqual(x, 42)

    def test_3(self):
        x = uoc_congruential_generator(71, 11, 1331, 7)
        self.assertEqual(x, 508)


class Test_1_3(unittest.TestCase):

    def test_1(self):
        msg = "0000000100000001000000010000000100000001000000010000000100000001"
        key = 1
        ciphertext = uoc_bad_stream_cipher(msg, key)
        self.assertEqual(ciphertext, "0000000000001011001001000111011101101000010000111100110001101111")

    def test_2(self):
        msg = "0000000000001011001001000111011101101000010000111100110001101111"
        key = 1
        ciphertext = uoc_bad_stream_cipher(msg, key)
        self.assertEqual(ciphertext, "0000000100000001000000010000000100000001000000010000000100000001")

    def test_3(self):
        msg = "1001010101000101000101111000001111110010101000101010010100000001"
        key = 1
        ciphertext = uoc_bad_stream_cipher(msg, key)
        self.assertEqual(ciphertext, "1001010001001111001100101111010110011011111000000110100001101111")

    def test_4(self):
        msg = "1001010001001111001100101111010110011011111000000110100001101111"
        key = 1
        ciphertext = uoc_bad_stream_cipher(msg, key)
        self.assertEqual(ciphertext, "1001010101000101000101111000001111110010101000101010010100000001")



class Test_2_1(unittest.TestCase):

    def test_1(self):
        p = uoc_calc_period(11, 7, 31, 17)
        self.assertEqual(p, 30)

    def test_2(self):
        p = uoc_calc_period(3, 11, 29, 2)
        self.assertEqual(p, 28)

    def test_3(self):
        p = uoc_calc_period(31, 39, 1429, 5)
        self.assertEqual(p, 204)


class Test_2_4(unittest.TestCase):

    def test_1(self):

        k = random.randint(2, 100000)
        opendoor_code = "10001000"
        door_id = "00000"+''.join([random.choice(["0", "1"]) for i in range(3)])
        cmd = uoc_bad_stream_cipher(opendoor_code+door_id, k)

        options = uoc_flipping_attack(cmd)
        self.assertEqual(len(options), 8)

        for opt in options:
            plaintext = uoc_bad_stream_cipher(opt, k)
            door_id = plaintext[8:]
            self.assertEqual(plaintext[:8], "10001000")
            if(door_id == "00000001"):
                break
        self.assertEqual(door_id, "00000001")


if __name__ == '__main__':

    # create a suite with all tests
    test_classes_to_run = [
        Test_1_1, 
        Test_1_2, 
        Test_1_3, 
        Test_2_1, 
        Test_2_4, 
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

