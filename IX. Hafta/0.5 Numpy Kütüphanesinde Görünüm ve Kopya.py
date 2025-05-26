#Numpy Kütüphanesinde Görünüm ve Kopya

#Kopya ve görünüm arasındaki farklar:

"""
Kopya:
-Yeni bir dizi oluşturur.
-Orijinal dizi değiştirildiğinde kopya etkilenmez.
-Veri bellekte ayrı tutulur.
"""

import numpy as np

orijinal = np.array([1, 2, 3, 4, 5])
kopya = orijinal.copy()
orijinal[0] = 99

print("Orijinal:", orijinal)  # [99 2 3 4 5]
print("Kopya:", kopya)        # [1 2 3 4 5]

"""
Görünüm:
-Orijinal dizinin aynı veri belleğini kullanmaktadır.
-Orijinal dizi değiştiği zaman her ikisi de etkilenir.
"""

orijinal = np.array([1, 2, 3, 4, 5])
gorunum = orijinal.view()
gorunum[0] = 88

print("Orijinal:", orijinal)  # [88 2 3 4 5]
print("Görünüm:", gorunum)    # [88 2 3 4 5]


#Verinin kime ait olduğunu bulmak için .base parametresi kullanılmaktadır.

a = np.array([1, 2, 3])
b = a.copy()
c = a.view()

print("b.base:", b.base)  # None
print("c.base:", c.base)  # [1 2 3]

#Dizi şekli her boyuttaki eleman sayısını göstemektedir. Numpy kütüphanesinde buna shape() fonksiyonu ile erişmekteyiz.
dizi = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print(dizi.shape)  # (2, 4)

#5 BOYUTLU BİR DİZİ OLUŞTURACAK İSEK:
dizi = np.array([1, 2, 3, 4], ndmin=5)
print(dizi.shape)
#ndmin parametresi kaç boyuta ayrılacağını ifade etmektedir.

"""
Bir diziyi reshape methodu ile yeniden düzenleyebiliriz.
"""
print()
degisecek = np.array([1,2,3,4,5,6])
yeni = degisecek.reshape(2,3)
print(yeni)


#1. boyuttan 3. boyuta geçiş için:
degis = np.array([1, 2, 3, 4, 5, 6, 7, 8])
yenidizi = degis.reshape(2,2,2)
print(yenidizi)

"""
Bazen geçersiz veriler girilebilmektedir. Eleman sayısını boyuta göre hesaplamamız gerekmektedir.
arr = np.array([1, 2, 3, 4, 5])
hata kodu:  arr.reshape(3, 2)  # ValueError: Toplam eleman sayısı uyuşmuyor
"""

#Hatanın önüne geçmek için -1 parametresi kullanılır bu sayede numpy otomatik olarak boyut hesabı yapabilmektedir.
print()
arr = np.array([1, 2, 3, 4, 5, 6])
yeni = arr.reshape(2, -1)
print(yeni)
# [[1 2 3]
#  [4 5 6]]


"""
Diziyi tek boyuta indirgemek için -1 parametresini tek bir yerde kullanmamız gerekmektedir.
"""
arr = np.array([[1, 2], [3, 4]])
flat = arr.reshape(-1)
print(flat)  # [1 2 3 4]

#Yeniden şekillendirmeler görüntü mü kopya mı olduğunu bilmek istiyorsak:
arr = np.array([1, 2, 3, 4, 5, 6])
reshaped = arr.reshape(2, 3)

print(reshaped.base)  # [1 2 3 4 5 6]

#Yani orijinal diziyi gösterdiğinden görünümdür.
