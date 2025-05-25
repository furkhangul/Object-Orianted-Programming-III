#Python da dizi indeksleme işlemleri:
import numpy as np

#1 boyutlu dizilerde inkesleme işlemi
birboyut = np.array([1,2,3,4,5,6,7,8,9,0])
print(birboyut[0] + birboyut[3])

#2 boyutlu dizilerde indeksleme işlemi
ikiboyut = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(ikiboyut[1,2]) # 1. satır, 2. sütun = 2

#3 boyutlu dizilerde indekseleme işlemi
ucboyut = np.array([[[1,2,3],[4,5,6],[7,8,9]],[[10,11,12],[13,14,15],[16,17,18]]])
print(ucboyut[0,1,2]) # 0. blok, 1. satır, 2. sütun = 6


#Negatif indeskleme işlemleri için:
print()
dizi = np.array([1, 2, 3, 4])
print(dizi[-1])

dizi2 = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(dizi2[0, -1])

dizi3 = np.array([[[1,2,3],[4,5,6],[7,8,9]],[[10,11,12],[13,14,15],[16,17,18]]])
print(dizi3[1,0,-1])



#Numpy de dizi dillendirme
"""
dizi[start : end : step]

start: Başlangıç indeksidir (dahil)

end: Bitiş indeksidir (hariç)

step: Kaçar kaçar alınacağı
"""

dizi = np.array([1, 2, 3, 4, 5, 6, 7])

print(dizi[1:5])     # [2 3 4 5]
print(dizi[4:])      # [5 6 7]
print(dizi[:4])      # [1 2 3 4]
print(dizi[-3:-1])   # [5 6]
print(dizi[1:5:2])   # [2 4]
print(dizi[::2])     # [1 3 5 7]

#2 Boyutlu dizi dillendirme
print()
dizi = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print(dizi[0:2, 2])     # Her iki satırdan 3. sütun [3 8]
print(dizi[1, 1:4])     # İkinci satırdan 2. ile 4. sütun [7 8 9]


"""
Özetle: 

np.array()	Dizi oluşturur
.ndim	Dizi boyutu
[]	İndeksleme
[start:end:step]	Dilimleme
as np	Takma ad (alias)
"""
