import random

import Utils as Ut
import sympy as sp
import math

alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
            "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " ",
            "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]


def encrypt(key: sp.Matrix, data: str) -> str:
    numbers: [int] = Ut.getNumbers(data, alphabet)
    resultIndexes: [int] = []

    length = len(key.row(0))
    count = math.ceil(len(data) / length)

    for i in range(count):
        vector = []
        for j in range(length):
            try:
                vector.append(numbers[length * i + j])
            except:
                vector.append(26)

        vector = sp.Matrix([vector]).T
        finalVector: sp.Matrix = key * vector

        for j in range(length):
            resultIndexes.append(finalVector[j, 0])

    alphabetLen = len(alphabet)
    for i in range(0, len(resultIndexes)):
        resultIndexes[i] = resultIndexes[i] % alphabetLen

    result = Ut.getLetters(resultIndexes, alphabet)

    return result


def decrypt(key: sp.Matrix, data: str) -> str:

    key = Ut.getInvByMod(key, len(alphabet))

    return encrypt(key, data)

def generateRandKey(side: int) -> sp.Matrix:
    key: sp.Matrix = sp.zeros(side, side)

    while key.det() == 0:
        mod = len(alphabet)
        for j in range(side):
            for i in range(side):
                key[j, i] = random.randint(0, mod)

    return key


# https://habr.com/ru/articles/710890/
def getKeyByText(encrypted: str, text: str) -> sp.Matrix:
    size = len(encrypted)
    if size != len(text): return

    side = int(size ** 0.5)
    C: sp.Matrix = sp.zeros(side, side)
    P: sp.Matrix = sp.zeros(side, side)

    ecrN: [int] = Ut.getNumbers(encrypted, alphabet)
    textN: [int] = Ut.getNumbers(text, alphabet)

    for i in range(side):
        for j in range(side):
            C[i, j] = ecrN[i + j * side]
            P[i, j] = textN[i + j * side]
    P = Ut.getInvByMod(P, len(alphabet))
    print(P)
    print(C)
    key = P * C % len(alphabet)
    return key

