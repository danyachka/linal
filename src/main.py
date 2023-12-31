import sympy as sp
import Utils as Ut
import src.HillEncryption as HillEncryption
import src.Hemming as Hemming


def firstPart():
    print("Enter text to encrypt")
    data = input()

    keys = [sp.Matrix([[1, 3], [2, 1]]), sp.Matrix([[1, 3, 5], [11, 4, 9], [2, 21, 18]]),
            sp.Matrix([[18, 3, 5, 16], [11, 4, 9, 27], [2, 21, 18, 13], [4, 14, 16, 23]])]

    for i in range(len(keys)):
        text = data
        key = keys[i]
        print("\n\nMatrix with side " + str(int(len(key) ** 0.5)))
        print("Determinant is " + str(key.det()))
        text = HillEncryption.encrypt(key.copy(), text)
        print("Encrypted text: " + text)
        newText = Ut.changeRandomLetters(text, HillEncryption.alphabet)
        print("Changed encrypted text: " + newText)
        print("Decryption of changed text: " + HillEncryption.decrypt(key.copy(), newText))
        print("Decryption of real text: " + HillEncryption.decrypt(key.copy(), text))


def secondPart():
    key: sp.Matrix = HillEncryption.generateRandKey(2)

    superSecretEncrypted = HillEncryption.encrypt(key, "данила")

    gottenText = "фото"
    gottenEncrypted = HillEncryption.encrypt(key, gottenText)
    print("You are super hacker, and you got:\n" +
          gottenEncrypted + " -> " + gottenText +"\n" +
          superSecretEncrypted + " -> " + "??????\n")

    impt = ""
    print("Do you want to become Allan Turing? (y/n)")
    while impt != "y" and impt != "n":
        impt = input()

    if impt == "n": return
    key = HillEncryption.getKeyByText(gottenEncrypted, gottenText)
    secretText = HillEncryption.decrypt(key, superSecretEncrypted)
    print("\n\nNice, second message - " + secretText)
    print("key is ")
    print(key)

def thirdPart():
    Hemming.defineMatrices()
    print("Without any errors:")
    encrypted = Hemming.encryptMessage("лайм", Hemming.G)
    print("Encrypted is " + encrypted + "\n")
    decrypted = Hemming.decrypt(encrypted)
    print("\nDecrypted is " + decrypted + "\n\n")

    for i in range(1, 5):
        print("With " + str(i) + " error:")
        encrypted = Hemming.encryptMessage("лайм", Hemming.G)
        encrypted = Hemming.changeRandomBit(encrypted, i)
        print("Encrypted is " + encrypted + "\n")
        decrypted = Hemming.decrypt(encrypted)
        print("\nDecrypted is " + decrypted + "\n\n")


if __name__ == '__main__':
    firstPart()
    #secondPart()
    #thirdPart()
