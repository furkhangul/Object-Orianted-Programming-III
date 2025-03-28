import numpy as np

dizi = np.ones((3,3))
print(dizi)
"""
Diziyi oluştuduk şimdi ise dizinin içeriğini doldurmak gerekiyor.
"""
for i in range(3):
    for j in range(3):
        dizi[i][j] = int(input(f"{i+1}.sütunun {j+1}. satırını giriniz:"))

print(dizi)
