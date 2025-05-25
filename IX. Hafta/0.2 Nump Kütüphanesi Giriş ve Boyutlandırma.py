#Numpy Kütüphanesi

"""
Numpy kütüphanesi Python'da bilimsel hesaplamalar yapmak için kullanılan güçlü bir kütüphanedir.
En temel işlevi çok boyutlu diziler ile veri çalıştırmaktır. Ayrıca matematiksel işlemler, lineer cebir, istatistik
ve Fourier dönüşümleri gibi işlemler için de kullanılmaktadır.

IDE'lerin çoğunda hazır olarak indirilmiş olarak gelmesine rağmen indirilmemesine karşın
pip install numpy komutu ile terminal üzerinde indirebiliriz.
"""

import numpy as np

#Sürüm kontrolü için

print(np.__version__)


#Numpy ile liste üzerinden dizi oluşturmak istersek
dizi = np.array([1,2,3,4,5,6,7,8,9,0])
print(dizi)

#Dizi kontrolü için:
print(type(dizi))

#Numpy ile tuple üzerinden dizi oluşturmak istersek
dizi2 = np.array((1,2,3,4,5,6,7,8,9,0))
print(dizi2)

"""
Numpy dizileri birden fazla boyutlu olabilmektedir. Bunun için köşeli parantezler kullanılmaktadır.
"""
#0 Boyutlu dizi için ( Tek değer için )
tekboyut = np.array(42)
print(tekboyut)

#1 Boyutlu dizi için ( Düz liste )
birboyut = np.array([1,2,3,4,5,6,7,8,9,0])
print(birboyut)

#2 Boyutlu dizi için ( Matris )
ikiboyut = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(ikiboyut)

#3 Boyutlu dizi için ( Matris Koleksiyonu )
ucboyut = np.array([[[1,2,3],[4,5,6],[7,8,9]],[[10,11,12],[13,14,15],[16,17,18]]])
print(ucboyut)


#Boyut sayısını öğrenmek için ndim() fonksiyonu çalıştırılmaktadır.
print()
print(ucboyut.ndim)
