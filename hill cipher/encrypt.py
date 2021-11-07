import math
import string
import sys

import numpy as np
from sympy import Matrix

# definiranje abecede
def get_abeceda():
    abeceda = {}
    for character in string.ascii_uppercase:
        abeceda[character] = string.ascii_uppercase.index(character)

    reverse_abeceda = {}
    for key, value in abeceda.items():
        reverse_abeceda[value] = key

    return abeceda, reverse_abeceda


# provjeri uneseni tekst
def tekst_unos(message, abeceda):
    while True:
        text = input(message)
        text = text.upper()
        if all(keys in abeceda for keys in text):
            return text
        else:
            print("\nTekst moze sadrzavati samo slova engleske abecede ([A to Z] ili [a to z]).")


# provjera kljuca
def is_square(key):
    key_length = len(key)
    if 2 <= key_length == int(math.sqrt(key_length)) ** 2:
        return True
    else:
        return False


# Create the matrix k for the key
def get_key_matrix(key, abeceda):
    k = list(key)
    m = int(math.sqrt(len(k)))
    for (i, character) in enumerate(k):
        k[i] = abeceda[character]

    return np.reshape(k, (m, m))


def get_text_matrix(text, m, abeceda):
    matrix = list(text)
    remainder = len(text) % m
    for (i, character) in enumerate(matrix):
        matrix[i] = abeceda[character]
    if remainder != 0:
        for i in range(m - remainder):
            matrix.append(25)

    return np.reshape(matrix, (int(len(matrix) / m), m)).transpose()


def encrypt(key, plaintext, abeceda):
    m = key.shape[0]
    m_grams = plaintext.shape[1]

    ciphertext = np.zeros((m, m_grams)).astype(int)
    for i in range(m_grams):
        ciphertext[:, i] = np.reshape(np.dot(key, plaintext[:, i]) % len(abeceda), m)
    return ciphertext


def Matrica_U_Tekst(matrix, order, abeceda):
    if order == 't':
        text_array = np.ravel(matrix, order='F')
    else:
        text_array = np.ravel(matrix)
    text = ""
    for i in range(len(text_array)):
        text = text + abeceda[text_array[i]]
    return text



def main():

            abeceda, reverse_abeceda = get_abeceda()
        
            plaintext = tekst_unos("\nUnesi tekst: ", abeceda)
            key = tekst_unos("Unesi kljuc: ", abeceda)

            if is_square(key):
            
                k = get_key_matrix(key, abeceda)
                print("\nMatrica kljuca:\n", k)

                p = get_text_matrix(plaintext, k.shape[0], abeceda)
                print("Plaintext matrica:\n", p)

                c = encrypt(k, p, abeceda)

                ciphertext = Matrica_U_Tekst(c, "t", reverse_abeceda)

                print("\nCiphertext: ", ciphertext,"\n")
                print("Ciphertext Matrica:\n", c, "\n")
            else:
                print("\nDužina ključa nije dobra (>=2).\n")


if __name__ == '__main__':
    main()