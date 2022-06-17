#!/usr/bin/env python
# -*- coding: utf-8 -*-


# --- IMPLEMENTATION GOES HERE ---------------------------------------------
#  Student helpers (functions, constants, etc.) can be defined here, if needed

def decimalToBinary(n):
    # converting decimal to binary
    # and removing the prefix(0b)
    return bin(n).replace("0b", "")


TRUTH_TABLE = ['000', '001', '011', '110', '100', '101', '010', '111']


# --------------------------------------------------------------------------


def uoc_xor(str1, str2):
    """
    Implements an XOR operation.

    :param str1: string of 1 and 0s with the binary representation of the messsage
    :param str2: string of 1 and 0s with the binary representation of the messsage
    :return: tring of 1 and 0s with the binary representation of the result.

    """

    xor = ""

    # --- IMPLEMENTATION GOES HERE ---
    for i in range(len(str1)):
        xor += str(int(str1[i]) ^ int(str2[i]))

    # --------------------------------

    return xor


def uoc_congruential_generator(a, b, m, x):
    """
    Implements a congruential generator.

    :param a: the 'a' value of the generator.
    :param b: the 'b' value of the generator.
    :param m: module of the generator.
    :param x: initial value of the sequence
    :return: integer containing the next element of the sequence
    """

    next_value = 1

    # --- IMPLEMENTATION GOES HERE ---
    next_value = (a * x + b) % m
    # --------------------------------

    return next_value


def uoc_bad_stream_cipher(message, key):
    """
    Implements the Bad Stream Cipher.

    :param message: string of 1 and 0s with the binary representation of the messsage we want to encrypt or decrypt
    :param key: integer that represents the x_0 value of the generator
    :return: string of 1 and 0s with the binary representation of the ciphered or deciphered message
    """

    a = 3
    b = 7
    m = 2 ** 8
    cipher_text = ""

    # --- IMPLEMENTATION GOES HERE ---
    length = len(message)
    i = 0

    while i < length:

        str1 = str(message[i:i + 8])
        key = key if i == 0 else uoc_congruential_generator(a, b, m, key)
        str2 = str((decimalToBinary(key)))

        if len(str2) > 8:
            str2 = str2[0:8]
        elif len(str2) < 8:
            str2 = str2.rjust(8, '0')

        cipher_text += uoc_xor(str1, str2)

        i += 8

    # --------------------------------

    return cipher_text


def uoc_calc_period(a, b, m, x_0):
    """
    Calculate the period of a congruential generator.

    :param x_0: integer that represents the initial value of the generator
    :param a: the 'a' value of the generator.
    :param b: the 'b' value of the generator.
    :param m: module of the generator.
    :return: period 
    """

    period = 0

    # --- IMPLEMENTATION GOES HERE ---
    key = 0
    x = x_0
    found = False

    while not found:
        if key == 0:
            key = x
            period += 1
            x = uoc_congruential_generator(a, b, m, x)
        elif key != x:
            x = uoc_congruential_generator(a, b, m, x)
            period += 1
        else:
            found = True

    # --------------------------------

    return period


def uoc_flipping_attack(ciphertext):
    """
    Bit Flipping attack

    :param ciphertext: string of 1 and 0s with the binary representation of the captured ciphertext
    :return: list containing 4 ciphertext to reply
    """

    ciphertexts_to_reply = []
    # --- IMPLEMENTATION GOES HERE ---

    for i in range(len(TRUTH_TABLE)):
        ciphertexts_to_reply.append(ciphertext[:13] + TRUTH_TABLE[i])
    # --------------------------------

    return ciphertexts_to_reply


# 6 - Exercici implementació
# Implementació de xifratge de bloc amb mode CBC

def ex6(message, v, key):
    length = len(message)
    i = 0
    blocs_xifrats = ''

    while i < length:
        m = str(message[i:i + 2])
        v = E(uoc_xor(m, v), key)
        blocs_xifrats += v
        i += 2

    return blocs_xifrats


def E(input, k):
    xifratge = {
        '00': {
            '00': '11',
            '01': '00',
            '10': '01',
            '11': '10'
        },
        '01': {
            '00': '10',
            '01': '01',
            '10': '11',
            '11': '00'
        },
        '10': {
            '00': '01',
            '01': '10',
            '10': '00',
            '11': '11'
        },
        '11': {
            '00': '00',
            '01': '11',
            '10': '10',
            '11': '01'
        }
    }

    return xifratge[input][k]


"""
message = '1001100100110000'
v = '10'
key = '10'
print(ex6(message, v, key))
"""
