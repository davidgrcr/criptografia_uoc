#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# --- IMPLEMENTATION GOES HERE -----------------------------------------------
#  Student helpers (functions, constants, etc.) can be defined here, if needed
ALPHABET_LENGTH = 26
alfabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
alfabet2 = "abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZ.,;:_-*=)(1234567890"
freq1 = "EAISOLNRTUDCMQPBGVFHXYJKWZ"
freq2 = "EAOSNRLDUICTMBPQYHGVFZJXKW"
clau = "=)(abcdefghijklmnopqrstuvwxyz.,;:ABCDEFGHIJKLMNOPQRSTUVWXYZ_-*1234567890"

# Funció per trobar totes les vegades que apareix un caràcter en una cadena de text
def find_all_occurrences(ch, txt):
    occurrence = 0
    for i in range(len(txt)):
        if txt[i] == ch:
            occurrence += 1
    return occurrence


# ----------------------------------------------------------------------------


def uoc_simple_subs_cipher(message, shift):
    """
    EXERCISE 1.1: Simple substitution cipher
    :message: message to cipher (plaintext)
    :shift: offset or displacement
    :return: ciphered text
    """

    ciphertext = ""

    #### IMPLEMENTATION GOES HERE ####

    # Funció lambda que retornar el index xifrat amb xifra de Cèsar
    index_xifrat = lambda index, shift: (index + shift) % ALPHABET_LENGTH

    for x in message:
        index = index_xifrat(alfabet.index(x), shift)
        ciphertext += alfabet[index]
    # --------------------------------

    return ciphertext


def uoc_simple_subs_decipher(message, shift):
    """
    EXERCISE 1.2: Simple substitution decipher
    :message: message to cipher (plaintext)
    :shift: offset or displacement
    :return: ciphered text
    """

    plaintext = ""

    #### IMPLEMENTATION GOES HERE ####
    # Funció lambda que retornar el index desxifrat amb xifra de Cèsar
    index_desxifrat = lambda index, shift: (index - shift) % ALPHABET_LENGTH

    for x in message:
        index = index_desxifrat(alfabet.index(x), shift)
        plaintext += alfabet[index]
    # --------------------------------

    return plaintext


def uoc_mono_subs_cipher(message, subs_alphabet):
    """
    EXERCISE 1.3: Monoalphabetic substitution cipher
    :message: message to cipher (plaintext)
    :subs_alphabet: substitution alphabet
    :return: ciphered text
    """

    ciphertext = ""

    #### IMPLEMENTATION GOES HERE ####
    for x in message:
        index = alfabet.index(x)                    # Trobem l'index del caràcter en l'alfabet normal
        ciphertext += subs_alphabet[index]          # i en el subs alfabet agafem el index trobat per tal de tornar el
                                                    # caràcter xifrat
    # --------------------------------

    return ciphertext


def uoc_mono_subs_decipher(message, subs_alphabet):
    """
    EXERCISE 1.4: Monoalphabetic substitution decipher
    :message: message to cipher (plaintext)
    :subs_alphabet: substitution alphabet
    :return: ciphered text
    """

    plaintext = ""

    #### IMPLEMENTATION GOES HERE ####
    for x in message:
        index = subs_alphabet.index(x)          # Trobem l'index del caràcter en el subs alfabet
        plaintext += alfabet[index]             # i en el alfabet normal agafem el index trobat per tal de tornar el
                                                # caràcter desxifrat
    # --------------------------------

    return plaintext


def uoc_find_shift(message):
    """
    EXERCISE 2.1: Find shift used by the simple substitution
    :message: encrypted message
    :return: estimated shift value
    """

    shift = -1

    #### IMPLEMENTATION GOES HERE ####
    dictionary = {}
    # Busquem totes les vegades que tenim cada caracter en el text, i ho guardem en un diccionari per tal de poder ordenar els
    # caràcters en ordre descent pel nombre de vegades que han aparegut cada caràcter.
    for i in range(len(freq1)):
        occurrences = find_all_occurrences(freq1[i], message)
        dictionary[freq1[i]] = occurrences

    sorted_dic = dict(sorted(dictionary.items(), key=lambda item: item[1], reverse=True))

    first_key_most_occurrences = next(iter(sorted_dic))

    # Obtenim el primer item que ha aparegut més cops i mirem la diferència que hi ha entre aquest i
    # el primer item de la cadena de freqüències
    shift = (abs(alfabet.index(first_key_most_occurrences) - alfabet.index(freq1[0])))

    # --------------------------------

    return shift


def uoc_find_alphabet(message):
    """
    EXERCISE 2.2: Find or approximate the used substitution alphabet
    :message: encrypted message
    :return: estimated substitution alphabet
    """

    subs_alphabet = ""

    #### IMPLEMENTATION GOES HERE ####
    dictionary = {}

    # Busquem totes les vegades que tenim cada caracter en el text, i ho guardem en un diccionari per tal de poder ordenar els
    # caràcters en ordre descent pel nombre de vegades que han aparegut cada caràcter.
    for i in range(len(freq2)):
        occurrences = find_all_occurrences(freq2[i], message)
        dictionary[freq2[i]] = occurrences

    sorted_dic = dict(sorted(dictionary.items(), key=lambda item: item[1], reverse=True))

    # Obtenim les claus ja previament ordenades i les posem en un nou diccionari clau:valor,
    # Llavors fem que les claus siguin els caràcters que em trobat ordenats i el valor sigui
    # el caràcter segons la cadena de distribució de freqüències que li toca per l'ordre que té.
    keys_values = sorted_dic.keys()
    alphabet_dictionary = {}

    for i, key in enumerate(keys_values):
        alphabet_dictionary[key] = freq2[i]

    # Ordenem el segon diccionari pels valors que ens marca la cadena de distribució de freqüències
    # que previament haviem trobat, i ho retornem com a string finalment.
    sorted_dic2 = dict(sorted(alphabet_dictionary.items(), key=lambda item: item[1], reverse=False))

    subs_alphabet = "".join(sorted_dic2.keys())
    # --------------------------------
    return subs_alphabet


def uoc_custom_cipher(message):
    """
    EXERCISE 3.1: Custom cipher
    :message: message to cipher (plaintext)
    :return: ciphered text
    """

    ciphertext = ""

    #### IMPLEMENTATION GOES HERE ####
    length = len(clau)
    length2 = len(alfabet2)
    index_substitucio_polialfabetica = lambda m, k, n: (m + (k % n)) % length2

    # Aquesta implementació és directament la funció de xifrat que surt en el mòdul 1, pàgina 18
    for i, key in enumerate(message):
        index = index_substitucio_polialfabetica(alfabet2.index(key), i, length)

        ciphertext += alfabet2[index]
    # --------------------------------

    return ciphertext


def uoc_custom_decipher(message):
    """
    EXERCISE 3.2: Custom decipher
    :message: message to cipher (plaintext)
    :return: ciphered text
    """

    plaintext = ""

    #### IMPLEMENTATION GOES HERE ####
    length = len(clau)
    length2 = len(alfabet2)
    index_desxifrat_substitucio_polialfabetica = lambda c, k, n: (c - (k % n)) % length2

    # Aquesta implementació és directament la funció de desxifrat que surt en el mòdul 1, pàgina 18
    for i, key in enumerate(message):
        index = index_desxifrat_substitucio_polialfabetica(alfabet2.index(key), i, length)

        plaintext += alfabet2[index]
    # --------------------------------

    return plaintext
