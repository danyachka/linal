import math
import random

import Utils as Ut
import sympy as sp

alphabet = ['а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р',
            'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']

G: sp.Matrix

H: sp.Matrix

n = -1
k = 4
m = -1
letter_len = int(math.log2(len(alphabet)))

def convertTextToBits(text: str) -> str:
    result = ""
    for letter in text:
        this_letter = format(alphabet.index(letter), "b")

        result += "0" * (int(letter_len - len(this_letter))) + this_letter

    print("\nconverted to " + result)
    return result


def defineMatrices():
    global G
    global H
    global m
    global k
    global n

    m = 0
    while 2**m - m - 1 < k:
        m += 1
    n = m + k
    # print(n)
    # print(m)
    # print(k)

    # Create H
    H = sp.zeros(m, n)
    for i in range(n):
        string = format(i + 1, 'b')
        l = len(string)
        for j in range(l - 1, -1, -1):
            H[j, i] = int(string[l - 1 - j])

    # Create G
    c = 0
    u = 0
    H1: sp.Matrix = sp.zeros(m, k)
    for i in range(n):
        if i + 1 == 2**u:
            u += 1
            #print(i)
            continue
        for j in range(m):
            H1[j, c] = H[j, i]
        c += 1

    G = sp.zeros(k, n)
    u = 0
    q = 0
    H1 = H1.T
    for i in range(n):
        if i + 1 != 2**u:
            #print(i + 1)
            G[q, i] = 1
            q += 1
            continue
        for j in range(k):
            #print("j is " + str(j))
            G[j, i] = H1[j, u]
        u += 1
    G = G % 2


def encryptMessage(text: str, key: sp.Matrix) -> str:
    result = ""
    data: str = convertTextToBits(text)
    l = k
    #print(len(data))
    count = int(len(data) / l)
    for i in range(count):
        numbers: str = data[l * i: l*(i+1)]
        vector = sp.Matrix([[int(number) for number in numbers]]) % 2

        vector = vector * key % 2

        for num in vector:
            result += str(num)
    return result


def fixError(vect: sp.Matrix):
    position = 0

    number = vect * H.T % 2
    text = ""
    for i in range(len(number)): text += str(number[i])

    position = int(text, 2) - 1
    if position == -1:
        print("No error there")
        return

    errorNumber = vect[0, position]
    if errorNumber == 1: errorNumber = 0
    else: errorNumber = 1

    vect[0, position] = errorNumber
    print("Syndrom was at position " + str(position))


def removeAuxiliaryBits(vect: sp.Matrix) -> [int]:
    array = []
    u = 0
    for i in range(len(vect)):
        if i + 1 == 2**u:
            u += 1
            continue
        array.append(vect[0, i])
    return array


def changeRandomBit(text: str, count) -> str:
    l = len(text)

    for i in range(count):
        position = random.randint(0, l - 1)

        symbol = "0"
        if text[position] == "0": symbol = "1"
        text = text[:position] + symbol + text[position + 1:]
    return text


def decrypt(text: str) -> str:
    fullList: [int] = []
    result = ""
    l = len(text)
    for i in range(l):
        numbers: str = text[n * i: n * (i + 1)]
        if len(numbers) == 0: break
        vector = sp.Matrix([[int(number) for number in numbers]]) % 2
        vect = vector

        fixError(vect)
        fullList += removeAuxiliaryBits(vect)

    realList = []
    for i in range(int(len(fullList) / letter_len)):
        text = ""
        for j in range(letter_len):
            text += str(fullList[i * letter_len + j])

        realList.append(int(text, 2))
    result = Ut.getLetters(realList, alphabet)
    return result


if __name__ == "__main__":
    defineMatrices()
    print("Without any errors:")
    encrypted = encryptMessage("лайм", G)
    print("Encrypted is " + encrypted + "\n")
    decrypted = decrypt(encrypted)
    print("\nDecrypted is " + decrypted + "\n\n")

    for i in range(1, 5):
        print("With " + str(i) + " error:")
        encrypted = encryptMessage("лайм", G)
        encrypted = changeRandomBit(encrypted, i)
        print("Encrypted is " + encrypted + "\n")
        decrypted = decrypt(encrypted)
        print("\nDecrypted is " + decrypted + "\n\n")
