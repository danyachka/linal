import random
import sympy as sp
import math

alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
            "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " ",
            "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]


def encrypt(key: sp.Matrix, data: str) -> str:
    numbers: [int] = getNumbers(data)
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

    result = getLetters(resultIndexes)

    return result


def decrypt(key: sp.Matrix, data: str) -> str:
    mod = len(alphabet)

    det = key.det()
    key = key.adjugate() % mod

    det = det % mod

    invDet = pow(det, -1, mod)

    key = key * invDet

    return encrypt(key, data)


def getNumbers(data) -> [int]:
    data = data.lower()

    numbers: [int] = []

    for letter in data:
        numbers.append(alphabet.index(letter))

    return numbers


def getLetters(data) -> str:
    result = ""

    for number in data:
        result += alphabet[int(number)]

    return result


def changeRandomLetters(text: str) -> str:
    length = len(text)

    count = 3
    if length < 4:
        count = 1

    size = len(alphabet)
    for j in range(count):
        i = random.randint(0, length - 1)
        new = alphabet[random.randint(0, size - 1)]
        text = text[:i] + new + text[i + 1:]

    return text


