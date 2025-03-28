import numpy as np


def matrisolustur():
    matris = np.zeros((3,3))
    for i in range(3):
        for j in range(3):
            matris[i][j] = int(input(f"{i+1}.sütunun {j+1}.satırını giriniz:"))
    return matris
def matrisdegerleri():
    sonuc = np.zeros((1,3))
    for i in range(3):
        sonuc[j][0] = int(input(f"{i+1}. sütunun değeri:"))
    return sonuc
def determinant(matris):
    det = np.linalg.det(matris)
    return det




matris = matrisolustur()
sonuc = matrisdegerleri()
det = determinant(matris)





print("Matrisiniz:")
print(matris)
print(f"Matrisinizin determinantı: {det}")
