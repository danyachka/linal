import numpy as np
import math

alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
            "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " "]


def crypt(key: np.matrix, data: str) -> str:
    numbers: [int] = getNumbers(data)
    resultIndexes: [int] = []

    length = len(key)
    count = math.ceil(len(data) / length)

    for i in range(count):
        vector = []
        for j in range(length):
            vector.append(numbers[length * i + j])

        vector = np.matrix([vector])

        vector = np.dot(vector, key)

        resultIndexes += list(vector.flat)

    alphabetLen = len(alphabet)
    for i in range(len(resultIndexes)):
        resultIndexes[i] = resultIndexes[i] % alphabetLen

    result = getLetters(resultIndexes)

    return result


def getNumbers(data) -> [int]:
    data = data.lower()

    numbers: [int] = []

    for letter in data:
        numbers.append(alphabet.index(letter))

    return numbers


def getLetters(data) -> str:
    result = ""

    for number in data:
        result += alphabet[number]

    return result
