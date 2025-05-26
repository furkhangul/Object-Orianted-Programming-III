#Numpy'de Arama, Sıralama ve Filtreleme


import numpy as np

#np.where() koşula uyan indisleri verir.
dizi = np.array([1, 2, 3, 4, 5, 4, 4])
np.where(dizi == 4)   # (array([3, 5, 6]),)

#Çift sayıları bulmak için:
print(np.where(dizi % 2 == 0))

#np.searchsorted(): Bir değerin sıralı bir diziye nereye ekleneceğini bulur.
dizi = np.array([6, 7, 8, 9])
np.searchsorted(dizi, 7)               # 1 → soldan arar
np.searchsorted(dizi, 7, side='right') # 2 → sağdan arar
np.searchsorted([1, 3, 5, 7], [2, 4, 6])  # → [1, 2, 3]


#np.sort(): Diziyi küçükten büyüğe sıralar.
np.sort([3, 2, 0, 1])           # → [0, 1, 2, 3]
np.sort(['muz', 'kiraz', 'elma'])  # → ['elma', 'kiraz', 'muz']
np.sort([True, False, True])   # → [False, True, True]


#İki boyutlu diziyi sıralamak için:
dizi = np.array([[3, 2, 4], [5, 0, 1]])
np.sort(dizi)
# [[2 3 4]
#  [0 1 5]]


#Filtreleme = Koşula uyan elemanları seçmek
diziler = np.array([41, 42, 43, 44])
filtre = [True, False, True, False]
diziler[filtre]  # → [41 43]

#Koşul ile filtre dizisi oluşturma
filtre = dizi > 42
yeni_dizi = dizi[filtre]  # → [43 44]


#Sadece çift sayıları alma
arr = np.array([1, 2, 3, 4, 5, 6, 7])
filtre = arr % 2 == 0
yeni = arr[filtre]  # → [2 4 6]


"""
Değer arama	np.where()	Koşula uyan indeksleri verir
Sıralı arama	np.searchsorted()	Bir değerin sıralı diziye ekleneceği yer
Sıralama	np.sort()	Diziyi küçükten büyüğe sıralar
Filtreleme	dizi[koşul]	Koşula uyan elemanları alır
"""

