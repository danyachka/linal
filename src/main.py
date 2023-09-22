import sympy as sp
import src.HillEncryption as HillEncryption


def firstPart():
    print("Enter text to encrypt")
    data = input()

    keys = [sp.Matrix([[1, 3], [2, 1]]), sp.Matrix([[1, 3, 5], [11, 4, 9], [2, 21, 18]]),
            sp.Matrix([[18, 3, 5, 16], [11, 4, 9, 27], [2, 21, 18, 13], [4, 14, 16, 23]])]

    for i in range(len(keys)):
        text = data
        key = keys[i]
        print("\n\nMatrix with side " + str(len(key)))
        print("Determinant is " + str(key.det()))
        text = HillEncryption.encrypt(key.copy(), text)
        print("Encrypted text: " + text)
        newText = HillEncryption.changeRandomLetters(text)
        print("Changed encrypted text: " + newText)
        print("Decryption of changed text: " + HillEncryption.decrypt(key.copy(), newText))
        print("Decryption of real text: " + HillEncryption.decrypt(key.copy(), text))


if __name__ == '__main__':
    print(len(HillEncryption.alphabet))
    firstPart()
