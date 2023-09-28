import random
import sympy as sp


def getNumbers(data, alphabet) -> [int]:
    data = data.lower()

    numbers: [int] = []

    for letter in data:
        numbers.append(alphabet.index(letter))

    return numbers


def getLetters(data, alphabet) -> str:
    result = ""

    for number in data:
        result += alphabet[int(number)]

    return result


def changeRandomLetters(text: str, alphabet) -> str:
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

def getInvByMod(key: sp.Matrix, mod: int) -> sp.Matrix:
    det = key.det()
    key = key.adjugate() % mod

    det = det % mod

    invDet = pow(det, -1, mod)

    key = key * invDet

    key = key % mod

    return key
