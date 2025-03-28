import numpy as np


def matrisolustur():
    matris = np.zeros((3, 3))
    for i in range(3):
        for j in range(3):
            matris[i][j] = int(input(f"{i+1}. sütunun {j+1}. satırını giriniz:"))
    return matris


def matrisdegerleri():
    sonuc = np.zeros((3, 1))  # 3x1 boyutunda bir vektör
    for i in range(3):
        sonuc[i][0] = int(input(f"{i+1}. sütunun değeri:"))
    return sonuc


def determinant(matris):
    det = np.linalg.det(matris)
    return det


def cramermetodu(matris, det, sonuc):
    # Matrisin sütunları xicin, yicin ve zicin olarak düzenleniyor
    xicin = np.copy(matris)  # x için kopya
    yicin = np.copy(matris)  # y için kopya
    zicin = np.copy(matris)  # z için kopya

    # Sonuç vektörünü her sütuna yerleştiriyoruz
    xicin[:, 0] = sonuc[:, 0]  # 1. sütun x için
    yicin[:, 1] = sonuc[:, 0]  # 2. sütun y için
    zicin[:, 2] = sonuc[:, 0]  # 3. sütun z için

    # Determinant hesaplanıyor
    xdet = np.linalg.det(xicin)
    ydet = np.linalg.det(yicin)
    zdet = np.linalg.det(zicin)

    # Cramer metoduyla çözüm
    x = xdet / det
    y = ydet / det
    z = zdet / det

    return x, y, z


# Ana işlem sırası
matris = matrisolustur()
sonuc = matrisdegerleri()
det = determinant(matris)

if det != 0:
    cevaplar = cramermetodu(matris, det, sonuc)
    print(f"x: {cevaplar[0]}\ny: {cevaplar[1]}\nz: {cevaplar[2]}")
else:
    print("Matrisin determinantı sıfır, çözüm yok!")

print("\nMatrisiniz:")
print(matris)
print("\nMatris Sonucu:")
print(sonuc)
print(f"Matrisinizin determinantı: {det}")
