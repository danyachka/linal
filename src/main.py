import numpy as np
import src.HillEncryption as HillEncryption

if __name__ == '__main__':

    key: np.matrix = np.matrix([[1, 3], [2, 1]])

    string = "huy huy huy "

    print(HillEncryption.crypt(key, string))
